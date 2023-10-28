import django_tables2 as tables
from django_tables2.utils import A

from WarhammerFantasyRoleplayVirtualGM_app.models import MeleeWeapons
from WarhammerFantasyRoleplayVirtualGM_app.models import Spells
from WarhammerFantasyRoleplayVirtualGM_app.models import Trapping
from WarhammerFantasyRoleplayVirtualGM_app.models import Talent

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

class SpellsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("SpellsEditView", args=[A('pk')])
    spellLists = tables.Column()
    cn = tables.Column()
    range = tables.Column()
    target = tables.Column()
    duration = tables.Column()
    effect = tables.Column()

    class Meta:
        model = Spells
        attrs = {"class": "paleblue"}
        sequence = ('spellLists', 'name',  'cn', 'range', 'target', 'duration', 'effect')

    def render_price(self, value):
        return f"{format_currencu(value)}"

class TrappingTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("TrappingssEditView", args=[A('pk')])
    description = tables.Column()
    encumbrance = tables.Column()

    class Meta:
        model = Trapping
        attrs = {"class": "paleblue"}
        sequence = ('name',  'description', 'encumbrance')
        order_by = ('name')
        data = Trapping.objects.all()
        per_page = 50

    def render_price(self, value):
        return f"{format_currencu(value)}"


class TalentTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("TalentsEditView", args=[A('pk')])
    description = tables.Column()
    ref = tables.Column()
    max = tables.Column()
    tests = tables.Column(visible=False)
    talent_parent = tables.Column(visible=False)

    class Meta:
        model = Talent
        attrs = {"class": "paleblue"}
        sequence = ('name',  'description','max', 'ref')
        order_by = ('name')
        data = Talent.objects.all()
        per_page = 500
