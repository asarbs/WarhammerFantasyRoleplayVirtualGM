#/bin/bash

set -o xtrace

PWD=/workspaces/WarhammerFantasyRoleplayVirtualGM/WarhammerFantasyRoleplayVirtualGM_site
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

find  ${PWD}/backup -type f -ctime +7 | xargs rm -rf
/workspaces/WarhammerFantasyRoleplayVirtualGM/WarhammerFantasyRoleplayVirtualGM_site/manage.py dumpdata > ${PWD}/backup/${TIMESTAMP}_wfrpg.json
