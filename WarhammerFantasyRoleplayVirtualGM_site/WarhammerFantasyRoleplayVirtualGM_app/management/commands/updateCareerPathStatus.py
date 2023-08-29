from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError

from WarhammerFantasyRoleplayVirtualGM_app.models import Status, CareerPath


class Command(BaseCommand):
    help = "Change CareerPath from text to Status"

    def handle(self, *args: Any, **options: Any) -> str | None:
        for cp in CareerPath.objects.all():
            earning_money = cp.earning_money.split(" ")
            tier = earning_money[0][0]
            level = earning_money[1]
            if tier not in ["B", "S", "G"]:
                raise ValueError("Tier {} must be one of [\"B\", \"S\", \"G\"]".format(tier))
            status, created = Status.objects.get_or_create(tier=tier, level=level)
            cp.status = status
            cp.save()
            self.stdout.write("{}: {} {} -> {}".format(cp.name, tier, level, cp.status), ending='\n\r')

