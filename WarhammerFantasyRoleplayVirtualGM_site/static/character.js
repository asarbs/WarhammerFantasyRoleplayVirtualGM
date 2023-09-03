
class Skill {
    #adv_standard        = 0;
    #adv_career          = 0;
    #adv_species         = 0;
    #characteristics     = "";
    #description         = "";
    #id                  = 0;
    #is_basic_skill      = false;
    #is_career_skill     = false;
    #is_species_skill    = false;
    #name                = "";
    constructor(id, name, characteristics, description, is_basic_skill, is_career_skill, is_species_skill, adv_standard, adv_career, adv_species ) {
        console.log("Skill \""+ name + "\" added");
        this.#id = id;
        this.#name = name;
        this.#characteristics = characteristics;
        this.#description = description;
        this.#is_basic_skill = is_basic_skill;
        this.#is_career_skill = is_career_skill;
        this.#is_species_skill = is_species_skill
        this.#adv_standard = adv_standard
        this.#adv_career = adv_career
        this.#adv_species = adv_species
    }
    get id() {
        return this.#id
    }
    get name() {
        return this.#name
    }
    get characteristics() {
        return this.#characteristics
    }
    get is_basic_skill() {
        return this.#is_basic_skill
    }
    get is_career_skill() {
        return this.#is_career_skill
    }
    get is_species_skill() {
        return this.#is_species_skill
    }
    set adv_standard(adv) {
        if(typeof adv === "number")
            this.#adv_standard = adv;
        else
            throw "" + adv + " is not a number";
    }
    set adv_career(adv) {
        if(typeof adv === "number")
            this.#adv_career = adv;
        else
            throw "" + adv + " is not a number";
    }
    set adv_species(adv) {
        if(typeof adv === "number")
            this.#adv_species = adv;
        else
            throw "" + adv + " is not a number";
    }
    get adv() {
        return this.#adv_standard + this.#adv_career + this.#adv_species;
    }
};
class Trapping {
    #id             = 0
    #name           = ""
    #enc            = 0
    #description    = "";
    constructor(id, name, enc, description) {
        this.#id = id;
        this.#name = name;
        this.#enc = enc;
        this.#description = description;
    }
    get id() {
        return this.#id;
    }
    set name(name) {
        if(typeof name === "string") {
            this.#name = name;
            $("td#trappings_name_"+this.#id).val(name);
        }
        else
            throw "" + name + " is not a string";
    }
    get name() {
        return this.#name;
    }
    set enc(enc) {
        if(typeof enc === "string") {
            this.#enc = enc;
            $("td#trappings_enc_"+this.#id).val(enc);
        }
        else
            throw "Trapping enc=" + enc + " is not a string";
    }
    get enc() {
        return this.#enc;
    }
    set description(description) {
        if(typeof enc === "string") {
            this.#description = description;
        }
        else
            throw "Trapping description=" + enc + " is not a string";
    }
    get enc() {
        return this.#description;
    }
}
class Talent {
    #id             = 0
    #name           = ""
    #max            = ""
    #test           = ""
    #description    = "";
    constructor(id, name, max, test, description) {
        this.#id = id;
        this.#name = name;
        this.#max = max;
        this.#test = test;
        this.#description = description;
    }
    get id() {
        return this.#id;
    }
    get name() {
        return this.#name;
    }
    get max() {
        return this.#max;
    }
    get test() {
        return this.#test;
    }
    get description() {
        return this.#description;
    }
}
class Armour{
    #id
    #name
    #armour_type
    #price
    #encumbrance
    #availability
    #penalty
    #locations
    #armour_points
    #qualities_and_flaws
    #is_in_inventory
    constructor(id, name, armour_type, price, encumbrance, availability, penalty, locations, armour_points, qualities_and_flaws, is_in_inventory) {
        this.#id = id;
        this.#name = name;
        this.#armour_type = armour_type;
        this.#price = price;
        this.#encumbrance = encumbrance;
        this.#availability = availability;
        this.#penalty = penalty;
        this.#locations = locations;
        this.#armour_points = armour_points;
        this.#qualities_and_flaws = qualities_and_flaws;
        this.#is_in_inventory = is_in_inventory
        console.log("Create Armour:" + this.name + "; this.#is_in_inventory:"+this.#is_in_inventory);
    }

    set name(name) {
        if(typeof name === "string")
            this.#name = name;
        else
            throw "" + name + " is not a string";
    }
    set armour_type(armour_type) {
        if(typeof armour_type === "string")
            this.#armour_type = armour_type;
        else
            throw "" + armour_type + " is not a string";
    }
    set price(price) {
        if(typeof price === "number")
            this.#price = price;
        else
            throw "" + price + " is not a number";
    }
    set encumbrance(encumbrance) {
        if(typeof encumbrance === "number")
            this.#encumbrance = encumbrance;
        else
            throw "" + encumbrance + " is not a number";
    }
    set availability(availability) {
        if(typeof availability === "string")
            this.#availability = availability;
        else
            throw "" + availability + " is not a string";
    }
    set penalty(penalty) {
        if(typeof penalty === "string")
            this.#penalty = penalty;
        else
            throw "" + penalty + " is not a string";
    }
    set locations(locations) {
        if(typeof locations === "string")
            this.#locations = locations;
        else
            throw "" + locations + " is not a string";
    }
    set armour_points(armour_points) {
        if(typeof armour_points === "number")
            this.#armour_points = armour_points;
        else
            throw "" + armour_points + " is not a number";
    }
    set qualities_and_flaws(qualities_and_flaws) {
        if(typeof qualities_and_flaws === "string") {
            this.#qualities_and_flaws = qualities_and_flaws;
            this.save()
         } else {
            throw "" + qualities_and_flaws + " is not a string";
         }
    }
    set is_in_inventory(is_in_inventory) {
        if(typeof is_in_inventory === "boolean"){
            this.#is_in_inventory = is_in_inventory;
            this.updateUI();
            this.save();
        }
        else {
            throw "" + is_in_inventory + " boolean";
        }
    }

    get id() {
        return this.#id;
    }
    get name() {
        return this.#name;
    }
    get armour_type() {
        return this.#armour_type;
    }
    get price() {
        return this.#price;
    }
    get encumbrance() {
        return this.#encumbrance;
    }
    get availability() {
        return this.#availability;
    }
    get penalty() {
        return this.#penalty;
    }
    get locations() {
        return this.#locations;
    }
    get armour_points() {
        return this.#armour_points;
    }
    get qualities_and_flaws() {
        return this.#qualities_and_flaws;
    }

    updateUI() {
        console.log("updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        if(this.#is_in_inventory && !$('td#armour_name__'+this.#id).length) {
            var new_row = '<tr class="block_body">'
            new_row += '<td id="armour_name__'+this.#id+'" class="left">'+this.#name+'</td>'
            new_row += '<td id="armour_location__'+this.#id+'" class="center">'+this.#locations+'</td>'
            new_row += '<td id="armour_encumbrance__'+this.#id+'" class="center">'+this.#encumbrance+'</td>'
            new_row += '<td id="armour_armour_points__'+this.#id+'" class="center">'+this.#armour_points+'</td>'
            new_row += '<td id="armour_qualities__'+this.#id+'" class="center">'+this.#qualities_and_flaws+'</td>'
            new_row += '</tr>'
            $("table#armour").append(new_row)
        } else {
            console.log("Armour NOT updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        }
    }

    save() {
        var characer_id = $("input[name='characer_id']").val()
        $.ajax({
            type: "POST",
            url: "ajax_addArmourToCharacter",
            data: {
                characer_id: characer_id,
                armour_id: this.id,
            },
            success: function(data) {

            }
        });

    }

}
class Weapon{
    #id
    #name
    #weapon_group
    #price
    #encumbrance
    #availability
    #damage
    #qualities_and_flaws
    #reach_range
    #is_in_inventory
    constructor(id, name, weapon_group, price, encumbrance, availability, damage, qualities_and_flaws, reach_range, is_in_inventory) {
        this.#id = id
        this.#name = name
        this.#weapon_group = weapon_group
        this.#price = price
        this.#encumbrance = encumbrance
        this.#availability =  availability
        this.#damage = damage
        this.#qualities_and_flaws = qualities_and_flaws
        this.#reach_range = reach_range
        this.#is_in_inventory = is_in_inventory
        console.log("Weaponr:" + this.name + "; this.#is_in_inventory:"+this.#is_in_inventory);
    }

    get id() {
        return this.#id
    }
    get name() {
        return this.#name
    }
    get weapon_group() {
        return this.#weapon_group
    }
    get price() {
        return this.#price
    }
    get encumbrance() {
        return this.#encumbrance
    }
    get availability() {
        return this.#availability
    }
    get damage() {
        return this.#damage
    }
    get qualities_and_flaws() {
        return this.#qualities_and_flaws
    }
    get reach_range() {
        return this.#reach_range
    }
    get is_in_inventory() {
        return this.#is_in_inventory
    }
    set name(name) {
        if(typeof name === "string")
            this.#name = name;
        else
            throw "" + name + " is not a string";
    }
    set weapon_group(weapon_group) {
        if(typeof weapon_group === "string")
            this.#weapon_group = weapon_group;
        else
            throw "" + weapon_group + " is not a string";
    }
    set price(price) {
        if(typeof price === "number")
            this.#price = price;
        else
            throw "" + price + " is not a number";
    }
    set encumbrance(encumbrance) {
        if(typeof encumbrance === "number")
            this.#encumbrance = encumbrance;
        else
            throw "" + encumbrance + " is not a number";
    }
    set availability(availability) {
        if(typeof availability === "string")
            this.#availability = availability;
        else
            throw "" + availability + " is not a string";
    }
    set damage(damage) {
        if(typeof damage === "number")
            this.#damage = damage;
        else
            throw "" + damage + " is not a number";
    }
    set qualities_and_flaws(qualities_and_flaws) {
        if(typeof qualities_and_flaws === "string") {
            this.#qualities_and_flaws = qualities_and_flaws;
         } else {
            throw "" + qualities_and_flaws + " is not a string";
         }
    }
    set reach_range(reach_range) {
        if(typeof reach_range === "string") {
            this.#reach_range = reach_range;
         } else {
            throw "" + reach_range + " is not a string";
         }
    }
    set is_in_inventory(is_in_inventory) {
        if(typeof is_in_inventory === "boolean"){
            this.#is_in_inventory = is_in_inventory;
            this.updateUI();
            this.save();
        }
        else {
            throw "" + is_in_inventory + " boolean";
        }
    }
    updateUI() {
        console.log("updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        if(this.#is_in_inventory && !$('td#weapon_name__'+this.#id).length) {
            var new_row = '<tr class="block_body">'
            new_row += '<td id="weapon_name__'+this.#id+'" class="left">'+this.#name+'</td>'
            new_row += '<td id="weapon_location__'+this.#id+'" class="center">'+this.#weapon_group+'</td>'
            new_row += '<td id="weapon_encumbrance__'+this.#id+'" class="center">'+this.#encumbrance+'</td>'
            new_row += '<td id="weapon_armour_points__'+this.#id+'" class="center">'+this.#reach_range+'</td>'
            new_row += '<td id="weapon_armour_points__'+this.#id+'" class="center">'+this.#damage+'</td>'
            new_row += '<td id="weapon_qualities__'+this.#id+'" class="center">'+this.#qualities_and_flaws+'</td>'
            new_row += '</tr>'
            $("table#weapons").append(new_row)
        } else {
            console.log("Weapon: NOT updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        }
    }

    save() {
        var characer_id = $("input[name='characer_id']").val()
        $.ajax({
            type: "POST",
            url: "ajax_addWeaponToCharacter",
            data: {
                characer_id: characer_id,
                weapon_id: this.id,
            },
            success: function(data) {

            }
        });

    }
}
class Spells{
    #id
    #name
    #spellLists
    #cn
    #range
    #target
    #duration
    #effect
    #is_in_inventory
    constructor(id, name, spellLists, cn, range, target, duration, effect, is_in_inventory) {
        this.#id = id
        this.#name = name
        this.#spellLists = spellLists
        this.#cn = cn
        this.#range = range
        this.#target = target
        this.#duration =  duration
        this.#effect = effect
        this.#is_in_inventory = is_in_inventory
        console.log("Spells:" + this.name + "; this.#is_in_inventory:"+this.#is_in_inventory);
    }
    get id() {
        return this.#id
    }
    get name() {
        return this.#name
    }
    get spellLists() {
        return this.#spellLists
    }
    get cn() {
        return this.#cn
    }
    get range() {
        return this.#range
    }
    get target() {
        return this.#target
    }
    get duration() {
        return this.#duration
    }
    get effect() {
        return this.#effect
    }
    get is_in_inventory() {
        return this.#is_in_inventory
    }
    set name(name) {
        if(typeof name === "string")
            this.#name = name;
        else
            throw "" + name + " is not a string";
    }
    set spellLists(spellLists) {
        if(typeof spellLists === "string")
            this.#spellLists = spellLists;
        else
            throw "" + spellLists + " is not a string";
    }
    set cn(cn) {
        return this.#cn
    }
    set range(range) {
        if(typeof range === "string")
            this.#range = range;
        else
            throw "" + range + " is not a string";
    }
    set target(target) {
        if(typeof target === "string")
            this.#target = target;
        else
            throw "" + target + " is not a string";
    }
    set duration(duration) {
        if(typeof duration === "string")
            this.#duration = duration;
        else
            throw "" + duration + " is not a string";
    }
    set effect(effect) {
        if(typeof effect === "string")
            this.#effect = effect;
        else
            throw "" + effect + " is not a string";
    }
    set is_in_inventory(is_in_inventory) {
        if(typeof is_in_inventory === "boolean"){
            this.#is_in_inventory = is_in_inventory;
            this.updateUI();
            this.save();
        }
        else {
            throw "" + is_in_inventory + " boolean";
        }
    }
    updateUI() {
        //name, cn, range, target, duration, effect
        console.log("updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        if(this.#is_in_inventory && !$('td#spell_name__'+this.#id).length) {
            var new_row = '<tr class="block_body">'
            new_row += '<td id="spell_name__'+this.#id+'" class="left">'+this.#name+'</td>'
            new_row += '<td id="spell_cn__'+this.#id+'" class="center">'+this.#cn+'</td>'
            new_row += '<td id="spell_range_'+this.#id+'" class="center">'+this.#range+'</td>'
            new_row += '<td id="spell_target__'+this.#id+'" class="center">'+this.#target+'</td>'
            new_row += '<td id="spell_duration__'+this.#id+'" class="center">'+this.#duration+'</td>'
            new_row += '<td id="spell_effect__'+this.#id+'" class="center">'+this.#effect+'</td>'
            new_row += '</tr>'
            $("table#spells").append(new_row)
        } else {
            console.log("Spell: NOT updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        }
    }

    save() {
        var characer_id = $("input[name='characer_id']").val()
        $.ajax({
            type: "POST",
            url: "ajax_addSpellsToCharacter",
            data: {
                characer_id: characer_id,
                spell_id: this.id,
            },
            success: function(data) {

            }
        });
    }
}
class AdvanceScheme {
    #characteristics_ws     = 0;
    #characteristics_bs     = 0;
    #characteristics_s      = 0;
    #characteristics_t      = 0;
    #characteristics_i      = 0;
    #characteristics_ag     = 0;
    #characteristics_dex    = 0;
    #characteristics_int    = 0;
    #characteristics_wp     = 0;
    #characteristics_fel    = 0;
    #skills                 = {1:[], 2:[], 3:[], 4:[]};
    #talents                = {1:[], 2:[], 3:[], 4:[]};
    #trappings              = {1:[], 2:[], 3:[], 4:[]};
    constructor(careersAdvanceScheme) {
        console.log(careersAdvanceScheme)
        var sign2Level = {
            'NO': 0,
            'CR': 1,
            'HA': 2,
            'SK': 3,
            'SH': 4,
        }

        this.#characteristics_ws    = sign2Level[careersAdvanceScheme['characteristics_ws_initial']];
        this.#characteristics_bs    = sign2Level[careersAdvanceScheme['characteristics_bs_initial']];
        this.#characteristics_s     = sign2Level[careersAdvanceScheme['characteristics_s_initial']];
        this.#characteristics_t     = sign2Level[careersAdvanceScheme['characteristics_t_initial']];
        this.#characteristics_i     = sign2Level[careersAdvanceScheme['characteristics_i_initial']];
        this.#characteristics_ag    = sign2Level[careersAdvanceScheme['characteristics_ag_initial']];
        this.#characteristics_dex   = sign2Level[careersAdvanceScheme['characteristics_dex_initial']];
        this.#characteristics_int   = sign2Level[careersAdvanceScheme['characteristics_int_initial']];
        this.#characteristics_wp    = sign2Level[careersAdvanceScheme['characteristics_wp_initial']];
        this.#characteristics_fel   = sign2Level[careersAdvanceScheme['characteristics_fel_initial']];

        for(let i = 1 ; i <= 4 ; i++) {
            this.#skills[i] = careersAdvanceScheme['advances_level'][i].skills
            this.#talents[i] = careersAdvanceScheme['advances_level'][i].talents
            this.#trappings[i] = careersAdvanceScheme['advances_level'][i].trappings
        }
    }

}
class CharacterParameters {
    #age                                = 0
    #avalible_attribute_points          = 100;
    #bonus_xp                           = 0;
    #career_id                        = 0;
    #career_level                       = 0;
    #career_name                        = "";
    #career_path                        = "";
    #ch_class_name                      = "";
    #character_creation_step            = 0;
    #characteristics_ag_advances        = 0;
    #characteristics_ag_initial         = 0;
    #characteristics_bs_advances        = 0;
    #characteristics_bs_initial         = 0;
    #characteristics_dex_advances       = 0;
    #characteristics_dex_initial        = 0;
    #characteristics_fel_advances       = 0;
    #characteristics_fel_initial        = 0;
    #characteristics_i_advances         = 0;
    #characteristics_i_initial          = 0;
    #characteristics_int_advances       = 0;
    #characteristics_int_initial        = 0;
    #characteristics_s_advances         = 0;
    #characteristics_s_initial          = 0;
    #characteristics_selection_random   = 0;
    #characteristics_t_advances         = 0;
    #characteristics_t_initial          = 0;
    #characteristics_wp_advances        = 0;
    #characteristics_wp_initial         = 0;
    #characteristics_ws_advances        = 0;
    #characteristics_ws_initial         = 0;
    #class_selection_random             = 0;
    #extra_points                       = 0;
    #eyes                               = ""
    #fate_fate                          = 0;
    #fate_fortune                       = 0;
    #hair                               = ""
    #height                             = 0
    #movement_movement                  = 0;
    #name                               = "";
    #needUpdate                         = false;
    #RandomAttributesTable              = [];
    #RandomEyesTable                    = [];
    #RandomHairTable                    = [];
    #resilience_resilience              = 0;
    #resilience_resolve                 = 0;
    #skills                             = {};
    #trappings                          = {};
    #species_id                         = 0;
    #status                             = "";
    #talents                            = {};
    #talentsNeedUpdate                  = false;
    #armour                            = [];
    #weapon                            = [];
    #spells                            = [];
    #wounds                             = 0;
    #skills_species                      = {};
    #advanceScheme;
    movement = {
        0: {'walk': 0,"run": 0},
        3: {'walk': 6,"run": 12},
        4: {'walk': 8,"run": 16},
        5: {'walk': 10,"run": 20},
        };

    constructor() {
        console.log("CharacterParameters::constructor");
    }
    set RandomAttributesTable(table) {
        this.#RandomAttributesTable = table;
    }
    get RandomAttributesTable() {
        return this.#RandomAttributesTable;
    }
    set RandomHairTable(table) {
        this.#RandomHairTable = table;
    }
    get RandomHairTable() {
        return this.#RandomHairTable
    }
    set RandomEyesTable(table) {
        this.#RandomEyesTable = table;
    }
    get RandomEyesTable() {
        return this.#RandomEyesTable;
    }
    set name(name) {
        if(typeof name === "string") {
            this.#name = name;
            $("input#character_sheet_name").val(characterParameters.name);
        }
        else
            throw "" + name + " is not a string";
    }
    get name() {
        return this.#name;
    }
    set hair(hair) {
        if(typeof hair === "number") {
            this.#hair = hair;
            this.#needUpdate = true;
        }
        else
            throw "hair: " + hair + " is not a number";
    }
    set eyes(eyes) {
        if(typeof eyes === "number") {
            this.#eyes = eyes;
            this.#needUpdate = true;
        }
        else
            throw "eyes: " + eyes + " is not a number";
    }
    set age(age) {
        if(typeof age === "number") {
            this.#age = age;
            $("input#age").val(characterParameters.age);
        }
        else
            throw "age:" + age + " is not a number";
    }
    get age() {
        return this.#age;
    }
    set height(height) {
        if(typeof height === "number") {
            this.#height = height;
            $("input#height").val(characterParameters.height);
        }
        else
            throw "height" + height + " is not a height";
    }
    get height() {
        return this.#height
    }
    set bonus_xp(bonus_xp) {
        if(typeof bonus_xp === "number") {
            this.#bonus_xp = bonus_xp;
            $("input#experience_current").val(characterParameters.bonus_xp);
        }
        else
            throw "bonus_xp[" + bonus_xp + "] is not a string";
    }
    get bonus_xp() {
        return this.#bonus_xp;
    }
    set characteristics_ws_initial(characteristics_ws_initial) {
        if(typeof characteristics_ws_initial === "number") {
            this.#characteristics_ws_initial = characteristics_ws_initial;
            $("input#characteristics_ws_initial"  ).val(characterParameters.characteristics_ws_initial)
            $("input#characteristics_ws_current"  ).val(characterParameters.characteristics_ws_current)
        }
        else
            throw "characteristics_ws_initial[" + characteristics_ws_initial + "] is not a string";
    }
    get characteristics_ws_initial() {
        return this.#characteristics_ws_initial;
    }
    set characteristics_bs_initial(characteristics_bs_initial) {
        if(typeof characteristics_bs_initial === "number") {
            this.#characteristics_bs_initial = characteristics_bs_initial;
            $("input#characteristics_bs_initial"  ).val(characterParameters.characteristics_bs_initial)
            $("input#characteristics_bs_current"  ).val(characterParameters.characteristics_bs_current)
        }
        else
            throw "characteristics_bs_initial[" + characteristics_bs_initial + "] is not a string";
    }
    get characteristics_bs_initial() {
        return this.#characteristics_bs_initial;
    }
    set characteristics_s_initial(characteristics_s_initial) {
        if(typeof characteristics_s_initial === "number") {
            this.#characteristics_s_initial = characteristics_s_initial;
            $("input#characteristics_s_initial"   ).val(characterParameters.characteristics_s_initial)
            $("input#characteristics_s_current"   ).val(characterParameters.characteristics_s_current)
            $("input#strength_bonus"              ).val(characterParameters.s_bonus)
            this.updateWounds();
        }
        else
            throw "characteristics_s_initial[" + characteristics_s_initial + "] is not a string";
    }
    get characteristics_s_initial() {
        return this.#characteristics_s_initial;
    }
    set characteristics_t_initial(characteristics_t_initial) {
        if(typeof characteristics_t_initial === "number") {
            this.#characteristics_t_initial = characteristics_t_initial;
            $("input#characteristics_t_initial"   ).val(characterParameters.characteristics_t_initial)
            $("input#characteristics_t_current"   ).val(characterParameters.characteristics_t_current )
            $("input#toughness_bonus"              ).val(this.t_bonus + " * 2")
            this.updateWounds();
        }
        else
            throw "characteristics_t_initial[" + characteristics_t_initial + "] is not a string";
    }
    get characteristics_t_initial() {
        return this.#characteristics_t_initial;
    }
    set characteristics_i_initial(characteristics_i_initial) {
        if(typeof characteristics_i_initial === "number") {
            this.#characteristics_i_initial = characteristics_i_initial;
            $("input#characteristics_i_initial"   ).val(characterParameters.characteristics_i_initial)
            $("input#characteristics_i_current"   ).val(characterParameters.characteristics_i_current)
        }
        else
            throw "characteristics_i_initial[" + characteristics_i_initial + "] is not a string";
    }
    get characteristics_i_initial() {
        return this.#characteristics_i_initial;
    }
    set characteristics_ag_initial(characteristics_ag_initial) {
        if(typeof characteristics_ag_initial === "number") {
            this.#characteristics_ag_initial = characteristics_ag_initial;
            $("input#characteristics_ag_initial"  ).val(characterParameters.characteristics_ag_initial)
            $("input#characteristics_ag_current"  ).val(characterParameters.characteristics_ag_current)
        }
        else
            throw "characteristics_ag_initial[" + characteristics_ag_initial + "] is not a string";
    }
    get characteristics_ag_initial() {
        return this.#characteristics_ag_initial;
    }
    set characteristics_dex_initial(characteristics_dex_initial) {
        if(typeof characteristics_dex_initial === "number") {
            this.#characteristics_dex_initial = characteristics_dex_initial;
            $("input#characteristics_dex_initial" ).val(characterParameters.characteristics_dex_initial)
            $("input#characteristics_dex_current" ).val(characterParameters.characteristics_dex_current)
        }
        else
            throw "characteristics_dex_initial[" + characteristics_dex_initial + "] is not a string";
    }
    get characteristics_dex_initial() {
        return this.#characteristics_dex_initial;
    }
    set characteristics_int_initial(characteristics_int_initial) {
        if(typeof characteristics_int_initial === "number") {
            this.#characteristics_int_initial = characteristics_int_initial;
            $("input#characteristics_int_initial" ).val(characterParameters.characteristics_int_initial)
            $("input#characteristics_int_current" ).val(characterParameters.characteristics_int_current)
        }
        else
            throw "characteristics_int_initial[" + characteristics_int_initial + "] is not a string";
    }
    get characteristics_int_initial() {
        return this.#characteristics_int_initial;
    }
    set characteristics_wp_initial(characteristics_wp_initial) {
        if(typeof characteristics_wp_initial === "number") {
            this.#characteristics_wp_initial = characteristics_wp_initial;
            $("input#characteristics_wp_initial"  ).val(characterParameters.characteristics_wp_initial)
            $("input#characteristics_wp_current"  ).val(characterParameters.characteristics_wp_current)
            $("input#willpower_bonus"              ).val(this.wp_bonus)
            this.updateWounds();
        }
        else
            throw "characteristics_wp_initial[" + characteristics_wp_initial + "] is not a string";
    }
    get characteristics_wp_initial() {
        return this.#characteristics_wp_initial;
    }
    set characteristics_fel_initial(characteristics_fel_initial) {
        if(typeof characteristics_fel_initial === "number") {
            this.#characteristics_fel_initial = characteristics_fel_initial;
            $("input#characteristics_fel_initial" ).val(characterParameters.characteristics_fel_initial)
            $("input#characteristics_fel_current" ).val(characterParameters.characteristics_fel_current)
        }
        else
            throw "characteristics_fel_initial[" + characteristics_fel_initial + "] is not a string";
    }
    get characteristics_fel_initial() {
        return this.#characteristics_fel_initial;
    }
    set characteristics_ws_advances(characteristics_ws_advances) {
        if(typeof characteristics_ws_advances === "number") {
            this.#characteristics_ws_advances = characteristics_ws_advances;
            $("input#characteristics_ws_advances"  ).val(characterParameters.characteristics_ws_advances)
            $("input#characteristics_ws_current"  ).val(characterParameters.characteristics_ws_current)
        }
        else
            throw "characteristics_ws_advances[" + characteristics_ws_advances + "] is not a string";
    }
    get characteristics_ws_advances() {
        return this.#characteristics_ws_advances;
    }
    set characteristics_bs_advances(characteristics_bs_advances) {
        if(typeof characteristics_bs_advances === "number") {
            this.#characteristics_bs_advances = characteristics_bs_advances;
            $("input#characteristics_bs_advances"  ).val(characterParameters.characteristics_bs_advances);
            $("input#characteristics_bs_current"  ).val(characterParameters.characteristics_bs_current);
        }
        else
            throw "characteristics_bs_advances[" + characteristics_bs_advances + "] is not a string";
    }
    get characteristics_bs_advances() {
        return this.#characteristics_bs_advances;
    }
    set characteristics_s_advances(characteristics_s_advances) {
        if(typeof characteristics_s_advances === "number") {
            this.#characteristics_s_advances = characteristics_s_advances;
            $("input#characteristics_s_advances"   ).val(characterParameters.characteristics_s_advances)
            $("input#characteristics_s_current"   ).val(characterParameters.characteristics_s_current)
            $("input#strength_bonus"              ).val(characterParameters.s_bonus)
            this.updateWounds();
        }
        else
            throw "characteristics_s_advances[" + characteristics_s_advances + "] is not a string";
    }
    get characteristics_s_advances() {
        return this.#characteristics_s_advances;
    }
    set characteristics_t_advances(characteristics_t_advances) {
        if(typeof characteristics_t_advances === "number") {
            this.#characteristics_t_advances = characteristics_t_advances;
            $("input#characteristics_t_advances"   ).val(characterParameters.characteristics_t_advances)
            $("input#characteristics_t_current"   ).val(characterParameters.characteristics_t_current)
            $("input#toughness_bonus"              ).val(this.t_bonus + " * 2")
            this.updateWounds();
        }
        else
            throw "characteristics_t_advances[" + characteristics_t_advances + "] is not a string";
    }
    get characteristics_t_advances() {
        return this.#characteristics_t_advances;
    }
    set characteristics_i_advances(characteristics_i_advances) {
        if(typeof characteristics_i_advances === "number") {
            this.#characteristics_i_advances = characteristics_i_advances;
            $("input#characteristics_i_advances"   ).val(characterParameters.characteristics_i_advances)
            $("input#characteristics_i_current"   ).val(characterParameters.characteristics_i_current)
        }
        else
            throw "characteristics_i_advances[" + characteristics_i_advances + "] is not a string";
    }
    get characteristics_i_advances() {
        return this.#characteristics_i_advances;
    }
    set characteristics_ag_advances(characteristics_ag_advances) {
        if(typeof characteristics_ag_advances === "number") {
            this.#characteristics_ag_advances = characteristics_ag_advances;
            $("input#characteristics_ag_advances"  ).val(characterParameters.characteristics_ag_advances)
            $("input#characteristics_ag_current"  ).val(characterParameters.characteristics_ag_current)
        }
        else
            throw "characteristics_ag_advances[" + characteristics_ag_advances + "] is not a string";
    }
    get characteristics_ag_advances() {
        return this.#characteristics_ag_advances;
    }
    set characteristics_dex_advances(characteristics_dex_advances) {
        if(typeof characteristics_dex_advances === "number") {
            this.#characteristics_dex_advances = characteristics_dex_advances;
            $("input#characteristics_dex_advances" ).val(characterParameters.characteristics_dex_advances)
            $("input#characteristics_dex_current" ).val(characterParameters.characteristics_dex_current)
        }
        else
            throw "characteristics_dex_advances[" + characteristics_dex_advances + "] is not a string";
    }
    get characteristics_dex_advances() {
        return this.#characteristics_dex_advances;
    }
    set characteristics_int_advances(characteristics_int_advances) {
        if(typeof characteristics_int_advances === "number") {
            this.#characteristics_int_advances = characteristics_int_advances;
            $("input#characteristics_int_advances" ).val(characterParameters.characteristics_int_advances)
            $("input#characteristics_int_current" ).val(characterParameters.characteristics_int_current)
        }
        else
            throw "characteristics_int_advances[" + characteristics_int_advances + "] is not a string";
    }
    get characteristics_int_advances() {
        return this.#characteristics_int_advances;
    }
    set characteristics_wp_advances(characteristics_wp_advances) {
        if(typeof characteristics_wp_advances === "number") {
            this.#characteristics_wp_advances = characteristics_wp_advances;
            $("input#characteristics_wp_advances"  ).val(characterParameters.characteristics_wp_advances)
            $("input#characteristics_wp_current"  ).val(characterParameters.characteristics_wp_current)
            $("input#willpower_bonus"              ).val(this.wp_bonus)
            this.updateWounds();
        }
        else
            throw "characteristics_wp_advances[" + characteristics_wp_advances + "] is not a string";
    }
    get characteristics_wp_advances() {
        return this.#characteristics_wp_advances;
    }
    set characteristics_fel_advances(characteristics_fel_advances) {
        if(typeof characteristics_fel_advances === "number") {
            this.#characteristics_fel_advances = characteristics_fel_advances;
            $("input#characteristics_fel_advances" ).val(characterParameters.characteristics_fel_advances)
            $("input#characteristics_fel_current" ).val(characterParameters.characteristics_fel_current)
        }
        else
            throw "characteristics_fel_advances[" + characteristics_fel_advances + "] is not a string";
    }
    get characteristics_fel_advances() {
        return this.#characteristics_fel_advances;
    }
    set fate_fate(fate_fate) {
        if(typeof fate_fate === "number") {
            this.#fate_fate = fate_fate;
            $("input#fate_fate"                   ).val(characterParameters.fate_fate)
        }
        else
            throw "fate_fate[" + fate_fate + "] is not a string";
    }
    get fate_fate() {
        return this.#fate_fate;
    }
    set fate_fortune(fate_fortune) {
        if(typeof fate_fortune === "number") {
            this.#fate_fortune = fate_fortune;
            $("input#fate_fortune"                ).val(characterParameters.fate_fortune)
        }
        else
            throw "fate_fortune[" + fate_fortune + "] is not a string";
    }
    get fate_fortune() {
        return this.#fate_fortune;
    }
    set resilience_resilience(resilience_resilience) {
        if(typeof resilience_resilience === "number") {
            this.#resilience_resilience = resilience_resilience;
            $("input#resilience_resilience"       ).val(characterParameters.resilience_resilience)
        }
        else
            throw "resilience_resilience[" + resilience_resilience + "] is not a string";
    }
    get resilience_resilience() {
        return this.#resilience_resilience;
    }
    set resilience_resolve(resilience_resolve) {
        if(typeof resilience_resolve === "number") {
            this.#resilience_resolve = resilience_resolve;
            $("input#resilience_resolve"          ).val(characterParameters.resilience_resolve)
        }
        else
            throw "resilience_resolve[" + resilience_resolve + "] is not a string";
    }
    get resilience_resolve() {
        return this.#resilience_resolve;
    }
    set movement_movement(movement_movement) {
        if(typeof movement_movement === "number") {
            this.#movement_movement = movement_movement;
            $("input#movement_movement"           ).val(characterParameters.movement_movement)
            $("input#movement_walk"               ).val(characterParameters.movement[characterParameters.movement_movement]['walk'])
            $("input#movement_run"                ).val(characterParameters.movement[characterParameters.movement_movement]['run'])
        }
        else
            throw "movement_movement[" + movement_movement + "] is not a string";
    }
    get movement_movement() {
        return this.#movement_movement;
    }
    set wounds(wounds) {
        if(typeof wounds === "number") {
            this.#wounds = wounds;
            $("input#wounds"                      ).val(characterParameters.wounds)
        }
        else
            throw "wounds[" + wounds + "] is not a string";
    }
    get wounds() {
        return this.#wounds;
    }
    set character_creation_step(character_creation_step) {
        if(typeof character_creation_step === "number")
            this.#character_creation_step = character_creation_step;
        else
            throw "character_creation_step[" + character_creation_step + "] is not a string";
    }
    get character_creation_step() {
        return this.#character_creation_step;
    }
    set class_selection_random(class_selection_random) {
        if(typeof class_selection_random === "number")
            this.#class_selection_random = class_selection_random;
        else
            throw "class_selection_random[" + class_selection_random + "] is not a string";
    }
    get class_selection_random() {
        return this.#class_selection_random;
    }
    set characteristics_selection_random(characteristics_selection_random) {
        if(typeof characteristics_selection_random === "number")
            this.#characteristics_selection_random = characteristics_selection_random;
        else
            throw "characteristics_selection_random[" + characteristics_selection_random + "] is not a string";
    }
    get characteristics_selection_random() {
        return this.#characteristics_selection_random;
    }
    set avalible_attribute_points(avalible_attribute_points) {
        if(typeof avalible_attribute_points === "number") {
            this.#avalible_attribute_points = avalible_attribute_points;
            $("span#avalible_attribute_points"    ).text(characterParameters.avalible_attribute_points)
        }
        else
            throw "avalible_attribute_points[" + avalible_attribute_points + "] is not a string";
    }
    get avalible_attribute_points() {
        return this.#avalible_attribute_points;
    }
    set extra_points(extra_points) {
        if(typeof extra_points === "number") {
            this.#extra_points = extra_points;
            $("span#avalible_extra_points"        ).text(characterParameters.extra_points)
        }
        else
            throw "extra_points[" + extra_points + "] is not a string";
    }
    get extra_points() {
        return this.#extra_points;
    }
    set needUpdate(needUpdate) {
        if(typeof needUpdate === "boolean")
            this.#needUpdate = needUpdate;
        else
            throw "needUpdate[" + needUpdate + "] is not a boolean";
    }
    get needUpdate() {
        return this.#needUpdate
    }
    set species_id(species_id) {
        if(typeof species_id === "number") {
            this.#species_id = species_id;
            $("select#species").val(this.#species_id);
        }
        else
            throw "species_id[" + species_id + "] is not a number";
    }
    get species_id() {
        return this.#species_id
    }
    set career_id(career_id) {
        if(typeof career_id === "number") {
            this.#career_id = career_id;
        }
        else
            throw "career_id[" + career_id + "] is not a number";
    }
    get career_id() {
        return this.#career_id
    }
    set career_name(career_name) {
        if(typeof career_name === "string") {
            this.#career_name = career_name;
            $("input#career").val(this.#career_name);
        }
        else
            throw "career_name[" + career_name + "] is not a String";
    }
    get career_name() {
        return this.#career_name
    }
    set ch_class_name(ch_class_name) {
        if(typeof ch_class_name === "string") {
            this.#ch_class_name = ch_class_name;
            $("input#class").val(this.#ch_class_name);
        }
        else
            throw "ch_class_name[" + ch_class_name + "] is not a String";
    }
    get ch_class_name() {
        return this.#ch_class_name
    }
    set career_path(career_path) {
        if(typeof career_path === "string") {
            this.#career_path = career_path;
            $("input#career_path").val(this.#career_path);
        }
        else
            throw "career_path[" + career_path + "] is not a String";
    }
    get career_path() {
        return this.#career_path;
    }
    set status(status) {
        if(typeof status === "string") {
            this.#status = status;
            $("input#status").val(this.#status);
        }
        else
            throw "status[" + status + "] is not a String";
    }
    get status() {
        return this.#status;
    }
    set career_level(career_level) {
        if(typeof career_level === "number") {
            this.#career_level = career_level;
            $("input#career_level").val(this.#career_level);
        }
        else
            throw "career_level[" + career_level + "] is not a number";
    }
    get career_level() {
        return career_level;
    }
    get characteristics_ws_current() {
        return this.#characteristics_ws_initial + this.#characteristics_ws_advances
    }
    get characteristics_bs_current() {
        return this.#characteristics_bs_initial + this.#characteristics_bs_advances
    }
    get characteristics_s_current() {
        return this.#characteristics_s_initial + this.#characteristics_s_advances
    }
    get characteristics_t_current() {
        return this.#characteristics_t_initial + this.#characteristics_t_advances
    }
    get characteristics_i_current() {
        return this.#characteristics_i_initial + this.#characteristics_i_advances
    }
    get characteristics_ag_current() {
        return this.#characteristics_ag_initial + this.#characteristics_ag_advances
    }
    get characteristics_dex_current() {
        return this.#characteristics_dex_initial + this.#characteristics_dex_advances
    }
    get characteristics_int_current() {
        return this.#characteristics_int_initial + this.#characteristics_int_advances
    }
    get characteristics_wp_current() {
        return this.#characteristics_wp_initial + this.#characteristics_wp_advances
    }
    get characteristics_fel_current() {
        return this.#characteristics_fel_initial + this.#characteristics_fel_advances
    }
    get ws_bonus() {
        return Math.floor(this.characteristics_ws_current /  10)
    }
    get bs_bonus() {
        return Math.floor(this.characteristics_bs_current /  10)
    }
    get s_bonus() {
        return Math.floor(this.characteristics_s_current /  10)
    }
    get t_bonus() {
        return Math.floor(this.characteristics_t_current /  10)
    }
    get i_bonus() {
        return Math.floor(this.characteristics_i_current /  10)
    }
    get ag_bonus() {
        return Math.floor(this.characteristics_ag_current /  10)
    }
    get dex_bonus() {
        return Math.floor(this.characteristics_dex_current /  10)
    }
    get int_bonus() {
        return Math.floor(this.characteristics_int_current /  10)
    }
    get wp_bonus() {
        return Math.floor(this.characteristics_wp_current /  10)
    }
    get fel_bonus() {
        return Math.floor(this.characteristics_fel_current /  10)
    }
    getCharacteristicsCurrent(name) {
        if(name === "WS")
            return this.characteristics_ws_current
        else if (name === "BS")
            return this.characteristics_bs_current
        else if (name === "S")
            return this.characteristics_s_current
        else if (name === "T")
            return this.characteristics_t_current
        else if (name === "I")
            return this.characteristics_i_current
        else if (name === "Ag")
            return this.characteristics_ag_current
        else if (name === "Dex")
            return this.characteristics_dex_current
        else if (name === "Int")
            return this.characteristics_int_current
        else if (name === "WP")
            return this.characteristics_wp_current
        else if (name === "Fel")
            return this.characteristics_fel_current
        else
            throw "\"" + name + "\" is invalid parameter";
    }
    updateStaticCharacterSheet() {
        if(!this.#needUpdate) {
            return
        }
        $("select#hair").empty()
        $("select#eyes").empty()
        $.each(this.#RandomHairTable[this.#species_id], function(i, item) {
            $("select#hair").append($('<option>', {value: item.val, text: item.name}))
        });
        $.each(this.#RandomEyesTable[this.#species_id], function(i, item) {
            $("select#eyes").append($('<option>', {value: item.val, text: item.name}))
        });
        this.#needUpdate = false;
    }
    updateSkillTable() {
        $.each(this.#skills, function(i, item) {
            var new_row = ""
            if(!$('#skills_adv__'+item.id).length && !$('#skills_characteristics__'+item.id).length) {
                new_row = '<tr class="block_body">'
                new_row += '<td id="skills_name__'+item.id+'" class="left">'+item.name+'</td>'
                new_row += '<td class="characteristics">'+item.characteristics+'</td>'
                new_row += '<td class="edit"><input type="text" id="skills_characteristics__'+item.id+'" name="fname"></td>'
                new_row += '<td class="edit"><input type="text" id="skills_adv__'+item.id+'" name="fname"></td>'
                new_row += '<td class="edit"><input type="text" id="skills__'+item.id+'" name="fname"></td>'
                new_row += '<td class=""><img id="skills__is_basic_skill__'+item.id+'" src="/static/NO.png"></td>'
                new_row += '<td class=""><img id="skills__is_career_skill__'+item.id+'" src="/static/NO.png"></td>'
                new_row += '<td class=""><img id="skills__is_species_skill__'+item.id+'" src="/static/NO.png"></td>'
                new_row += '</tr>'
                $("#skills_table").append(new_row)
            }

            $('#skills_characteristics__'+item.id).val(characterParameters.getCharacteristicsCurrent(item.characteristics))
            $('#skills_adv__'+item.id).val(item.adv)
            $('#skills__'+item.id).val(characterParameters.getCharacteristicsCurrent(item.characteristics) + item.adv)
            if(item.is_basic_skill == true) {
                $('img#skills__is_basic_skill__'+item.id).attr("src", "/static/img/tick.png")
            } else {
                $('img#skills__is_basic_skill__'+item.id).attr("src", "/static/NO.png")
            }
            if(item.is_career_skill == true) {
                $('img#skills__is_career_skill__'+item.id).attr("src", "/static/img/tick.png")
            } else {
                $('img#skills__is_career_skill__'+item.id).attr("src", "/static/NO.png")
            }
            if(item.is_species_skill == true) {
                $('img#skills__is_species_skill__'+item.id).attr("src", "/static/img/tick.png")
            } else {
                $('img#skills__is_species_skill__'+item.id).attr("src", "/static/NO.png")
            }

        });
    }
    updateTalentsTable() {
        if(!this.talentsNeedUpdate) {
            return;
        }
        console.log("updateTalentsTable");
        this.talentsNeedUpdate = false;
        $("table#talents_table tr.block_body").remove();
        $.each(this.#talents, function(i, item) {
            var new_row = ""
            if(!$('#talents_adv__'+item.id).length) {
                new_row = '<tr class="block_body">'
                new_row += '<td id="talents_name__'+item.id+'" class="left">'+item.name+'</td>'
                new_row += '<td class="edit"><input type="text" id="talents_adv__'+item.id+'" name="fname"></td>'
                new_row += '<td class="description">'+item.description+'</td>'
                new_row += '</tr>'
                $("#talents_table").append(new_row)
            }
        });
    }
    updateTrappingsTable() {
        if(!this.trappingsNeedUpdate) {
            return;
        }
        console.log("updateTrappingsTable");
        this.trappingsNeedUpdate = false;
        $("table#trappings_table tr.block_body").remove();
        $.each(this.#trappings, function(i, item) {
            console.log("updateTrappingsTable: "+item.id);
            var new_row = ""
            if(!$('#trappings_enc__'+item.id).length) {
                new_row = '<tr class="block_body">'
                new_row += '<td id="trappings_name__'+item.id+'" class="left">'+item.name+'</td>'
                new_row += '<td class="edit"><input type="text" id="trappings_enc__'+item.id+'" name="fname" value="'+item.enc+'"></td>'
                new_row += '</tr>'
                $("#trappings_table").append(new_row)
            }
        });
    }
    updateCharacterState() {
        this.updateStaticCharacterSheet();
        this.updateSkillTable()
        this.updateTalentsTable()
        this.updateTrappingsTable()
    }
    appendSkill(skill_params) {
        this.#skills[skill_params['id']] = new Skill(skill_params['id'],
                                                    skill_params['name'],
                                                    skill_params['characteristics'],
                                                    skill_params['description'],
                                                    skill_params['is_basic_skill'],
                                                    skill_params['is_career_skill'],
                                                    skill_params['is_species_skill'],
                                                    skill_params['adv'],
                                                    skill_params['adv'],
                                                    skill_params['adv']);
    }
    get skills() {
        return this.#skills;
    }
    getSkill(id) {
        console.log("get_skill("+id+")");
        return this.#skills[id];
    }
    deleteSkills() {
        console.log("deleteSkills");
        this.#skills = {};
    }
    appendTrappings(trapping) {
        console.log("appendTrappings:"+ trapping['id']+"; "+trapping['name']+"; "+trapping['description']+"; "+trapping['enc']);
        this.#trappings[trapping['id']] = new Trapping(trapping['id'],
                                                    trapping['name'],
                                                    trapping['description'],
                                                    trapping['enc']);
        this.trappingsNeedUpdate = true;
    }
    deleteTrappings() {
        console.log("deleteTrappings");
        this.#trappings = {};
    }
    appendTalent(talent_params) {
        this.#talents = {};
        this.#talents[talent_params['id']] = new Talent(talent_params['id'],
        talent_params['name'],
        talent_params['max'],
        talent_params['test'],
        talent_params['characteristics']);
        this.talentsNeedUpdate = true;
    }
    appendArmour(armour) {

        var a = new Armour(armour.id,
            armour.name,
            armour.armour_type,
            armour.price,
            armour.encumbrance,
            armour.availability,
            armour.penalty,
            armour.locations,
            armour.armour_points,
            armour.qualities_and_flaws,
            false);
        this.#armour.push(a)
        a.updateUI();
        $("select#add_armour").append($('<option>', {value: armour.id, text: armour.name}));
    }
    armour_add(armour_to_add) {
        console.log("characeter armour_add: "+ armour_to_add);
        $.each(this.#armour, function(i, item) {
            if(item.id == armour_to_add) {
                console.log("characeter armour_add: "+ armour_add);
                item.is_in_inventory = true;
            }
        });
    }
    appendWeapon(weapon) {
        var a = new Weapon(weapon.id,
            weapon.name,
            weapon.weapon_group,
            weapon.price,
            weapon.encumbrance,
            weapon.availability,
            weapon.damage,
            weapon.qualities_and_flaws,
            weapon.reach_range,
            false);
        this.#weapon.push(a)
        a.updateUI();
        $("select#add_weapon").append($('<option>', {value: weapon.id, text: weapon.name}));
    }
    add_weapon(weapon_to_add) {
        console.log("characeter weapon_add: "+ weapon_to_add);
        $.each(this.#weapon, function(i, item) {
            if(item.id == weapon_to_add) {
                console.log("characeter weapon_to_add: "+ weapon_to_add);
                item.is_in_inventory = true;
            }
        });
    }
    appendSpells(spell) {
        var a = new Spells(
            spell.id,
            spell.name,
            spell.spellLists,
            spell.cn,
            spell.range,
            spell.target,
            spell.duration,
            spell.effect,
            false);
        this.#spells.push(a)
        a.updateUI();
        $("select#add_spell").append($('<option>', {value: spell.id, text: spell.name}));
    }

    add_spell(spell_to_add) {
        console.log("characeter spell: "+ spell_to_add);
        $.each(this.#spells, function(i, item) {
            if(item.id == spell_to_add) {
                console.log("characeter spell_to_add: "+ spell_to_add);
                item.is_in_inventory = true;
            }
        });
    }
    add_careersAdvanceScheme(careersAdvanceScheme) {
        this.#advanceScheme = new AdvanceScheme(careersAdvanceScheme);
    }
    updateWounds() {
        $("input#wounds"              ).val(this.s_bonus + 2 * this.t_bonus + this.wp_bonus);
    }
};

const characterParameters = new CharacterParameters();
const character_creation_steps = ["step_1_species", "step_2_class", "step_3_characteristics", 'step_4_species_skills', 'step_5_career_skills', 'step_6_spendXP']
const character_creation_steps_header = ["Species", "Class", "Characteristics", "Species Skills", "Career Skills", "Spend XP"]

function selectSpecies() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    val = $(this).find(":selected").val()
    characer_id = $("input[name='characer_id']").val()

    $.ajax({
        type: "POST",
        url: "ajax_save_character_species",
        data: {
            characer_id: characer_id,
            species_id: val
        },
        success: function(data) {
            console.log(data);
            characterParameters.needUpdate = true;

            characterParameters.bonus_xp    = 0;
            characterParameters.species_id  = data['species_id'];
            characterParameters.name        = data['name'];
            characterParameters.age         = data['age']
            characterParameters.height      = data['height']
            characterParameters.hair        = data['hair']
            characterParameters.eyes        = data['eyes']
            $.each(data['species_skills'], function(i, item) {
                characterParameters.appendSkill(item);
            });

            selectSpeciesTalent(data['species_tallents']);
        }
    });
}
function selectSpeciesTalent(talens) {

    $.each(talens, function(i, item) {
        radio = '<input type="radio" id="SpeciesTalent_'+item['id']+'" name="SpeciesTalent" value="'+item['id']+'"><label for="SpeciesTalent_'+item['id']+'">'+item['name']+'</label><br>';
        $("div#step_1_species_talent_selection").append(radio)
        }
    );
    var oldValue = 0
    $('input[name="SpeciesTalent"][type="radio"]')
    .mouseup(function(){
        oldValue = $('input[name="SpeciesTalent"][type="radio"]:checked').val();
        if( oldValue === undefined)
            oldValue = '0'
    }).change(function() {
        newValue = $(this).val();
        console.log({
            characer_id: characer_id,
            new_talent_id: newValue,
            old_talent_id: oldValue
        })
        $.ajax({
            type: "POST",
            url: "ajax_replaceTalentToCharacter",
            data: {
                characer_id: characer_id,
                new_talent_id: newValue,
                old_talent_id: oldValue
            },
            success: function(data) {
                $.each(data['talents'], function(i, item) {
                    characterParameters.appendTalent(item);
                });
            }
        });

    });
}
function randomSpecies() {
    console.log("randomSpecies");
    characer_id = $("input[name='characer_id']").val()

    $.ajax({
        type: "POST",
        url: "ajax_randomSpecies",
        data: {
            characer_id: characer_id,

        },
        success: function(data) {
            console.log(data);
            characterParameters.needUpdate = true;

            characterParameters.bonus_xp    = 20;
            characterParameters.species_id  = data['species_id'];
            characterParameters.name        = data['name'];
            characterParameters.age         = data['age']
            characterParameters.height      = data['height']
            characterParameters.hair        = data['hair']
            characterParameters.eyes        = data['eyes']
            $.each(data['species_skills'], function(i, item) {
                characterParameters.appendSkill(item);
            });

            selectSpeciesTalent(data['species_tallents']);
        }
    });
}
function nextStep() {
    console.log("div#"+ character_creation_steps[characterParameters.character_creation_step]);
    $("div#"+ character_creation_steps[characterParameters.character_creation_step]).hide(200);
    characterParameters.character_creation_step++
    $("div#"+ character_creation_steps[characterParameters.character_creation_step]).show(200);
    $("div.create_character div.header h1").text(character_creation_steps_header[characterParameters.character_creation_step])
    if(characterParameters.character_creation_step == 3) {
        fill_species_skills_select();
    }
    if(characterParameters.character_creation_step == 4) {
        fill_career_skills_select();
    }
    if(characterParameters.character_creation_step == 5) {
        console.log("ajax_getCareersAdvanceScheme")
        var characer_id = $("input[name='characer_id']").val()
        $.ajax({
            type: "POST",
            url: "ajax_getCareersAdvanceScheme",
            data: {
                characer_id: characer_id,
                career_id: characterParameters.career_id,
            },
            success: function(data) {
                characterParameters.add_careersAdvanceScheme(data['careersAdvanceScheme'])
            }
        });

        $("div.create_character").animate({width: '+=1200', left: '+=300', top: '50' }, 1000, function () {

        });
    }
}
function fill_species_skills_select() {
    console.log("fill_species_skills_select: characterParameters.character_creation_step="+ characterParameters.character_creation_step);
    console.log(characterParameters.skills);
    $("select#species_skills_5_1 option").remove()
    $("select#species_skills_5_2 option").remove()
    $("select#species_skills_5_3 option").remove()
    $("select#species_skills_3_1 option").remove()
    $("select#species_skills_3_2 option").remove()
    $("select#species_skills_3_3 option").remove()

    $("select#species_skills_5_1").append($('<option>', { value: "-", text: "-" }));
    $("select#species_skills_5_2").append($('<option>', { value: "-", text: "-" }));
    $("select#species_skills_5_3").append($('<option>', { value: "-", text: "-" }));
    $("select#species_skills_3_1").append($('<option>', { value: "-", text: "-" }));
    $("select#species_skills_3_2").append($('<option>', { value: "-", text: "-" }));
    $("select#species_skills_3_3").append($('<option>', { value: "-", text: "-" }));

    $.each(characterParameters.skills, function (i, item) {
        console.log(item.name+":"+item.is_species_skill);
        if (characterParameters.character_creation_step == 3 && item.is_species_skill == true) {
            $("select#species_skills_5_1").append($('<option>', { value: item.id, text: item.name }));
            $("select#species_skills_5_2").append($('<option>', { value: item.id, text: item.name }));
            $("select#species_skills_5_3").append($('<option>', { value: item.id, text: item.name }));
            $("select#species_skills_3_1").append($('<option>', { value: item.id, text: item.name }));
            $("select#species_skills_3_2").append($('<option>', { value: item.id, text: item.name }));
            $("select#species_skills_3_3").append($('<option>', { value: item.id, text: item.name }));
        }
    });
}
function fill_career_skills_select() {
    $.each(characterParameters.skills, function(i, item) {
        if(item.is_career_skill == true) {
            $("#step_5_career_skills").append('<label for="career_skills_slider__'+item.id+'">'+item.name+'</label><input type="range" min="0" max="40" value="0" class="career_skills_slider" id="career_skills_slider__'+item.id+'" skill_id="'+item.id+'"><br>');
        }
    });

    $("input.career_skills_slider").on("change", function() {
        item_val = parseInt($(this).val());
        item_id = $(this).attr("skill_id");

        var sum = 0;
        $(".career_skills_slider").each( function(index) {
            sum += parseInt($(this).val());
        });

        console.log(typeof sum)
        var over_40 = 0
        if(sum > 40) {
            over_40 = sum - 40
            console.log("career_skills to big:"+ over_40.toString() );
            $("#step_5_career_skills_error").fadeIn("slow")
        }
        setTimeout(function(){ $("#step_5_career_skills_error").fadeOut() }, 5000);
        $(this).val(item_val - over_40);
        $("#step_5_career_skills_sum").text(sum-over_40);
        characterParameters.getSkill(item_id).adv_career = item_val

    });
}
function randomClass() {
    if(characterParameters.class_selection_random == 0) {
        characterParameters.bonus_xp += 50
        characterParameters.class_selection_random++
    }
    else if(characterParameters.class_selection_random == 1) {
        characterParameters.bonus_xp -= 50
        characterParameters.bonus_xp += 25
        characterParameters.class_selection_random++
    }
    else if(characterParameters.class_selection_random == 2) {
        characterParameters.bonus_xp -= 25
        characterParameters.bonus_xp += 0
        characterParameters.class_selection_random = 3
    }

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_randomClass",
        data: {
            characer_id: characer_id,
        },
        success: function(data) {
            characterParameters.career_id     = data['career_id'];
            characterParameters.career_name     = data['career_name'];
            characterParameters.ch_class_name   = data['ch_class_name'];
            characterParameters.career_path     = data['career_path'];
            characterParameters.status          = data['status'];
            characterParameters.career_level    = data['career_level'];
            characterParameters.deleteSkills()
            $.each(data['skills'], function(i, item) {
                characterParameters.appendSkill(item);
            })
            characterParameters.deleteTrappings()
            $.each(data['trappings'], function(i, item) {
                characterParameters.appendTrappings(item);
            })
        }
    });
}
function saveName(e) {

    n = $("input#character_sheet_name").val();
    console.log("saveName="+n);
    characterParameters.name = n
    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveName",
        data: {
            characer_id: characer_id,
            name: n,
        },
        success: function(data) {
        }
    });
}
function saveAge(e) {
    n = parseInt($("input#age").val());

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveAge",
        data: {
            characer_id: characer_id,
            age: n,
        },
        success: function(data) {
        }
    });
}
function saveHeight(e) {
    n = parseInt($("input#height").val());

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveHeight",
        data: {
            characer_id: characer_id,
            height: n,
        },
        success: function(data) {
        }
    });
}
function saveHair(e) {
    n = $('select#hair').find(":selected").val()

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveHair",
        data: {
            characer_id: characer_id,
            hair: n,
        },
        success: function(data) {
        }
    });
}
function saveEyes(e) {
    n = $('select#eyes').find(":selected").val()

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveEyes",
        data: {
            characer_id: characer_id,
            eyes: n,
        },
        success: function(data) {
        }
    });
}
function randomAttributes() {
    console.log("randomAttributes")

    if(characterParameters.characteristics_selection_random == 0) {
        characterParameters.bonus_xp += 50
        characterParameters.characteristics_selection_random++
    }
    else if(characterParameters.characteristics_selection_random == 1) {
        characterParameters.bonus_xp -= 50
        characterParameters.bonus_xp += 25
        characterParameters.characteristics_selection_random++
    }
    else if(characterParameters.characteristics_selection_random == 2) {
        characterParameters.bonus_xp -= 25
        characterParameters.bonus_xp += 0
        characterParameters.characteristics_selection_random = 3
    }

    if(characterParameters.characteristics_selection_random == 4) {

        characterParameters.characteristics_ws_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_ws_initial'   ];
        characterParameters.characteristics_bs_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_bs_initial'   ];
        characterParameters.characteristics_s_initial           = 4 + characterParameters.RandomAttributesTable[species]['characteristics_s_initial'    ];
        characterParameters.characteristics_t_initial           = 4 + characterParameters.RandomAttributesTable[species]['characteristics_t_initial'    ];
        characterParameters.characteristics_i_initial           = 4 + characterParameters.RandomAttributesTable[species]['characteristics_i_initial'    ];
        characterParameters.characteristics_ag_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_ag_initial'   ];
        characterParameters.characteristics_dex_initial         = 4 + characterParameters.RandomAttributesTable[species]['characteristics_dex_initial'  ];
        characterParameters.characteristics_int_initial         = 4 + characterParameters.RandomAttributesTable[species]['characteristics_int_initial'  ];
        characterParameters.characteristics_wp_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_wp_initial'   ];
        characterParameters.characteristics_fel_initial         = 4 + characterParameters.RandomAttributesTable[species]['characteristics_fel_initial'  ];

        $('input#characteristics_ws_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_ws_initial'   ]);
        $('input#characteristics_bs_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_bs_initial'   ]);
        $('input#characteristics_s_initial'    ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_s_initial'    ]);
        $('input#characteristics_t_initial'    ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_t_initial'    ]);
        $('input#characteristics_i_initial'    ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_i_initial'    ]);
        $('input#characteristics_ag_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_ag_initial'   ]);
        $('input#characteristics_dex_initial'  ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_dex_initial'  ]);
        $('input#characteristics_int_initial'  ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_int_initial'  ]);
        $('input#characteristics_wp_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_wp_initial'   ]);
        $('input#characteristics_fel_initial'  ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_fel_initial'  ]);
        $('input#characteristics_ws_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_ws_initial'   ]);
        $('input#characteristics_bs_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_bs_initial'   ]);
        $('input#characteristics_s_initial'    ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_s_initial'    ]);
        $('input#characteristics_t_initial'    ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_t_initial'    ]);
        $('input#characteristics_i_initial'    ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_i_initial'    ]);
        $('input#characteristics_ag_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_ag_initial'   ]);
        $('input#characteristics_dex_initial'  ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_dex_initial'  ]);
        $('input#characteristics_int_initial'  ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_int_initial'  ]);
        $('input#characteristics_wp_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_wp_initial'   ]);
        $('input#characteristics_fel_initial'  ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_fel_initial'  ]);

        characterParameters.avalible_attribute_points =  characterParameters.avalible_attribute_points - 40;
        return;
    }

    if(characterParameters.characteristics_selection_random == 3) {
        var quantity = jQuery('.quantity input').each( function() {
            jQuery('<div class="quantity-nav"><button class="quantity-button quantity-up" onClick="btnUp(\''+this.id+'\')">&#xf106;</button><button class="quantity-button quantity-down" onClick="btnDown(\''+this.id+'\')">&#xf107</button></div>').insertAfter(this)
          });
          characterParameters.characteristics_selection_random = 4
        species = $("select#species").val()
        console.log(species);
        characterParameters.characteristics_ws_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_ws_initial'   ];
        characterParameters.characteristics_bs_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_bs_initial'   ];
        characterParameters.characteristics_s_initial           = 4 + characterParameters.RandomAttributesTable[species]['characteristics_s_initial'    ];
        characterParameters.characteristics_t_initial           = 4 + characterParameters.RandomAttributesTable[species]['characteristics_t_initial'    ];
        characterParameters.characteristics_i_initial           = 4 + characterParameters.RandomAttributesTable[species]['characteristics_i_initial'    ];
        characterParameters.characteristics_ag_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_ag_initial'   ];
        characterParameters.characteristics_dex_initial         = 4 + characterParameters.RandomAttributesTable[species]['characteristics_dex_initial'  ];
        characterParameters.characteristics_int_initial         = 4 + characterParameters.RandomAttributesTable[species]['characteristics_int_initial'  ];
        characterParameters.characteristics_wp_initial          = 4 + characterParameters.RandomAttributesTable[species]['characteristics_wp_initial'   ];
        characterParameters.characteristics_fel_initial         = 4 + characterParameters.RandomAttributesTable[species]['characteristics_fel_initial'  ];

        $('input#characteristics_ws_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_ws_initial'   ]);
        $('input#characteristics_bs_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_bs_initial'   ]);
        $('input#characteristics_s_initial'    ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_s_initial'    ]);
        $('input#characteristics_t_initial'    ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_t_initial'    ]);
        $('input#characteristics_i_initial'    ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_i_initial'    ]);
        $('input#characteristics_ag_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_ag_initial'   ]);
        $('input#characteristics_dex_initial'  ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_dex_initial'  ]);
        $('input#characteristics_int_initial'  ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_int_initial'  ]);
        $('input#characteristics_wp_initial'   ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_wp_initial'   ]);
        $('input#characteristics_fel_initial'  ).attr('min',  4 + characterParameters.RandomAttributesTable[species]['characteristics_fel_initial'  ]);
        $('input#characteristics_ws_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_ws_initial'   ]);
        $('input#characteristics_bs_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_bs_initial'   ]);
        $('input#characteristics_s_initial'    ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_s_initial'    ]);
        $('input#characteristics_t_initial'    ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_t_initial'    ]);
        $('input#characteristics_i_initial'    ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_i_initial'    ]);
        $('input#characteristics_ag_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_ag_initial'   ]);
        $('input#characteristics_dex_initial'  ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_dex_initial'  ]);
        $('input#characteristics_int_initial'  ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_int_initial'  ]);
        $('input#characteristics_wp_initial'   ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_wp_initial'   ]);
        $('input#characteristics_fel_initial'  ).attr('max', 18 + characterParameters.RandomAttributesTable[species]['characteristics_fel_initial'  ]);

        characterParameters.avalible_attribute_points =  characterParameters.avalible_attribute_points - 40;

        return;
    }

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveAttributes",
        data: {
            characer_id: characer_id,
        },
        success: function(data) {
            characterParameters.characteristics_ws_initial  = data['characteristics_ws_initial'];
            characterParameters.characteristics_bs_initial  = data['characteristics_bs_initial'];
            characterParameters.characteristics_s_initial   = data['characteristics_s_initial'];
            characterParameters.characteristics_t_initial   = data['characteristics_t_initial'];
            characterParameters.characteristics_i_initial   = data['characteristics_i_initial'];
            characterParameters.characteristics_ag_initial  = data['characteristics_ag_initial'];
            characterParameters.characteristics_dex_initial = data['characteristics_dex_initial'];
            characterParameters.characteristics_int_initial = data['characteristics_int_initial'];
            characterParameters.characteristics_wp_initial  = data['characteristics_wp_initial'];
            characterParameters.characteristics_fel_initial = data['characteristics_fel_initial'];
            characterParameters.fate_fate                   = data['fate_fate'];
            characterParameters.fate_fortune                = data['fate_fortune'];
            characterParameters.resilience_resilience       = data['resilience_resilience'];
            characterParameters.resilience_resolve          = data['resilience_resolve'];
            characterParameters.movement_movement           = data['movement_movement'];
            characterParameters.wounds                      = data['wounds'];
            characterParameters.extra_points                = data['extra_points'];
        }
    });
}
function btnUp(input_id) {
    if(characterParameters.avalible_attribute_points <= 0) {
        return
    }

    inp = $('input#'+input_id);
    max = parseInt(inp.attr('max'));
    min = parseInt(inp.attr('min'));
    step = parseInt(inp.attr('step'));
    oldValue = parseInt(inp.val());



    if ((oldValue + step) > max) {
        return
    } else {
      var newVal = oldValue + step;
    }

    console.log("btnUp: input_id="+input_id+"; min="+min + "; max="+max+"; step="+step+"; oldVal="+oldValue+"; newVal="+newVal);
    characterParameters.input_id  = newVal
    inp.val(newVal);
    inp.trigger("change");

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveAttribute",
        data: {
            characer_id: characer_id,
            input_id: input_id,
            'newVal': {
                'characteristics_ws_initial'    : $('input#characteristics_ws_initial'  ).val(),
                'characteristics_bs_initial'    : $('input#characteristics_bs_initial'  ).val(),
                'characteristics_s_initial'     : $('input#characteristics_s_initial'   ).val(),
                'characteristics_t_initial'     : $('input#characteristics_t_initial'   ).val(),
                'characteristics_i_initial'     : $('input#characteristics_i_initial'   ).val(),
                'characteristics_ag_initial'    : $('input#characteristics_ag_initial'  ).val(),
                'characteristics_dex_initial'   : $('input#characteristics_dex_initial' ).val(),
                'characteristics_int_initial'   : $('input#characteristics_int_initial' ).val(),
                'characteristics_wp_initial'    : $('input#characteristics_wp_initial'  ).val(),
                'characteristics_fel_initial'   : $('input#characteristics_fel_initial' ).val()
            }
        },
        success: function(data) {
            console.log(data)
            characterParameters.characteristics_ws_initial  = data['characteristics_ws_initial'];
            characterParameters.characteristics_bs_initial  = data['characteristics_bs_initial'];
            characterParameters.characteristics_s_initial   = data['characteristics_s_initial'];
            characterParameters.characteristics_t_initial   = data['characteristics_t_initial'];
            characterParameters.characteristics_i_initial   = data['characteristics_i_initial'];
            characterParameters.characteristics_ag_initial  = data['characteristics_ag_initial'];
            characterParameters.characteristics_dex_initial = data['characteristics_dex_initial'];
            characterParameters.characteristics_int_initial = data['characteristics_int_initial'];
            characterParameters.characteristics_wp_initial  = data['characteristics_wp_initial'];
            characterParameters.characteristics_fel_initial = data['characteristics_fel_initial'];
            characterParameters.fate_fate                   = data['fate_fate'];
            characterParameters.fate_fortune                = data['fate_fortune'];
            characterParameters.resilience_resilience       = data['resilience_resilience'];
            characterParameters.resilience_resolve          = data['resilience_resolve'];
            characterParameters.movement_movement           = data['movement_movement'];
            characterParameters.wounds                      = data['wounds'];
            characterParameters.avalible_attribute_points--
        }
    });

}
function btnDown(input_id) {
    if(characterParameters.avalible_attribute_points >= 60) {
        return
    }
    inp = $('input#'+input_id);
    max = parseInt(inp.attr('max'));
    min = parseInt(inp.attr('min'));
    step = parseInt(inp.attr('step'));
    oldValue = parseInt(inp.val());

    if ((oldValue - step) < min) {
      return
    } else {
      var newVal = oldValue - step;
    }

    console.log("btnDown: input_id="+input_id+"; min="+min + "; max="+max+"; step="+step+"; oldVal="+oldValue+"; newVal="+newVal);
    characterParameters.input_id  = newVal
    inp.val(newVal);
    inp.trigger("change");

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveAttribute",
        data: {
            characer_id: characer_id,
            input_id: input_id,
            'newVal': {
                'characteristics_ws_initial'    : $('input#characteristics_ws_initial'  ).val(),
                'characteristics_bs_initial'    : $('input#characteristics_bs_initial'  ).val(),
                'characteristics_s_initial'     : $('input#characteristics_s_initial'   ).val(),
                'characteristics_t_initial'     : $('input#characteristics_t_initial'   ).val(),
                'characteristics_i_initial'     : $('input#characteristics_i_initial'   ).val(),
                'characteristics_ag_initial'    : $('input#characteristics_ag_initial'  ).val(),
                'characteristics_dex_initial'   : $('input#characteristics_dex_initial' ).val(),
                'characteristics_int_initial'   : $('input#characteristics_int_initial' ).val(),
                'characteristics_wp_initial'    : $('input#characteristics_wp_initial'  ).val(),
                'characteristics_fel_initial'   : $('input#characteristics_fel_initial' ).val()
            }
        },
        success: function(data) {
            characterParameters.characteristics_ws_initial  = data['characteristics_ws_initial'];
            characterParameters.characteristics_bs_initial  = data['characteristics_bs_initial'];
            characterParameters.characteristics_s_initial   = data['characteristics_s_initial'];
            characterParameters.characteristics_t_initial   = data['characteristics_t_initial'];
            characterParameters.characteristics_i_initial   = data['characteristics_i_initial'];
            characterParameters.characteristics_ag_initial  = data['characteristics_ag_initial'];
            characterParameters.characteristics_dex_initial = data['characteristics_dex_initial'];
            characterParameters.characteristics_int_initial = data['characteristics_int_initial'];
            characterParameters.characteristics_wp_initial  = data['characteristics_wp_initial'];
            characterParameters.characteristics_fel_initial = data['characteristics_fel_initial'];
            characterParameters.fate_fate                   = data['fate_fate'];
            characterParameters.fate_fortune                = data['fate_fortune'];
            characterParameters.resilience_resilience       = data['resilience_resilience'];
            characterParameters.resilience_resolve          = data['resilience_resolve'];
            characterParameters.movement_movement           = data['movement_movement'];
            characterParameters.wounds                      = data['wounds'];
            characterParameters.avalible_attribute_points++
        }
    });
}
function btnUpFate(input_id) {
    if(characterParameters.extra_points <= 0) {
        console.error("btnUpFate: " + characterParameters.extra_points + " <= 0" )
        return
    }

    inp = $('input#'+input_id);
    max = parseInt(inp.attr('max'));
    min = parseInt(inp.attr('min'));
    step = parseInt(inp.attr('step'));
    oldValue = parseInt(inp.val());

    if ((oldValue + step) > max) {
        console.error("btnUpFate: (oldValue + step) > max" )
      return
    } else {
      var newVal = oldValue + step;
    }

    characterParameters.input_id  = newVal
    inp.val(newVal);
    inp.trigger("change");

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveFate_and_fortune",
        data: {
            characer_id: characer_id,
            input_id: input_id,
            'newVal': {
                'fate_fate'    : $('input#fate_fate'  ).val(),
                'fate_fortune'    : $('input#fate_fortune'  ).val(),
            }
        },
        success: function(data) {
            characterParameters.fate_fate  = data['fate_fate'];
            characterParameters.fate_fortune  = data['fate_fortune'];
            characterParameters.extra_points--
        }
    });

}
function btnDownFate(input_id) {
    if(characterParameters.extra_points >= 3) {
        console.error("btnUpFate: " + characterParameters.extra_points + " >= 3" )
        return
    }
    inp = $('input#'+input_id);
    max = parseInt(inp.attr('max'));
    min = parseInt(inp.attr('min'));
    step = parseInt(inp.attr('step'));
    oldValue = parseInt(inp.val());

    if ((oldValue - step) < min) {
        console.error("btnDownFate: (oldValue["+oldValue+"] - step["+step+"]) < min["+min+"]" )
      return
    } else {
      var newVal = oldValue - step;
    }

    characterParameters.input_id  = newVal
    inp.val(newVal);
    inp.trigger("change");

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveFate_and_fortune",
        data: {
            characer_id: characer_id,
            input_id: input_id,
            'newVal': {
                'fate_fate'     : $('input#fate_fate').val(),
                'fate_fortune'  : $('input#fate_fortune').val(),
            }
        },
        success: function(data) {
            characterParameters.fate_fate  = data['fate_fate'];
            characterParameters.fate_fortune  = data['fate_fortune'];
            characterParameters.extra_points++
        }
    });
}
function getRandomAttributesTable() {
    $.ajax({
        type: "POST",
        url: "ajax_getRandomAttributesTable",
        data: {
        },
        success: function(data) {
            characterParameters.RandomAttributesTable = data['attributesTable'];
            characterParameters.RandomHairTable = data['hairTable'];
            characterParameters.RandomEyesTable = data['eyesTable'];
            $.each(data['armour'], function(i, item) {
                characterParameters.appendArmour(item);
            });
            $.each(data['weapon'], function(i, item) {
                characterParameters.appendWeapon(item);
            });
            $.each(data['spells'], function(i, item) {
                characterParameters.appendSpells(item);
            });

        }
    });
}
function saveSkillAdv(eventData, points) {
    new_adv_id = $(eventData.currentTarget).val();

    old_skill_adv_db_id = characterParameters.skills_species[eventData.currentTarget.id]
    if(new_adv_id  === '-') {
        $.each(characterParameters.skills, function(i, item) {
            if(item.id == old_skill_adv_db_id) {
                item.adv_species = 0
                characer_id = $("input[name='characer_id']").val()
                $.ajax({
                    type: "POST",
                    url: "ajax_saveSkillAdv",
                    data: {
                        characer_id: characer_id,
                        skill_id: 0,
                        points: points,
                        old_skill_adv: old_skill_adv_db_id
                    },
                    success: function(data) {
                    }
                });
            }
        });
    }
    else {
        new_adv_id = $(eventData.currentTarget).val()
        skill = characterParameters.getSkill(new_adv_id);
        skill.adv_species = parseInt(new_adv_id)
        characterParameters.skills_species[eventData.currentTarget.id] = new_adv_id;

        $.each(characterParameters.skills, function(i, item) {
            if(item.id == old_skill_adv_db_id) {
                item.adv_species = 0
            }
            if(item.id == new_adv_id) {
                item.adv_species = parseInt(points)
                characer_id = $("input[name='characer_id']").val()
                $.ajax({
                    type: "POST",
                    url: "ajax_saveSkillAdv",
                    data: {
                        characer_id: characer_id,
                        skill_id: new_adv_id,
                        points: points,
                        old_skill_adv: old_skill_adv_db_id
                    },
                    success: function(data) {
                    }
                });
            }
        });
    }
}
function saveSkillAdv5(eventData) {
    saveSkillAdv(eventData, 5);
}
function saveSkillAdv3(eventData) {
    saveSkillAdv(eventData, 3);
}
function armour_add() {
    var armour_to_add = $("select#add_armour").val()
    console.log("armour_add: "+ armour_to_add);
    characterParameters.armour_add(armour_to_add);
}
function weapon_add() {
    var weapon_to_add = $("select#add_weapon").val()
    console.log("add_weapon: "+ weapon_to_add);
    characterParameters.add_weapon(weapon_to_add);
}
function spell_add() {
    var spell_to_add = $("select#add_spell").val()
    console.log("add_spell: "+ spell_to_add);
    characterParameters.add_spell(spell_to_add);
}
function main() {

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    getRandomAttributesTable();
    var quantity = jQuery('.quantity_fate input').each( function() {
        jQuery('<div class="quantity-nav"><button class="quantity-button quantity-up" onClick="btnUpFate(\''+this.id+'\')">&#xf106;</button><button class="quantity-button quantity-down" onClick="btnDownFate(\''+this.id+'\')">&#xf107</button></div>').insertAfter(this)
    });

    $("select#species").on("change", selectSpecies);
    $("img#img_character_creaton_next").click(nextStep);

    $("img#img_random_species").click(randomSpecies);
    $("div#"+ character_creation_steps[0]).show();

    $("img#img_random_class").click(randomClass);

    $("input#character_sheet_name").keyup(saveName);
    $("input#age").keyup(saveAge);
    $("input#height").keyup(saveHeight);
    $("select#hair").on("change", saveHair);
    $("select#eyes").on("change", saveEyes);

    var eventData5_1
    var eventData5_2
    var eventData5_3
    var eventData3_1
    var eventData3_2
    var eventData3_3

    $("select#species_skills_5_1").on("change", eventData5_1, saveSkillAdv5);
    $("select#species_skills_5_2").on("change", eventData5_2, saveSkillAdv5);
    $("select#species_skills_5_3").on("change", eventData5_3, saveSkillAdv5);
    $("select#species_skills_3_1").on("change", eventData3_1, saveSkillAdv3);
    $("select#species_skills_3_2").on("change", eventData3_2, saveSkillAdv3);
    $("select#species_skills_3_3").on("change", eventData3_3, saveSkillAdv3);

    $("img#img_random_characteristics").click(randomAttributes);

    $("button#armour_add_button").click(armour_add);
    $("button#weapon_add_button").click(weapon_add);
    $("button#spells_add_button").click(spell_add);

    setInterval(function() {
        characterParameters.updateCharacterState();
    }, 100);

}
