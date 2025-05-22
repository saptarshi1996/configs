import os
import sys

shared_content_template = """
# ─────────────────────────────────────────────────────────────
# Common Aliases & Environment Setup
# ─────────────────────────────────────────────────────────────

alias cl="clear"
alias vzshrc="vim ~/.zshrc"
alias szshrc="source ~/.zshrc"
alias szprofile="source ~/.zprofile"
alias iterm2reset="defaults delete com.googlecode.iterm2 && \\
  rm ~/Library/Preferences/com.googlecode.iterm2.plist"

# ───────────────
# Git Shortcuts
# ───────────────
alias gadd="git add"
alias gcommit="git commit"
alias gcommitm="git commit -m"
alias gcout="git checkout"
alias gcoutb="git checkout -b"
alias gpull="git pull"
alias gpullog="git pull origin"
alias gpush="git push"
alias gpushup="git push --set-upstream origin"
alias gcpick="git cherry-pick"
alias gstash="git stash"
alias gfetch="git fetch"
alias gstatus="git status"
alias gbranch="git branch"
alias greset="git reset"
alias gdiff="git diff"
alias gconfig="git config"
alias gconfigname="git config user.name"
alias gconfigemail="git config user.email"
alias gcreds="git config credential.helper store"
alias gabort="git merge --abort"

# ─────────────────────────────────────────
# Docker Environment & Shortcuts
# ─────────────────────────────────────────
unset DOCKER_TLS_VERIFY
unset DOCKER_CERT_PATH
unset DOCKER_MACHINE_NAME
unset DOCKER_HOST

alias dkcpup="docker compose up"
alias dkcpdn="docker compose down"
alias dkcimgprune="docker image prune"
alias dkcprune="docker system prune"

# ───────────────
# Python Helpers
# ───────────────
alias python="python3"
alias pyvenv="python3 -m venv"
alias pyinstall="pip3 install"

# ─────────────────────────────
# Editor Launch Shortcuts
# ─────────────────────────────
alias vcode="open -b com.microsoft.VSCode"

# ──────────────
# Navigation
# ──────────────
alias goprojects="cd ~/Developer/projects && ls"
alias goconfigs="cd ~/Developer/projects/configs && ls"
alias goscripts="cd ~/Developer/scripts && ls"
alias gonotes="cd ~/Developer/notes && ls"
alias back="cd ~/ && clear"

# ────────────────────────────────────────────────
# Applications & Developer Tools
# ────────────────────────────────────────────────
alias aopen="open -a"
alias openall="{{OPEN_COMMANDS}}"

# ─────────────────────────────
# Cache Management
# ─────────────────────────────
alias clearcache="rm -rf ~/Library/Caches/"
alias sizecache="du -h ~/Library/Caches/"

# ─────────────
# Dock Settings
# ─────────────
alias dockmax="defaults delete com.apple.dock tilesize && \\
  defaults write com.apple.dock magnification -bool false && \\
  defaults write com.apple.dock autohide -bool false && \\
  killall Dock"

alias dockmin="defaults write com.apple.dock tilesize -int 16 && \\
  defaults write com.apple.dock magnification -bool true && \\
  defaults write com.apple.dock largesize -float 80 && \\
  defaults write com.apple.dock autohide -bool true && \\
  killall Dock"

alias dockleft="defaults write com.apple.dock orientation -string \\
    'left' && killall Dock"
alias dockdown="defaults write com.apple.dock orientation -string \\
  'bottom' && killall Dock"

alias dockhide="defaults write com.apple.dock autohide -bool true && \\
    killall Dock"
alias dockshow="defaults write com.apple.dock autohide -bool false && \\
    killall Dock"

alias dockfast="defaults write com.apple.dock autohide-delay -float 0 && \\
    defaults write com.apple.dock autohide-time-modifier -int 0 && \\
    killall Dock;"
alias dockslow="defaults delete com.apple.dock autohide-delay && \\
    defaults delete com.apple.dock autohide-time-modifier && killall Dock;"

# ─────────────
# NVM Settings
# ─────────────
export NVM_DIR="$HOME/.nvm"
[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \\
  . "/opt/homebrew/opt/nvm/nvm.sh"

[ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \\
  . "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"

# ─────────────────
# Homebrew Setup
# ─────────────────
eval "$(/opt/homebrew/bin/brew shellenv)"

alias brewall="brew update && brew upgrade && \\
  brew autoremove && brew cleanup --prune=all && clearcache"
"""

default_only = """
# ────────────────────────────────────────────────
# Default zsh-only aliases and settings
# ────────────────────────────────────────────────

# Directory Listings
alias ll='ls -alF --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'

# Case-Insensitive Autocompletion
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'

"""

omz_only = """
# ─────────────────────────────
# Oh My Zsh setup
# ─────────────────────────────

# Oh My Zsh base directory
export ZSH="$HOME/.oh-my-zsh"

# Zsh theme (can be changed to your preference)
ZSH_THEME="simple"

# Load Oh My Zsh
source $ZSH/oh-my-zsh.sh

"""


def build_open_aliases(file_path):
    if not os.path.exists(file_path):
        print(f"📝 {file_path} not found. Creating it...")
        with open(file_path, "w") as f:
            f.write("")
    with open(file_path, "r") as f:
        apps = [line.strip() for line in f if line.strip()]

    open_commands = [
        f"{app}"
        if app.startswith(("code", "subl", "open"))
        else f"open -a {app}" for app in apps]

    return open_commands


def write_and_source(zsh_type, open_command):
    home_zshrc = os.path.expanduser("~/.zshrc")

    shared_content = shared_content_template.replace(
        "{{OPEN_COMMANDS}}",
        open_command
    )

    if zsh_type == "default":
        content = f"{default_only.strip()}\n\n{shared_content.strip()}\n"
    elif zsh_type == "omz":
        content = f"{omz_only.strip()}\n\n{shared_content.strip()}\n"
    else:
        print("❌ Invalid argument. Use 'default' or 'omz'.")
        return

    with open(home_zshrc, "w") as f:
        f.write(content)

    print(f"✅ ~/.zshrc updated with {zsh_type} config.")
    print("⚠️  Please restart your terminal to view changes.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 set_zshrc.py [default|omz]")
    else:
        default, custom = "defaultopen", "customopen"

        default_open_aliases = build_open_aliases(default)
        custom_open_aliases = build_open_aliases(custom)

        open_alias_list = default_open_aliases + custom_open_aliases
        open_command = " && \\\n  ".join(open_alias_list)

        zsh_type = sys.argv[1].lower()

        write_and_source(
            zsh_type=zsh_type,
            open_command=open_command,
        )
