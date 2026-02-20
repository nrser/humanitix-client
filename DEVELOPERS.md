Developer Notes
==============================================================================

This package is generated with OpenAPI, which writes `README.md`. This file is a
place for instructions and information about generating the package that won't
be overwritten in the process.

The top priority is to keep things super simple. I need this API client for some
volunteer work, and I if I come back to it at all, I'll almost certainly have
forgotten how or why I did everything.

For that reason, I don't want a build system involved. Just read this file and
run some commands.

This is a separate package because I don't want the generated code in-tree on an
actual project. I don't want to see it in search results, I don't want tools
wasting time on it or getting confused by it. I don't want to deal with having
a local vendored package, and I don't want to figure out configuration options
or post-generation steps to convert it into a regular module.

Quick Patch
------------------------------------------------------------------------------

1.  Make adjustments in `humanitix_client/schema.yaml` and **commit** your
    changes. We're going to just wipe the whole `humanitix_client` directory
    and restore that path, because it's much easier.
    
    You may be tempted to simply tweak something in a `.py` file, but then it
    will get clobbered by the next regeneration.

2.  Knock out the generated files:

        rm -rf ./.ruff_cache ./humanitix_client ./.gitignore ./pyproject.toml ./README.md

3.  Restore only `humanitix_client/schema.yaml`:

        git checkout humanitix_client/schema.yaml

4.  Generate:

        uvx --from openapi-python-client openapi-python-client generate \
            --path ./humanitix_client/schema.yaml \
            --config ./openapi-python-client.yaml \
            --output-path . \
            --overwrite

5.  Restore files that are generated but have local modifications:

        git checkout README.md .gitignore pyproject.toml

6.  Use this script to bump the sub-patch version (`x` in `M.m.p.x`) or just do
    it by hand in `pyproject.toml`:

```shell
uv run --no-project python <<'EOF'
import re
v_re = r'version = "([\d.]+)"'

with open('pyproject.toml', 'r') as f:
    content = f.read()

def get_version(content):
    return re.search(v_re, content)[1]

def bump_version(match):
    version = match.group(1)
    parts = version.split('.')
    parts[-1] = str(int(parts[-1]) + 1)
    return f'version = "{".".join(parts)}"'

v_from = get_version(content)
content = re.sub(v_re, bump_version, content)
v_to = get_version(content)

with open('pyproject.toml', 'w') as f:
    f.write(content)

print(f"Version bumped {v_from} -> {v_to} in pyproject.toml")
EOF
```

7.  Make sure that looks ok, commit everything, then:

```shell
tag="v$(uvx --from poetry poetry version --short)" \
&& git tag "$tag" \
&& git push origin "$tag" \
&& uvx --from poetry poetry build \
&& uvx --from poetry poetry publish \
    -u __token__ \
    -p "$(op item get "PyPI" --reveal --fields "api token")"
```

Schema
------------------------------------------------------------------------------

Initially, we used a JSON schema from

https://api.humanitix.com/v1/documentation/json

but that's `404 Not Found` now (2026-02-20).

Now we're using a YAML schema from https://humanitix.stoplight.io/, click the
_Export_ drop-down in the upper right.

Seem to be able to get it directly with:

```shell
curl -o ./humanitix_client/schema.yaml https://stoplight.io/api/v1/projects/humanitix/humanitix-public-api/nodes/apps/public-api/src/docs/openapi.yaml
```

> ❗❗ WARNING ❗❗
> 
> I've made some tweaks to the `schema.yaml` to fix response parsing crashes,
> check out the `git` history of `humanitix_client/schema.yaml`.
>
> If you download a new version, you may need to re-apply those changes.

Versioning
------------------------------------------------------------------------------

We've added an additional 4th version segment to track patches, for example
`1.18.0.1` as a patch to schema `1.18.0`. 

Publishing
------------------------------------------------------------------------------

[openapi-python-client][] uses [poetry][] setup in `pyproject.toml` by default,
and has some other options, but [uv][] is not one of them. I'm going to try
using [poetry][] through [uv][] to build and publish the package.

[openapi-python-client]: https://github.com/openapi-generators/openapi-python-client
[poetry]: https://python-poetry.org/

### Build ###

```shell
uvx --from poetry poetry build
```

### PyPI Token ###

To publish the package to [PyPI][] (at least, how I'm doing it) you'll need to
make the authentication token available in the shell as `$PYPI_TOKEN`.

#### 1Password CLI ####

I'm storing my token in [1Password][], so I'm going to use the [1Password CLI][]
via the [_1password-cli Nix package][] to fetch it out on demand, with the usual
on-demand biometric authorization (macOS fingerprint reader).

[PyPI]: https://pypi.org/
[1Password CLI]: https://developer.1password.com/docs/cli/get-started/
[_1password-cli Nix package]: https://wiki.nixos.org/wiki/1Password

After installing the [_1password-cli Nix package][], followed the instructions
at

<https://developer.1password.com/docs/cli/app-integration/>

I need 1Password 8 for the app/CLI integration to work.

Now this works:

```shell
uvx --from poetry poetry publish \
    -u __token__ \
    -p "$(op item get "PyPI" --reveal --fields "api token")"
```

### Publish ###

```shell
export PYPI_TOKEN=...  # pypi-XXXX
uvx --from poetry poetry publish -u __token__ -p "$PYPI_TOKEN"
```

