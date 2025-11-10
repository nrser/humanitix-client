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

Probably want to remove the existing files first:

```shell
rm -rf \
    ./.ruff_cache \
    ./humanitix_client \
    ./.gitignore \
    ./pyproject.toml \
    ./README.md 
```

Then generate new ones:

```shell
uvx --from openapi-python-client openapi-python-client generate \
    --url https://api.humanitix.com/v1/documentation/json \
    --config ./openapi-python-client.yaml \
    --output-path . \
    --overwrite
```

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

