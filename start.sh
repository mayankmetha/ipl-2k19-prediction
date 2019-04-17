#!/bin/bash
#clean up
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m"
rm -rf out/ > /dev/null 2>&1
mkdir out out/prediction out/clustering out/pvp > /dev/null 2>&1
rm datasets/teamList/* > /dev/null 2>&1
rm datasets/PlayerStatsIPL/* > /dev/null 2>&1
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m\n"
#data mining team list
cd miners
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m"
python3 teamListMiner.py 
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m\n"
cd ..
#data mining player stats
cd miners
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m"
xterm -geometry 120x25+0+0 -T "IPL DATAMINER" -e "python3 iplMiner.py" > /dev/null 2>&1
if [ -f 'status' ]
then
    s=`cat status|head -1`
    rm status > /dev/null 2>&1
else
    s=0
fi
if [[ $s -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m\n"
cd ..
#clustering
cd clustering
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m"
python3 kmeans.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m\n"
cd ..
#cluster mapping to probability
cd pvp
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mapping Cluster Data\033[0m"
python3 mapping.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mapping Cluster Data\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mapping Cluster Data\033[0m\n"
cd ..
exit
## TODO: add prob averaging here
#gui step 1
cd prediction
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m"
python3 selectPlayers.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
cd ..
#gui step 2
team0=`cat ./out/prediction/teams|head -1`
cd prediction
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m"
python3 playingSquad.py 0 > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
cd ..
#gui step 3
team1=`cat ./out/prediction/teams|tail -1`
cd prediction
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m"
python3 playingSquad.py 1 > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"
cd ..
#gui step 4
cd prediction
echo -ne "\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m"
python3 prediction/toss.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[1;37m[\033[0m\033[1;31m✘\033[0m\033[1;37m]\033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m\n"
    exit
fi
echo -ne "\r\033[1;37m[\033[0m\033[1;32m✔\033[0m\033[1;37m]\033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m\n"
cd ..