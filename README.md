# configs

Personal macOS configs all in one place.

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run all scripts from the repo root.

```sh
# Generate ~/.zshrc (use "default" or "omz" for Oh My Zsh)
python3 zshrc.py default

# Export current VS Code settings and extensions
python3 vscode.py

# Export current Dock items
python3 dock.py

# Record display info
python3 macos.py
```

Restart the terminal after generating `~/.zshrc`.

## Custom open aliases

`zshrc.py` reads `defaultopen` and `customopen`, one command per line, and builds open aliases from them. `defaultopen` is shared and tracked. `customopen` is for local, per-machine entries and is git-ignored.
