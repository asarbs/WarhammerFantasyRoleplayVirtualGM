import django_tables2 as tables
from django_tables2.utils import A

from WarhammerFantasyRoleplayVirtualGM_app.models import MeleeWeapons

from .character_creations_helpers import format_currencu

class MeleeWeaponsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("EditMeleWeapon", args=[A('pk')])
    weapon_group = tables.Column()
    price = tables.Column()
    encumbrance = tables.Column()
    availability = tables.Column()
    damage = tables.Column()
    qualities_and_flaws = tables.Column()
    reference = tables.Column(visible=False)
    weapon_ptr = tables.Column(visible=False)

    class Meta:
        model = MeleeWeapons
        attrs = {"class": "paleblue"}
        sequence = ('weapon_group', 'name',  'price', 'encumbrance', 'availability', 'damage', 'qualities_and_flaws', 'reach', 'reference')

    def render_price(self, value):
        return f"{format_currencu(value)}"

class RangedWeaponsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("EditRangedWeapon", args=[A('pk')])
    weapon_group = tables.Column()
    price = tables.Column()
    encumbrance = tables.Column()
    availability = tables.Column()
    damage = tables.Column()
    qualities_and_flaws = tables.Column()
    reference = tables.Column(visible=False)
    weapon_ptr = tables.Column(visible=False)

    class Meta:
        model = MeleeWeapons
        attrs = {"class": "paleblue"}
        sequence = ('weapon_group', 'name',  'price', 'encumbrance', 'availability', 'damage', 'qualities_and_flaws', 'reach', 'reference')

    def render_price(self, value):
        return f"{format_currencu(value)}"