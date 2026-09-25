#!/bin/bash
# (c) J~Net 2026
#
# ./start.sh
#
#
if [ -z "$1" ]; then
    read -r -p "Put URL To Transcribe: " user_in
else
    user_in="$1"
fi

#
if [ ! -f "venv/bin/activate" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

source venv/bin/activate

python transcribe.py "$user_in"
