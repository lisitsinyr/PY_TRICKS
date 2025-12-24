# Installing uv
## Installation methods
Install uv with our standalone installers or your package manager of choice.

### Standalone installer
uv provides a standalone installer to download and install uv:

**Windows**

Use irm to download the script and execute it with iex:

`pwsh -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Changing the execution policy allows running a script from the internet.

Request a specific version by including it in the URL:

`pwsh -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.9.18/install.ps1 | iex"`

### PyPI
For convenience, uv is published to PyPI.

If installing from PyPI, we recommend installing uv into an isolated environment, e.g., with pipx:

`pipx install uv`

However, pip can also be used:

`pip install uv`

### Homebrew
uv is available in the core Homebrew packages.

`brew install uv`

### WinGet
uv is available via WinGet.

`winget install --id=astral-sh.uv  -e`