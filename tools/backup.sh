#/bin/bash

PWD=/workspaces/WarhammerFantasyRoleplayVirtualGM/WarhammerFantasyRoleplayVirtualGM_site
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

cp ${PWD}/db.sqlite3 ${PWD}/backup/${TIMESTAMP}_db.sqlite3
/workspaces/WarhammerFantasyRoleplayVirtualGM/WarhammerFantasyRoleplayVirtualGM_site/manage.py dumpdata > ${PWD}/backup/${TIMESTAMP}_wfrpg.json
sqlite3 ${PWD}/db.sqlite3 ".dump" > ${PWD}/backup/${TIMESTAMP}_wfrpg.sql