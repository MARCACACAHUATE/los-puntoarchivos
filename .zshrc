# Created by newuser for 5.8.1
export EDITOR=nvim

autoload -U compinit
compinit

zstyle ':completion:*' menu select

setopt completealiases

eval "$(oh-my-posh init zsh --config ~/.poshthemes/agnoster-custom.omp.json)"


alias ls="lsd"
alias ll="ls -la"
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

source /home/marca/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
