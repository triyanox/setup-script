set fish_greeting ""
set -gx EDITOR nvim
set -gx PATH bin $PATH
set -gx PATH ~/bin $PATH
set -gx PATH ~/.local/bin $PATH
set PATH $HOME/.cargo/bin $PATH
set PATH $HOME/.bun/bin $PATH
set PATH $HOME/.deno/bin $PATH
set -gx NPM_DIR $HOME/.npm
set -gx PATH $NPM_DIR/bin $PATH
set -gx PATH /usr/local/bin $PATH
set -gx PATH /opt/homebrew/bin $PATH
set -gx NVM_DIR $HOME/.nvm
set -gx PATH node_modules/.bin $PATH

command -qv nvim && alias vim nvim

starship init fish | source
alias ls "exa -l1"
alias la "exa -a1"
alias ll "exa -a -l"
alias l  "lla -l"
alias g git

alias dmongo "sudo docker run -d -p 27017:27017 --name mongo mongo"
alias smongo "sudo docker stop mongo && sudo docker rm mongo"
alias dmysql "sudo docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=secret mysql"
alias mysql_del_db 'sudo docker exec -it mysql mysql -uroot -psecret -e "DROP DATABASE IF EXISTS db_name"'
alias createDB "sudo docker exec -it mysql mysql -uroot -psecret -e 'CREATE DATABASE IF NOT EXISTS db_name'"
alias listDB "sudo docker exec -it mysql mysql -uroot -psecret -e 'SHOW DATABASES' | grep -v Database"
alias smysql "sudo docker stop mysql && sudo docker rm mysql"
alias dmysql5 "sudo docker run -d -p 3306:3306 --name mysql5 -e MYSQL_ROOT_PASSWORD=secret mysql:5.7"
alias smysql5 "sudo docker stop mysql5 && sudo docker rm mysql5"
alias listDB5 "sudo docker exec -it mysql5 mysql -uroot -psecret -e 'SHOW DATABASES' | grep -v Database"
alias createDB5 "sudo docker exec -it mysql5 mysql -uroot -psecret -e 'CREATE DATABASE IF NOT EXISTS db_name'"
alias listTablesinStrapi "sudo docker exec -it mysql5 mysql -e 'use strapi; show tables;' -uroot -psecret"
alias dredis "sudo docker run -d -p 6379:6379 --name redis redis"
alias sredis "sudo docker stop redis && sudo docker rm redis"
alias dpostgres "sudo docker run -d -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=secret postgres"
alias spostgres "sudo docker stop postgres && sudo docker rm postgres"
alias create-postgres-db "sudo docker exec -it postgres psql -U postgres -c 'CREATE DATABASE vercel'"

alias nextapp "yarn create next-app --ts"
alias reactapp "yarn create react-app --typescript"
alias gatsbyapp "yarn create gatsby"
alias expressapp "yarn create express-app"


