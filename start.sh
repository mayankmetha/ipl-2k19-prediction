#!/bin/bash
#data mining team list
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m"
python3 miners/teamListMiner.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m\n"
#data mining player stats
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m"
python3 miners/iplMiner.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m\n"
#clean up
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m"
rm -rf out/ > /dev/null 2>&1
mkdir out out/prediction out/clustering > /dev/null 2>&1
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m\n"
#clustering
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m"
python3 clustering/kmeans.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m\n"
#gui step 1
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m"
python3 prediction/selectPlayers.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
#gui step 2
team0=`cat ./out/prediction/teams|head -1`
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m"
python3 prediction/playingSquad.py 0 > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
#gui step 3
team1=`cat ./out/prediction/teams|tail -1`
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m"
python3 prediction/playingSquad.py 1 > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"
#gui step 4
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m"
python3 prediction/toss.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m\n"
