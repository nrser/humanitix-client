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

Generation
------------------------------------------------------------------------------

> All commands run from the repo root.

You need to have [uv][] available. If you're using `nix`, you can run
`nix-shell` to drop into a shell with it available.

[uv]: https://docs.astral.sh/uv/

### Clean ###

Probably want to remove the existing files first:

```shell
rm -rf \
    ./.ruff_cache \
    ./humanitix_client \
    ./.gitignore \
    ./pyproject.toml \
    ./README.md 
```

Initially, I used the schema from
<https://api.humanitix.com/v1/documentation/json>, but it has some errors that
needed to be fixed, so it got pulled down locally with

```shell
curl -o schema.json https://api.humanitix.com/v1/documentation/json
```

That file then has edits applied to it.

### Generate ###

```shell
uvx --from openapi-python-client openapi-python-client generate \
    --path ./schema.json \
    --config ./openapi-python-client.yaml \
    --output-path . \
    --overwrite
```

### Preserving Edits ###

After that, I edited the two code blocks at the start of `README.md` to
construct the client correctly:

```python
from humanitix_client import Client

client = Client(base_url="https://api.humanitix.com/")
```

and:

```python
from humanitix_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.humanitix.com/",
    token="SuperSecretToken",
    auth_header_name="X-Api-Key",
    prefix="",
)
```

If you're updating the generation though you can just discard the edits to
`README.md` after generating to achieve the same effect. You'll want to discard
edits to `.gitignore` as well to preserve changes:

```shell
git checkout README.md .gitignore
```

### Bumping Version ###

We're adding an additional 4th version segment to track patches, for example
`1.18.0.1` as a patch to schema `1.18.0`.

Edit the `version` in `pyproject.toml` and commit it.

Publishing
------------------------------------------------------------------------------

[openapi-python-client][] uses [poetry][] setup in `pyproject.toml` by default,
and has some other options, but [uv][] is not one of them. I'm going to try
using [poetry][] through [uv][] to build and publish the package.

[openapi-python-client]: https://github.com/openapi-generators/openapi-python-client
[poetry]: https://python-poetry.org/

Build:

```shell
uvx --from poetry poetry build
```

Publish:

```shell
export PYPI_TOKEN=...  # pypi-XXXX
uvx --from poetry poetry publish -u __token__ -p "$PYPI_TOKEN"
```

