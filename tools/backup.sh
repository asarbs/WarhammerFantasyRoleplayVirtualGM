#/bin/bash

PWD=$(pwd)
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

cp ${PWD}/db.sqlite3 ${PWD}/backup/${TIMESTAMP}_db.sqlite3


