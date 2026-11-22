# configs

Personal macOS configs all in one place.

## Contents

| File | Description |
|---|---|
| `zshrc.py` | Generates `~/.zshrc` (aliases, git shortcuts, open commands) |
| `bashrc.py` | Template for bash config (currently empty) |
| `vscode.py` | Exports VS Code settings and extensions |
| `vscode.json` | Exported VS Code `settings.json` |
| `vscodeextension` | Exported list of installed VS Code extensions |
| `dock.py` | Exports pinned Dock items |
| `dock` | Exported Dock layout |
| `macos.py` | Records display resolution and color theme (writes `macos.txt`, git-ignored) |
| `defaultopen` | Apps and commands turned into open aliases by `zshrc.py` |
| `customopen` | Machine-specific open aliases (git-ignored, create locally) |
| `terminal` | Terminal.app and iTerm settings notes |
| `sublime.json` | Sublime Text settings |

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
