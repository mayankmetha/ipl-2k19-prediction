#!/bin/bash
#parallel data miner
if ! type xterm > /dev/null 2>&1
then
    echo "Install xterm"
    exit
fi
xterm -geometry 120x25+0+0 -T "IPL DATAMINER" -e "python3 iplMiner.py" &
xterm -geometry 120x25+0+400 -T "CRICINFO DATAMINER" -e "python3 cricinfoMiner.py" &