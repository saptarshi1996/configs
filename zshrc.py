import os
import sys


shared_content = """
# Common Aliases & Environment

# Build zshrc
alias vzshrc="vim ~/.zshrc"
alias szshrc="source ~/.zshrc"

# Git commands
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

# Docker
unset DOCKER_TLS_VERIFY
unset DOCKER_CERT_PATH
unset DOCKER_MACHINE_NAME
unset DOCKER_HOST
alias dkcpup="docker compose up"
alias dkcpdn="docker compose down"
alias dkcprune="docker system prune"

# Python
alias python="python3"
alias pyvenv="python3 -m venv"
alias pyinstall="pip3 install"

# Editor
alias vcode="open -b com.microsoft.VSCode"
alias subl='/Applications/Sublime\\ Text.app/Contents/SharedSupport/bin/subl'

# Navigation
alias goproject="cd ~/Developer/projects && ls"
alias goconfigs="cd ~/Developer/projects/configs"
alias back="cd ~/"

# Open Applications
alias aopen="open -a"
alias openiterm="open -a iterm"
alias opendevelopment="open -a SourceTree && open -a ChatGPT && open -a Postman"
alias opennote="open -a Notes && subl ~/Developer/notes"
alias opencomms="open -a WhatsApp && open -a Mail && open -a Calendar"

# Opens all the above configs
alias openall="openiterm && opendevelopment && opennote && opencomms"

# Cache management
alias clearcache="rm -rf ~/Library/Caches/"
alias sizecache="du -h ~/Library/Caches/"

# NVM
export NVM_DIR="$HOME/.nvm"
[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \\. "/opt/homebrew/opt/nvm/nvm.sh"
[ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \\. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"
"""

default_only = """
# Default zsh-only aliases and settings

alias ll='ls -alF --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'

zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'

"""

omz_only = """
# Oh My Zsh setup

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"

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
