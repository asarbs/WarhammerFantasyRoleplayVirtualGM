import django_tables2 as tables
from django_tables2.utils import A

from WarhammerFantasyRoleplayVirtualGM_app.models import *

from .character_creations_helpers import format_currency

class MeleeWeaponsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("EditMeleWeapon", args=[A('pk')])
    reference = tables.Column(visible=False)
    weapon_ptr = tables.Column(visible=False)

    class Meta:
        model = MeleeWeapons
        attrs = {"class": "paleblue"}
        sequence = ('weapon_group', 'name',  'price', 'encumbrance', 'availability', 'damage', 'qualities_and_flaws', 'reach', 'reference')
        order_by = ('weapon_group', 'name')

    def render_price(self, value):
        return f"{format_currency(value)}"

class RangedWeaponsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("EditRangedWeapon", args=[A('pk')])
    reference = tables.Column(visible=False)
    weapon_ptr = tables.Column(visible=False)

    class Meta:
        model = RangedWeapon
        attrs = {"class": "paleblue"}
        sequence = ('weapon_group', 'name',  'price', 'encumbrance', 'availability', 'damage', 'qualities_and_flaws', 'range', 'reference')
        order_by = ('weapon_group', 'name')

    def render_price(self, value):
        return f"{format_currency(value)}"

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
        return f"{format_currency(value)}"

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
        return f"{format_currency(value)}"


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

class ContainerTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn("ContainersEditView", args=[A('pk')])
    reference = tables.Column(visible=False)
    weapon_ptr = tables.Column(visible=False)

    class Meta:
        model = Containers
        attrs = {"class": "paleblue"}
        sequence = ('name', 'encumbrance',  'carries', 'price', 'availability')
        order_by = ('name', 'encumbrance',)

    def render_price(self, value):
        return f"{format_currency(value)}"