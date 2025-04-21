# ─────────────────────────────
# Oh My Zsh setup
# ─────────────────────────────

# Oh My Zsh base directory
export ZSH="$HOME/.oh-my-zsh"

# Zsh theme (can be changed to your preference)
ZSH_THEME="simple"

# Load Oh My Zsh
source $ZSH/oh-my-zsh.sh

# ─────────────────────────────────────────────────────────────
# Common Aliases & Environment Setup
# ─────────────────────────────────────────────────────────────

# Zsh Configuration
alias vzshrc="vim ~/.zshrc"
alias szshrc="source ~/.zshrc"

# iTerm2 Reset
alias iterm2reset="defaults delete com.googlecode.iterm2 && \
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

# ──────────────
# Navigation
# ──────────────
alias goproject="cd ~/Developer/projects && ls"
alias goconfigs="cd ~/Developer/projects/configs"
alias back="cd ~/"

# ────────────────────────────────────────────────
# Applications & Developer Tools
# ────────────────────────────────────────────────
alias aopen="open -a"
alias openall="open -a iTerm && \
  open -a SourceTree && \
  open -a ChatGPT && \
  open -a Postman && \
  open -a Notes && \
  open -a Mail && \
  open -a Calendar && \
  zed ~/Developer/scripts && \
  zed ~/Developer/notes && \
  open -a WhatsApp && \
  open -a Passwords && \
  zed ~/Developer/projects/configs"

# ─────────────────────────────
# Cache Management
# ─────────────────────────────
alias clearcache="rm -rf ~/Library/Caches/"
alias sizecache="du -h ~/Library/Caches/"

# ─────────────
# Dock Settings
# ─────────────
alias dockmax="defaults delete com.apple.dock tilesize && \
  defaults write com.apple.dock magnification -bool false && \
  defaults write com.apple.dock autohide -bool false && \
  killall Dock"

alias dockmin="defaults write com.apple.dock tilesize -int 16 && \
  defaults write com.apple.dock magnification -bool true && \
  defaults write com.apple.dock largesize -float 64 && \
  defaults write com.apple.dock autohide -bool true && \
  killall Dock"

# ─────────────
# NVM Settings
# ─────────────
export NVM_DIR="$HOME/.nvm"
[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \
  . "/opt/homebrew/opt/nvm/nvm.sh"

[ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \
  . "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"

# ─────────────────
# Homebrew Setup
# ─────────────────
eval "$(/opt/homebrew/bin/brew shellenv)"

alias brewall="brew update && brew upgrade && \
  brew autoremove && brew cleanup"
