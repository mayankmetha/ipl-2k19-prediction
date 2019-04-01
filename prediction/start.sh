#!/bin/bash
python3 selectPlayers.py
if [[ $? -ne 1 ]]
then
    echo "Error occured in selectPlayers.py"
    exit
fi
python3 playingSquad.py 0
python3 playingSquad.py 1