alias ll='ls -alF --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'

alias vzshrc="vim ~/.zshrc"
alias szshrc="source ~/.zshrc"

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

unset DOCKER_TLS_VERIFY
unset DOCKER_CERT_PATH
unset DOCKER_MACHINE_NAME
unset DOCKER_HOST

alias dkcpup="docker compose up"
alias dkcpdn="docker compose down"

alias python="python3"
alias pyvenv="python3 -m venv"
alias pyinstall="pip3 install"

export NVM_DIR="$HOME/.nvm"
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"

zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
