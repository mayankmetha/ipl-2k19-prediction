#!/bin/bash
#clean up
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m"
rm -rf out/prediction > /dev/null 2>&1
mkdir out out/prediction > /dev/null 2>&1
mkdir results > /dev/null 2>&1
if [[ $1 == '-f' ]]
then
    mkdir out/clustering out/pvp > /dev/null 2>&1
    rm datasets/teamList/* > /dev/null 2>&1
    rm datasets/PlayerStatsIPL/* > /dev/null 2>&1
fi
echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Clean Up\033[0m\n"
if [[ $1 == '-f' ]]
then
    #data mining team list
    cd miners
    echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m"
    python3 teamListMiner.py 
    if [[ $? -ne 1 ]]
    then
        echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m\n"
        exit
    fi
    echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mining Teams List\033[0m\n"
    cd ..
    #data mining player stats
    cd miners
    echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m"
    xterm -geometry 60x30+480+160 -T "IPL DATAMINER" -e "python3 iplMiner.py" > /dev/null 2>&1
    if [ -f 'status' ]
    then
        s=`cat status|head -1`
        rm status > /dev/null 2>&1
    else
        s=0
    fi
    if [[ $s -ne 1 ]]
    then
        echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m\n"
        exit
    fi
    echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mining Player Details\033[0m\n"
    cd ..
    #clustering
    cd clustering
    echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m"
    python3 kmeans.py > /dev/null 2>&1
    if [[ $? -ne 1 ]]
    then
        echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m\n"
        exit
    fi
    echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Clustering\033[0m\n"
    cd ..
    #cluster mapping to probability
    cd pvp
    echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Mapping Cluster Data\033[0m"
    python3 mapping.py > /dev/null 2>&1
    if [[ $? -ne 1 ]]
    then
        echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Mapping Cluster Data\033[0m\n"
        exit
    fi
    echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Mapping Cluster Data\033[0m\n"
    cd ..
    #addition of cluster data
    cd pvp
    echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Aggregating Cluster Data\033[0m"
    python3 summing.py > /dev/null 2>&1
    if [[ $? -ne 1 ]]
    then
        echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Aggregating Cluster Data\033[0m\n"
        exit
    fi
    echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Aggregating Cluster Data\033[0m\n"
    cd ..
    #probability calculation
    cd pvp
    echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Computing Probability\033[0m"
    python3 probability.py > /dev/null 2>&1
    if [[ $? -ne 1 ]]
    then
        echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Computing Probability\033[0m\n"
        exit
    fi
    echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Computing Probability\033[0m\n"
    cd ..
fi
#gui step 1
cd prediction
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m"
python3 selectPlayers.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
    exit
fi
echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Select Team & Squad\033[0m\n"
cd ..
#gui step 2
team0=`cat ./out/prediction/teams|head -1`
cd prediction
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m"
python3 playingSquad.py 0 > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
    exit
fi
echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team0\033[0m\n"
cd ..
#gui step 3
team1=`cat ./out/prediction/teams|tail -1`
cd prediction
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m"
python3 playingSquad.py 1 > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"
    exit
fi
echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Configure $team1\033[0m\n"
cd ..
#gui step 4
cd prediction
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m"
python3 toss.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m\n"
    exit
fi
echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Toss\033[0m\n"
cd ..
#simulation step
cd prediction
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Executing \033[0m\033[1;37m:\033[0m\033[1;36m Simulation\033[0m"
python3 prediction.py > /dev/null 2>&1
if [[ $? -ne 1 ]]
then
    echo -ne "\r\033[5;1;31m ✘ \033[0m\033[1;33m Failed    \033[0m\033[1;37m:\033[0m\033[1;36m Simulation\033[0m\n"
    exit
fi
echo -ne "\r\033[5;1;32m ✔ \033[0m\033[1;33m Executed  \033[0m\033[1;37m:\033[0m\033[1;36m Simulation\033[0m\n"
cd ..
#Display output Folders
path="results/"$team0"vs"$team1
winner=`cat $path"/winner" |head -1`
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Winner    \033[0m\033[1;37m:\033[0m\033[1;36m $winner\033[0m\n"
echo -ne "\033[5;1;35m ★ \033[0m\033[1;33m Output    \033[0m\033[1;37m:\033[0m\033[1;36m $path\033[0m\n"
