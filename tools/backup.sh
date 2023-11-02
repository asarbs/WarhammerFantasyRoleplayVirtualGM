#/bin/bash

set -o xtrace


HOSTNAME=$(hostname)
PWD=/workspaces/WarhammerFantasyRoleplayVirtualGM/WarhammerFantasyRoleplayVirtualGM_site
if [ "$HOSTNAME" = warhammer ]; then
    PWD=/var/www/django/WarhammerFantasyRoleplayVirtualGM/WarhammerFantasyRoleplayVirtualGM_site
    source /var/www/django/WarhammerFantasyRoleplayVirtualGM/wfrpg_venv/bin/activate
fi
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

find  ${PWD}/backup -type f -ctime +7 | xargs rm -rf
${PWD}/manage.py dumpdata > ${PWD}/backup/${TIMESTAMP}_wfrpg.json