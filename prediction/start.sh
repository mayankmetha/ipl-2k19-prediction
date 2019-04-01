#!/bin/bash
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m"
rm ../out/prediction/* 1> /dev/null 2>&1
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m\n"
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m"
python3 selectPlayers.py 1> /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
team0=`cat ../out/prediction/teams|head -1`
team1=`cat ../out/prediction/teams|tail -1`
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m"
python3 playingSquad.py 0 1>/dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m"
python3 playingSquad.py 1 1>/dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"