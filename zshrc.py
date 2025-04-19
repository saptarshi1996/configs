import os
import sys

shared_content = """
# ─────────────────────────────────────────────────────────────
# Common Aliases & Environment Setup
# ─────────────────────────────────────────────────────────────

# Zsh Configuration
alias vzshrc="vim ~/.zshrc"
alias szshrc="source ~/.zshrc"

# iTerm2 Reset
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
alias subl='/Applications/Sublime\\ Text.app/Contents/SharedSupport/bin/subl'

# ──────────────
# Navigation
# ──────────────
alias goproject="cd ~/Developer/projects && ls"
alias goconfigs="cd ~/Developer/projects/configs"
alias back="cd ~/"

# ────────────────────────────────────────────────
# Open Common Applications & Developer Tools
# ────────────────────────────────────────────────
alias aopen="open -a"

alias openiterm="open -a iterm"
alias openscripts="code ~/Developer/scripts && \\
  subl ~/Developer/projects/configs"
alias opendevelopment="open -a SourceTree && \\
  open -a ChatGPT && open -a Postman"
alias opennote="open -a Notes && \\
  subl ~/Developer/notes"
alias opencomms="open -a WhatsApp && \\
  open -a Mail && open -a Calendar"

alias openall="openiterm && openscripts && opendevelopment && \\
  opennote && opencomms"

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
  defaults write com.apple.dock largesize -float 64 && \\
  defaults write com.apple.dock autohide -bool true && \\
  killall Dock"

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


def write_and_source(zsh_type):
    home_zshrc = os.path.expanduser("~/.zshrc")

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
        write_and_source(sys.argv[1].lower())
