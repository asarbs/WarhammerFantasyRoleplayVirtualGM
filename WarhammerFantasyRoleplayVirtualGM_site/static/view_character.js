
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
        this.#adv_career = 0
        this.#adv_species = 0
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
        if(typeof adv === "number") {
            this.#adv_standard = adv;
            console.log("skill: "+ this.#name + "; new adv_standard="+ this.#adv_standard)
            $('#skills__'+this.id).val(characterParameters.getCharacteristicsCurrent(this.characteristics) + this.adv)
        }
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
    save() {
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveFreeHandSkillAdv",
            data: {
                character_id: $("input[name='character_id']").val(),
                skill_id: this.id,
                skill_adv_val: this.#adv_standard
            },
            success: function(data) {
                console.log("skill save: " + data['status'])
            }
        });
    }
};
class Trapping {
    #id              = 0
    #name            = ""
    #enc             = 0
    #description     = ""
    #is_in_inventory = false
    constructor(id, name, enc, description, is_in_inventory) {
        this.#id = id;
        this.#name = name;
        this.#enc = enc;
        this.#description = description;
        this.#is_in_inventory = is_in_inventory;
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
    get description() {
        return this.#description;
    }
    get is_in_inventory() {
        return this.#is_in_inventory;
    }
    set is_in_inventory(is_in_inventory) {
        if(typeof is_in_inventory === "boolean"){
            this.#is_in_inventory = is_in_inventory;
            console.log("Trapping:"+this.name+" is_in_inventory="+is_in_inventory)
        }
        else {
            throw "Trapping ["+this.#name+"].is_in_inventory = " + is_in_inventory + " is not boolean";
        }
    }
    save_to_character() {
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveTrappingToCharacter",
            data: {
                character_id: characterParameters.id,
                trapping_id: this.id,
            },
            success: function(data) {
                console.log("Trapping save_to_character: " + data['status'])
            }
        });
    }
}
class Talent {
    #id             = 0
    #name           = ""
    #max            = ""
    #test           = ""
    #description    = "";
    #taken          = "";
    constructor(id, name, max, test, description, taken) {
        this.#id = id;
        this.#name = name;
        this.#max = max;
        this.#test = test;
        this.#description = description;
        this.#taken = taken;
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
    set taken(taken) {
        if(typeof taken === "number")
            this.#taken = taken;
        else
            throw "" + taken + " is not a number";
    }
    get taken() {
        return this.#taken
    }
    save_to_character() {
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveTalentToCharacter",
            data: {
                character_id: characterParameters.id,
                talent_id: this.id,
                talent_taken: this.#taken
            },
            success: function(data) {
                console.log("Talent save_to_character: " + data['status'])
            }
        });
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
    #put_on
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
        this.#put_on = false;
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
            throw "Armour ["+this.#name+"].is_in_inventory = " + is_in_inventory + " is not boolean";
        }
    }
    set put_on(put_on) {
        if(typeof put_on === "boolean" ){
            if(this.#put_on != put_on){
                this.#put_on = put_on;
                console.log("Armour.put_on: name="+this.name+"; put_on="+this.#put_on)
                this.put_on_update_ui();
            } else {
                console.log("Armour.put_on: name="+this.name+"; #put_on="+this.#put_on+"; put_on="+put_on)
            }
        }
        else {
            throw "Armour ["+this.#name+"].put_on = " + put_on + " is not boolean";
        }
    }
    get put_on() {
        return this.#put_on;
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
    get is_in_inventory() {
        return this.#is_in_inventory
    }

    try_put_off(locations) {
        var arr_locations = locations.split(", ")
        var item_locations = this.locations.split(", ")
        for(var i = 0; i < arr_locations.length; i++) {
            if(item_locations.includes(arr_locations[i])){
                this.put_on = false
            }
        }

    }

    put_on_update_ui() {
        if(this.is_in_inventory == false) {
            return
        }
        console.log("Armour.put_on_update_ui: name="+this.name+"; put_on="+this.put_on + "; #locations="+this.#locations)
        if(this.put_on == true) {
            $("input#armour_put_on_checkbox__"+this.#id).prop( "checked", true );

            if(this.#locations == "Head") {
                $("input#armour_put_on_head").val(this.armour_points)
            } else if(this.#locations == "Arms") {
                $("input#armour_put_on_left_arm").val(this.armour_points)
                $("input#armour_put_on_right_arm").val(this.armour_points)
            } else if(this.#locations == "Arms, Body") {
                $("input#armour_put_on_left_arm").val(this.armour_points)
                $("input#armour_put_on_right_arm").val(this.armour_points)
                $("input#armour_put_on_body").val(this.armour_points)
            } else if(this.#locations == "Body") {
                $("input#armour_put_on_body").val(this.armour_points)
            } else if(this.#locations == "Legs") {
                $("input#armour_put_on_left_leg").val(this.armour_points)
                $("input#armour_put_on_right_leg").val(this.armour_points)
            } else if(this.#locations == "Shield") {
                $("input#armour_put_on_shield").val(this.armour_points)
            }
        } else if(this.put_on == false) {
            $("input#armour_put_on_checkbox__"+this.#id).prop( "checked", false );

            if(this.#locations == "Head") {
                $("input#armour_put_on_head").val (" ")
            } else if(this.#locations == "Arms") {
                $("input#armour_put_on_left_arm").val (" ")
                $("input#armour_put_on_right_arm").val (" ")
            } else if(this.#locations == "Arms, Body") {
                $("input#armour_put_on_left_arm").val (" ")
                $("input#armour_put_on_right_arm").val (" ")
                $("input#armour_put_on_body").val (" ")
            } else if(this.#locations == "Body") {
                $("input#armour_put_on_body").val (" ")
            } else if(this.#locations == "Legs") {
                $("input#armour_put_on_left_leg").val (" ")
                $("input#armour_put_on_right_leg").val (" ")
            } else if(this.#locations == "Shield") {
                $("input#armour_put_on_shield").val (" ")
            }
        }

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
            new_row += '<td id="armour_put_on__'+this.#id+'" class="center"><input type="checkbox" id="armour_put_on_checkbox__'+this.#id+'" name="armour_put_on__'+this.#id+'" class="armour_put_on" armour_id="'+this.#id+'"></td>'
            new_row += '</tr>'
            $("table#armour").append(new_row)
            $("input[type='checkbox']#armour_put_on_checkbox__"+this.#id).on("change", put_on_armour);
        } else {
            console.log("Armour NOT updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        }
    }

    save() {
        var character_id = $("input[name='character_id']").val()
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_addArmourToCharacter",
            data: {
                character_id: character_id,
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
    #not_sb_group= ['BLACKPOWDER', "CROSSBOW", "ENGINEERING", "EXPLOSIVES", "SLING"]
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
        if(this.#not_sb_group.includes(this.#weapon_group) ) {
            return "+"+this.#damage
        } else if(this.#name === "Lasso") {
            return "-"
        } else if(this.#name === "Incendiary") {
            return "An Incendiary gives every affected target 1+SL Ablaze Conditions";
        }
        return "+SB+"+this.#damage
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
            new_row += '<td id="weapon_name__'+this.#id+'" class="left">'+this.name+'</td>'
            new_row += '<td id="weapon_location__'+this.#id+'" class="center">'+this.weapon_group+'</td>'
            new_row += '<td id="weapon_encumbrance__'+this.#id+'" class="center">'+this.encumbrance+'</td>'
            new_row += '<td id="weapon_armour_points__'+this.#id+'" class="center">'+this.reach_range+'</td>'
            new_row += '<td id="weapon_armour_points__'+this.#id+'" class="center">'+this.damage+'</td>'
            new_row += '<td id="weapon_qualities__'+this.#id+'" class="center">'+this.qualities_and_flaws+'</td>'
            new_row += '</tr>'
            $("table#weapons").append(new_row)
        } else {
            console.log("Weapon: NOT updateUI: "+ this.name +" is_in_inventory:"+this.#is_in_inventory);
        }
    }

    save() {
        var character_id = $("input[name='character_id']").val()
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_addWeaponToCharacter",
            data: {
                character_id: character_id,
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
        var character_id = $("input[name='character_id']").val()
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_addSpellsToCharacter",
            data: {
                character_id: character_id,
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
            'NO': 10,
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

    canCharacteristicsAdvancement(attribureId, career_level) {
        console.log("canCharacteristicsAdvancement:"+attribureId+"; career_level:"+career_level)
        switch(attribureId) {
            case "characteristics_ws_advances"  :
                return this.#characteristics_ws <= career_level;
            case "characteristics_bs_advances"  :
                return this.#characteristics_bs <= career_level;
            case "characteristics_s_advances"   :
                return this.#characteristics_s <= career_level;
            case "characteristics_t_advances"   :
                return this.#characteristics_t <= career_level;
            case "characteristics_i_advances"   :
                return this.#characteristics_i <= career_level;
            case "characteristics_ag_advances"  :
                return this.#characteristics_ag <= career_level;
            case "characteristics_dex_advances" :
                return this.#characteristics_dex <= career_level;
            case "characteristics_int_advances" :
                return this.#characteristics_int <= career_level;
            case "characteristics_wp_advances"  :
                return this.#characteristics_wp <= career_level;
            case "characteristics_fel_advances" :
                return this.#characteristics_fel <= career_level;
            default:
              throw "AdvanceScheme.canCharacteristicsAdvancement("+attribureId+") unrecognized";
          }
    }

}
class Ambitions {
    #id          = 0;
    #description  = "";
    #achieved     = false;
    #shortterm = false;
    #deleted = false;
    constructor(id, description, achieved, shortterm) {
        this.#id            = id
        this.#description   = description
        this.#achieved      = achieved
        this.#shortterm     = shortterm
        this.#deleted = false;
        console.log("Ambitions: id="+this.#id+"; description="+this.#description+"; achieved="+this.#achieved)
    }

    set description(description) {
        if(typeof description === "string")
            this.#description = description;
        else
            throw "Ambitions: description=" + description + " is not a string";
    }
    set achieved(achieved) {
        if(typeof achieved === "boolean"){
            this.#achieved = achieved;
        }
        else {
            throw "Ambitions: achieved=" + achieved + " boolean";
        }
    }
    get achieved() {
        return this.#achieved;
    }
    get description() {
        return this.#description
    }
    set id(id) {
        if(typeof id === "number" && this.#id == 0) {
            this.#id = id;
        }
        else if(this.#id != id) {
            throw "Ambitions: #id" + this.#id + "; id="+id+" is not a number";
        }
    }
    get id() {
        return this.#id;
    }
    set deleted(deleted) {
        if(typeof deleted === "boolean"){
            this.#deleted = deleted;

            let id = this.id

            if(this.#deleted == true) {
                $.ajax({
                    type: "POST",
                    url: "/wfrpg_gm/ajax_removeAmbitions",
                    async: false,
                    cache: false,
                    timeout: 30000,
                    fail: function(){
                        return true;
                    },
                    data: {
                        ambition_id   : this.#id
                    },
                    success: function(data) {
                        $("li[ambitions_id="+id+"]").remove()
                        console.log("remove: li [ambitions_id="+id+"]")
                    }
                });
            }
        }
        else {
            throw "Ambitions: deleted=" + deleted + " boolean";
        }
    }
    get deleted() {
        return this.#deleted;
    }

    updateUI() {
        var cl = this.#shortterm == true ? "ambitions_shortterm" : "ambitions_longterm"
        var new_row = ""
        console.log("Ambitions.updateUI(): this.id="+this.id)
        if($("li[ambitions_id="+this.id+"]").length > 0) {

            if(this.#deleted == true) {
                return;
            }

            if(this.#achieved == true) {
                $("img[ambitions_id="+this.id+"]").remove()
                $("li.to_achieved[ambitions_id="+this.id+"]").addClass("achieved")
                $("li.to_achieved[ambitions_id="+this.id+"]").removeClass("to_achieved")
            } else {
                $("li.to_achieved[ambitions_id="+this.id+"]").removeClass("achieved")
                $("li.to_achieved[ambitions_id="+this.id+"]").addClass("to_achieved")
            }
        } else if( this.#id > 0) {
            if(this.#achieved == true) {
                new_row = "<li class=\"achieved\">"+this.#description+"</li>";
                $("ol."+cl).append(new_row)
            } else {
                new_row = "<li class=\"to_achieved\" ambitions_id='"+this.id+"'>"+this.#description+"   <img src=\"/static/img/tick.png\" width=\"15\" close_ambitions_id='"+this.id+"'><img src=\"/static/img/trash.png\" width=\"15\" delete_ambitions_id='"+this.id+"'></li>";
                $("ol."+cl).append(new_row)
                $("li.to_achieved img[close_ambitions_id="+this.id+"]").click(close_ambition)
                $("li.to_achieved img[delete_ambitions_id="+this.id+"]").click(delete_ambition)
            }
            console.log("Ambitions.updateUI() cl="+cl+"; new_row="+new_row)
        }
    }

    save() {
        var ambition = this;
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveAmbitions",
            async: false,
            cache: false,
            timeout: 30000,
            fail: function(){
                return true;
            },
            data: {
                ambitions_id   : this.id,
                description    : this.description,
                achieved       : this.achieved,
                character_id   : characterParameters.id,
                is_shortterm   : this.#shortterm
            },
            success: function(data) {
                ambition.id = data['id']
                console.log("Ambitions.save: ambition.id="+ambition.id)
                return true;
            }
        });
    }

}
class CharacterParameters {
    #id                                 = 0;
    #age                                = 0;
    #avalible_attribute_points          = 100;
    #experience_current                 = 0;
    #experience_spent                   = 0;
    #career_id                          = 0;
    #career_level                       = 0;
    #career_path_id                        = "";
    #ch_class_id                        = 0;
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
    #careers_advance_scheme_ws_initial  =  "";
    #careers_advance_scheme_bs_initial  =  "";
    #careers_advance_scheme_s_initial   =  "";
    #careers_advance_scheme_t_initial   =  "";
    #careers_advance_scheme_i_initial   =  "";
    #careers_advance_scheme_ag_initial  =  "";
    #careers_advance_scheme_dex_initial =  "";
    #careers_advance_scheme_int_initial =  "";
    #careers_advance_scheme_wp_initial  =  "";
    #careers_advance_scheme_fel_initial =  "";
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
    #resilience_motivation              = "";
    #skills                             = {};
    #trappings                          = {};
    #species                            = 0;
    #status                             = "";
    #talents                            = {};
    #armour                             = [];
    #weapon                             = [];
    #spells                             = [];
    #wounds                             = 0;
    skills_species                      = {};
    #improvementXPCosts                 = [];
    #wealth                             = 0;
    #ambitions_shortterm                = [];
    #ambitions_longterm                 = [];
    #notes                              = [];
    #advanceScheme;
    classModel = {}
    movement = {
        0: {'walk': 0,"run": 0},
        3: {'walk': 6,"run": 12},
        4: {'walk': 8,"run": 16},
        5: {'walk': 10,"run": 20},
        };

    constructor() {
        console.log("CharacterParameters::constructor");
    }
    set id(id) {
        if(typeof id === "number") {
            this.#id = id;
        }
        else
            throw "character id:" + id + " is not a number";
    }
    get id() {
        return this.#id;
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
            $("select#hair").val(this.#hair).change();
        }
        else
            throw "hair: " + hair + " is not a string";
    }
    set eyes(eyes) {
        if(typeof eyes === "number") {
            this.#eyes = eyes;
            $("select#eyes").val(this.#eyes).change();
        }
        else
            throw "eyes: " + eyes + " is not a string";
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
    set experience_spent(experience_spent) {
        if(typeof experience_spent === "number") {
            this.#experience_spent = experience_spent;
            $("input#experience_spent").val(characterParameters.experience_spent);
            $("input#experience_total").val(characterParameters.experience_current + characterParameters.experience_spent);
        }
        else
            throw "experience_spent[" + experience_spent + "] is not a number";
    }
    get experience_spent() {
        return this.#experience_spent;
    }
    set experience_current(experience_current) {
        if(typeof experience_current === "number") {
            this.#experience_current = experience_current;
            $("input#experience_current").val(characterParameters.experience_current);
            $("input#experience_total").val(characterParameters.experience_current + characterParameters.experience_spent);
        }
        else
            throw "experience_current[" + experience_current + "] is not a number";
    }
    get experience_current() {
        return this.#experience_current;
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
            $("input#encumbrance_max"          ).val(characterParameters.s_bonus + characterParameters.t_bonus)
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
            $("input#encumbrance_max"          ).val(characterParameters.s_bonus + characterParameters.t_bonus)
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

    set careers_advance_scheme_ws_initial (x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_ws_initial = x;
            $("td#careers_advance_scheme_ws_initial").html('<img src="/static/' + this.#careers_advance_scheme_ws_initial + '.png">')
        } else {
            throw "careers_advance_scheme_ws_initial["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_bs_initial (x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_bs_initial = x;
            $("td#careers_advance_scheme_bs_initial").html('<img src="/static/' + this.#careers_advance_scheme_bs_initial + '.png">')
        } else {
            throw "careers_advance_scheme_bs_initial["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_s_initial  (x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_s_initial  = x;
            $("td#careers_advance_scheme_s_initial").html('<img src="/static/' + this.#careers_advance_scheme_s_initial + '.png">')
        } else {
            throw "careers_advance_scheme_s_initial ["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_t_initial  (x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_t_initial  = x;
            $("td#careers_advance_scheme_t_initial").html('<img src="/static/' + this.#careers_advance_scheme_t_initial + '.png">')
        } else {
            throw "careers_advance_scheme_t_initial ["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_i_initial  (x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_i_initial  = x;
            $("td#careers_advance_scheme_i_initial").html('<img src="/static/' + this.#careers_advance_scheme_i_initial + '.png">')
        } else {
            throw "careers_advance_scheme_i_initial ["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_ag_initial (x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_ag_initial = x;
            $("td#careers_advance_scheme_ag_initial").html('<img src="/static/' + this.#careers_advance_scheme_ag_initial + '.png">')
        } else {
            throw "careers_advance_scheme_ag_initial["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_dex_initial(x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_dex_initial= x;
            $("td#careers_advance_scheme_dex_initial").html('<img src="/static/' + this.#careers_advance_scheme_dex_initial + '.png">')
        } else {
            throw "careers_advance_scheme_dex_initia["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_int_initial(x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_int_initial = x;
            $("td#careers_advance_scheme_int_initial").html('<img src="/static/' + this.#careers_advance_scheme_int_initial + '.png">')
        } else {
            throw "careers_advance_scheme_int_initia["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_wp_initial (x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_wp_initial = x;
            $("td#careers_advance_scheme_wp_initial").html('<img src="/static/' + this.#careers_advance_scheme_wp_initial + '.png">')
        } else {
            throw "careers_advance_scheme_wp_initial["+ x +"] is not a string";
        }
    }
    set careers_advance_scheme_fel_initial(x) {
        if(typeof x === "string") {
            this.#careers_advance_scheme_fel_initial= x;
            $("td#careers_advance_scheme_fel_initial").html('<img src="/static/' + this.#careers_advance_scheme_fel_initial + '.png">')

        } else {
            throw "careers_advance_scheme_fel_initia["+ x +"] is not a string";
        }
    }

    get careers_advance_scheme_ws_initial () {
        return this.#careers_advance_scheme_ws_initial ;
    }
    get careers_advance_scheme_bs_initial () {
        return this.#careers_advance_scheme_bs_initial ;
    }
    get careers_advance_scheme_s_initial  () {
        return this.#careers_advance_scheme_s_initial  ;
    }
    get careers_advance_scheme_t_initial  () {
        return this.#careers_advance_scheme_t_initial  ;
    }
    get careers_advance_scheme_i_initial  () {
        return this.#careers_advance_scheme_i_initial  ;
    }
    get careers_advance_scheme_ag_initial () {
        return this.#careers_advance_scheme_ag_initial ;
    }
    get careers_advance_scheme_dex_initial() {
        return this.#careers_advance_scheme_dex_initial;
    }
    get careers_advance_scheme_int_initial() {
        return this.#careers_advance_scheme_int_initial;
    }
    get careers_advance_scheme_wp_initial () {
        return this.#careers_advance_scheme_wp_initial ;
    }
    get careers_advance_scheme_fel_initial() {
        return this.#careers_advance_scheme_fel_initial;
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
            throw "fate_fate[" + fate_fate + "] is not a number";
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
            throw "fate_fortune[" + fate_fortune + "] is not a number";
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
            throw "resilience_resilience[" + resilience_resilience + "] is not a number";
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
            throw "resilience_resolve[" + resilience_resolve + "] is not a number";
    }
    get resilience_resolve() {
        return this.#resilience_resolve;
    }
    set resilience_motivation(resilience_motivation) {
        if(typeof resilience_motivation === "string") {
            this.#resilience_motivation = resilience_motivation;
            $("input#resilience_motivation"       ).val(characterParameters.resilience_motivation)
        }
        else
            throw "resilience_resolve[" + resilience_resolve + "] is not a number";
    }
    get resilience_motivation() {
        return this.#resilience_motivation
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
    set wealth(wealth) {
        if(typeof wealth === "number") {
            this.#wealth = wealth;
            $("input#wealth"                      ).val(characterParameters.wealth)
        }
        else
            throw "wealth[" + wealth + "] is not a number";
    }
    get wealth() {
        var GC = Math.floor(this.#wealth / 240)
        var GC_left = this.#wealth % 240
        var SC = Math.floor(GC_left / 12)
        var SC_left = GC_left % 12
        var BC = SC_left
        return GC+"GC " + SC + "/" + BC
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
    set species(species) {
        if(typeof species === "number") {
            this.#species = species;
            $("select#species").val(this.#species).change();
        }
        else
            throw "species[" + species + "] is not a number";
    }
    get species() {
        return this.#species
    }
    set career_id(career_id) {
        if(typeof career_id === "number") {
            this.#career_id = career_id;
            $("select#career").val(this.#career_id).change();
            $("input#career_path").val(this.classModel[this.#ch_class_id].carrer[this.career_id].name);
        }
        else {
            throw "career_name[" + career_id + "] is not a number";
        }
    }
    get career_id() {
        return this.#career_id
    }
    set ch_class_id(ch_class_id) {
        if(typeof ch_class_id === "number") {
            this.#ch_class_id = ch_class_id;
            console.log("set ch_class_id:"+this.#ch_class_id);
            $("select#class").val(this.#ch_class_id).change();
            $("select#career").find('option').remove()

            for(let k in this.classModel[this.#ch_class_id].carrer) {
                 $("select#career").append($('<option>', {value: this.classModel[this.#ch_class_id].carrer[k].id, text: this.classModel[this.#ch_class_id].carrer[k].name }));
            }

            $("select#career").val(this.#career_id).change();
        }
        else
            throw "ch_class_name[" + ch_class_id + "] is not a number";
    }
    get ch_class_id() {
        return this.#ch_class_id
    }
    set career_path_id(career_path_id) {
        if(typeof career_path_id === "number") {
            this.#career_path_id = career_path_id;
        }
        else
            throw "career_path[" + career_path_id + "] is not a number";
    }
    get career_path_id() {
        return this.#career_path_id;
    }
    set status(status) {
        if(typeof status === "string") {
            this.#status = status;
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
            $("input#status").val(this.classModel[this.#ch_class_id].carrer[this.career_id].careersAdvanceScheme[[this.career_id]].advances_level[this.#career_level].status.tier + " "+ this.classModel[this.#ch_class_id].carrer[this.career_id].careersAdvanceScheme[[this.career_id]].advances_level[this.#career_level].status.level);
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
    updateSkillTable() {
        var sorted_skills = []
        for(let skill_key in this.#skills) {
            sorted_skills[this.#skills[skill_key].name] = this.#skills[skill_key]
        }
        console.log(sorted_skills)

        var keys_sorted_skills = Object.keys(sorted_skills);
        keys_sorted_skills.sort()

        for (var k = 0; k < keys_sorted_skills.length; k++) {
            var key = keys_sorted_skills[k]
            var item = sorted_skills[key]
            console.log("updateSkillTable:" +k+ ";"+ item.name)
            var new_row = ""
            if(!$('#skills_adv__'+item.id).length && !$('#skills_characteristics__'+item.id).length) {
                new_row = '<tr class="block_body">'
                new_row += '<td id="skills_name__'+item.id+'" class="left">'+item.name+'</td>'
                new_row += '<td class="characteristics">'+item.characteristics+'</td>'
                new_row += '<td class="edit"><input type="number" id="skills_characteristics__'+item.id+'" name="fname"></td>'
                new_row += '<td class="edit"><input type="number" id="skills_adv__'+item.id+'" class="skills_adv" skill_id="'+item.id+'" min="0" max="100" step="1" name="fname"></td>'
                new_row += '<td class="edit"><input type="number" id="skills__'+item.id+'" name="fname"></td>'
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

        };
    }
    updateTalentsTable() {
        console.log("updateTalentsTable");
        $("table#talents_table tr.block_body").remove();
        $.each(this.#talents, function(i, item) {
            var new_row = ""
            if(!$('#talents_adv__'+item.id).length && item.taken > 0) {
                new_row = '<tr class="block_body">'
                new_row += '<td id="talents_name__'+item.id+'" class="left"><a href="/wfrpg_gm/TalentsEditView/'+item.id+'">'+item.name+'</a></td>'
                new_row += '<td class="edit"><input type="text" id="talents_adv__'+item.id+'" class="talents_adv" talent_id="'+item.id+'" min="0" max="100" step="1" name="fname" talent_id="'+item.id+'"></td>'
                new_row += '<td class="description">'+item.description+'</br><b>Max:'+item.max+'</b></td>'
                new_row += '</tr>'
                $("#talents_table").append(new_row)
                $('#talents_adv__'+item.id).val(item.taken)
            }
        });
    }
    updateTrappingsTable() {
        if(!this.trappingsNeedUpdate) {
            console.log("updateTrappingsTable return");
            return;
        }
        console.log("updateTrappingsTable");
        this.trappingsNeedUpdate = false;
        $("table#trappings_table tr.block_body").remove();

        $.each(this.#trappings, function(i, item) {
            var new_row = ""
            if(!$('#trappings_enc__'+item.id).length && item.is_in_inventory) {
                console.log("updateTrappingsTable: "+item.id +"; "+item.name);
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
                                                    parseInt(skill_params['adv']),
                                                    parseInt(skill_params['adv']),
                                                    parseInt(skill_params['adv']));
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
        // console.log("appendTrappings:"+ trapping['id']+"; "+trapping['name']+"; "+trapping['description']+"; "+trapping['enc']);
        // id, name, enc, description, is_in_inventory
        let traping = new Trapping(trapping['id'], trapping['name'],trapping['enc'],trapping['description'],trapping['is_in_inventory']);
        this.#trappings[trapping['id']] = traping
        this.trappingsNeedUpdate = true;
        $("select#add_trappings").append($('<option>', {value: traping.id, text: traping.name}));
    }
    deleteTrappings() {
        console.log("deleteTrappings");
        this.#trappings = {};
    }
    appendTalent(talent_params) {
        let talent = new Talent(talent_params['id'],
        talent_params['name'],
        talent_params['max'],
        talent_params['test'],
        talent_params['description'],
        talent_params['taken']);

        this.#talents[talent_params['id']] = talent;
        $("select#add_talents").append($('<option>', {value: talent.id, text: talent.name }));
    }
    add_talent(talent_to_add) {
        console.log("characeter add_talent: "+ talent_to_add);
        $.each(this.#talents, function(i, item) {
            if(item.id == talent_to_add) {
                console.log("characeter add_talent: "+ talent_to_add);
                item.taken++;
                item.save_to_character();
            }
        });
    }
    add_trappings(trappings_to_add) {
        $.each(this.#trappings, function(i, item) {
            if(item.id == trappings_to_add) {
                console.log("characeter add_trappings: "+ trappings_to_add);
                item.is_in_inventory = true;
                characterParameters.trappingsNeedUpdate = true;
                characterParameters.updateTrappingsTable();
                item.save_to_character();
            }
        });
    }
    appendArmour(armour) {
        console.log("appendArmour: +"+armour)
        var a = new Armour(armour.id,
            armour.name,
            armour.armour_type,
            armour.price,
            armour.encumbrance,
            armour.availability,
            armour.penalty,
            armour.locations,
            armour.armour_points,
            armour.is_in_inventory);
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
            weapon.is_in_inventory);
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
            spell.is_in_inventory);
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
    appendImprovementXPCosts(improvementXPCosts) {
        this.#improvementXPCosts.push(improvementXPCosts);
    }
    calcCharacteristicAdvXPPointCost(adv) {
        $.each(this.#improvementXPCosts, function(i, item) {
            if(item['advances_interval_start'] >= adv && item['advances_interval_end'] <= adv) {
                return item['characteristics_xp_cost'];
            }
        })
        throw "calcCharacteristicAdvXPPointCost: adv=" + adv + "; out of bound"
    }
    calcSkillsAdvXPPointCost(adv) {
        $.each(this.#improvementXPCosts, function(i, item) {
            if(item['advances_interval_start'] >= adv && item['advances_interval_end'] <= adv) {
                return item['skills_xp_cost'];
            }
        })
        throw "calcSkillsAdvXPPointCost: adv=" + adv + "; out of bound"
    }
    isInCharacteristicAdvancement(attribureId) {
        return this.#advanceScheme.canCharacteristicsAdvancement(attribureId, this.#career_level)
    }
    upCharacteristicsXPSpend(newCharVal) {
        console.log("upCharacteristicsXPSpend: "+ newCharVal);
        for(let i = 0 ; i < this.#improvementXPCosts.length; i++ ) {
            var item = this.#improvementXPCosts[i];
            console.log("newCharVal["+newCharVal+"] >= item.advances_interval_start["+item.advances_interval_start+"] && newCharVal["+newCharVal+"] <= item.advances_interval_end["+item.advances_interval_end+"]");
            if(newCharVal >= item.advances_interval_start && newCharVal <= item.advances_interval_end) {
                if(this.experience_current - item.characteristics_xp_cost < 0) {
                    return false;
                }
                this.experience_current -= item.characteristics_xp_cost;
                this.experience_spent += item.characteristics_xp_cost;
                return true
            }
        }
        throw( "newCharVal:" + newCharVal +" out of scope");
    }
    downCharacteristicsXPSpend(newCharVal) {
        console.log("downCharacteristicsXPSpend: "+ newCharVal);
        for(let i = 0 ; i < this.#improvementXPCosts.length; i++ ) {
            var item = this.#improvementXPCosts[i];
            if(newCharVal >= item.advances_interval_start && newCharVal <= item.advances_interval_end) {
                if(this.#experience_spent - item.characteristics_xp_cost < 0) {
                    console.log("downCharacteristicsXPSpend false");
                    return false;
                }
                this.experience_current += item.characteristics_xp_cost;
                this.experience_spent -= item.characteristics_xp_cost;
                console.log("downCharacteristicsXPSpend true");
                return true;
            }
        }
        throw( "newCharVal:" + newCharVal +" out of scope");
    }
    upSkillsXPSpend(newCharVal) {
        console.log("upSkillsXPSpend: "+ newCharVal);
        for(let i = 0 ; i < this.#improvementXPCosts.length; i++ ) {
            var item = this.#improvementXPCosts[i];
            console.log("newCharVal["+newCharVal+"] >= item.advances_interval_start["+item.advances_interval_start+"] && newCharVal["+newCharVal+"] <= item.advances_interval_end["+item.advances_interval_end+"]");
            if(newCharVal >= item.advances_interval_start && newCharVal <= item.advances_interval_end) {
                if(this.experience_current - item.skills_xp_cost < 0) {
                    console.log("upSkillsXPSpend false");
                    return false;
                }
                this.experience_current -= item.skills_xp_cost;
                this.experience_spent += item.skills_xp_cost;
                console.log("upSkillsXPSpend true");
                return true
            }
        }
        throw( "newSkillVal:" + newCharVal +" out of scope");
    }
    downSkillsXPSpend(newCharVal) {
        console.log("downSkillsXPSpend: "+ newCharVal);
        for(let i = 0 ; i < this.#improvementXPCosts.length; i++ ) {
            var item = this.#improvementXPCosts[i];
            if(newCharVal >= item.advances_interval_start && newCharVal <= item.advances_interval_end) {
                if(this.#experience_spent - item.skills_xp_cost < 0) {
                    console.log("downSkillsXPSpend false");
                    return false;
                }
                this.experience_current += item.skills_xp_cost;
                this.experience_spent -= item.skills_xp_cost;
                console.log("downSkillsXPSpend true");
                return true;
            }
        }
        throw( "newSkillVal:" + newCharVal +" out of scope");
    }
    updateSkillVal(skill_id, newVal) {
        console.log("updateSkillVal: this.#skills.length="+this.#skills.length);
        this.#skills[skill_id].adv_standard = newVal;
        this.#skills[skill_id].save();
    }
    updateCharacterAdvVal(characteristics_id, characteristics_adv_val) {
        switch(characteristics_id) {
            case "characteristics_ws_advances" :
                this.characteristics_ws_advances = characteristics_adv_val;
                break;
            case "characteristics_bs_advances" :
                this.characteristics_bs_advances = characteristics_adv_val;
                break;
            case "characteristics_s_advances"  :
                this.characteristics_s_advances = characteristics_adv_val;
                break;
            case "characteristics_t_advances"  :
                this.characteristics_t_advances = characteristics_adv_val;
                break;
            case "characteristics_i_advances"  :
                this.characteristics_i_advances = characteristics_adv_val;
                break;
            case "characteristics_ag_advances" :
                this.characteristics_ag_advances = characteristics_adv_val;
                break;
            case "characteristics_dex_advances":
                this.characteristics_dex_advances = characteristics_adv_val;
                break;
            case "characteristics_int_advances":
                this.characteristics_int_advances = characteristics_adv_val;
                break;
            case "characteristics_wp_advances" :
                this.characteristics_wp_advances = characteristics_adv_val;
                break;
            case "characteristics_fel_advances":
                this.characteristics_fel_advances = characteristics_adv_val;
                break;
        }

        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveFreeHandCharacteristicAdv",
            data: {
                character_id: $("input[name='character_id']").val(),
                characteristics_ws_advances  : this.characteristics_ws_advances,
                characteristics_bs_advances  : this.characteristics_bs_advances,
                characteristics_s_advances   : this.characteristics_s_advances,
                characteristics_t_advances   : this.characteristics_t_advances,
                characteristics_i_advances   : this.characteristics_i_advances,
                characteristics_ag_advances  : this.characteristics_ag_advances,
                characteristics_dex_advances : this.characteristics_dex_advances,
                characteristics_int_advances : this.characteristics_int_advances,
                characteristics_wp_advances  : this.characteristics_wp_advances,
                characteristics_fel_advances : this.characteristics_fel_advances,
            },
            success: function(data) {
                console.log("skill save: " + data['status'])
            }
        });
    }
    updateCharacterInitialVal(characteristics_id, characteristics_adv_val) {
        switch(characteristics_id) {
            case "characteristics_ws_initial" :
                this.characteristics_ws_initial = characteristics_adv_val;
                break;
            case "characteristics_bs_initial" :
                this.characteristics_bs_initial = characteristics_adv_val;
                break;
            case "characteristics_s_initial"  :
                this.characteristics_s_initial = characteristics_adv_val;
                break;
            case "characteristics_t_initial"  :
                this.characteristics_t_initial = characteristics_adv_val;
                break;
            case "characteristics_i_initial"  :
                this.characteristics_i_initial = characteristics_adv_val;
                break;
            case "characteristics_ag_initial" :
                this.characteristics_ag_initial = characteristics_adv_val;
                break;
            case "characteristics_dex_initial":
                this.characteristics_dex_initial = characteristics_adv_val;
                break;
            case "characteristics_int_initial":
                this.characteristics_int_initial = characteristics_adv_val;
                break;
            case "characteristics_wp_initial" :
                this.characteristics_wp_initial = characteristics_adv_val;
                break;
            case "characteristics_fel_initial":
                this.characteristics_fel_initial = characteristics_adv_val;
                break;
        }

        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveFreeHandCharacteristicInit",
            data: {
                character_id: this.#id,
                characteristics_ws_initial  : this.characteristics_ws_initial,
                characteristics_bs_initial  : this.characteristics_bs_initial,
                characteristics_s_initial   : this.characteristics_s_initial,
                characteristics_t_initial   : this.characteristics_t_initial,
                characteristics_i_initial   : this.characteristics_i_initial,
                characteristics_ag_initial  : this.characteristics_ag_initial,
                characteristics_dex_initial : this.characteristics_dex_initial,
                characteristics_int_initial : this.characteristics_int_initial,
                characteristics_wp_initial  : this.characteristics_wp_initial,
                characteristics_fel_initial : this.characteristics_fel_initial,
            },
            success: function(data) {
                console.log("skill save: " + data['status'])
            }
        });
    }
    upTalentXPSpend(oldValue) {
        var xpToSpend = oldValue * 100 + 100;
        if( xpToSpend <= this.experience_current) {
            this.experience_current -= xpToSpend;
            this.experience_spent += xpToSpend;
            console.log("upTalentXPSpend: oldValue="+ oldValue + "; ok");
            return true

        }
        console.log("upTalentXPSpend: oldValue="+ oldValue + "; not ok");
        return false;
    }
    downTalentXPSpend(oldValue) {
        console.log("downTalentXPSpend: oldValue="+ oldValue);

        var xpToSpend = oldValue * 100 + 100;
        if( this.#experience_spent - xpToSpend  >= this.experience_current) {
            this.experience_current += xpToSpend;
            this.experience_spent -= xpToSpend;
            console.log("downTalentXPSpend: oldValue="+ oldValue + "; ok");
            return true
        }
        console.log("downTalentXPSpend: oldValue="+ oldValue + "; not ok");
        return false;
    }
    updateTalentVal(talent_id, newVal) {
        console.log("updateTalentVal: this.#talents.length="+this.#talents.length);
        this.#talents[talent_id].taken = newVal;
    }
    get hardy() {
        console.log("hardy: "+ this.#talents)
        if( 417 in this.#talents) {
            let talent = this.#talents[417]
            console.log("hardy: "+ talent)
            return talent.taken
        }
        return 0
    }

    updateWounds() {
        $("input#hardy"              ).val(this.hardy + " * " + this.t_bonus);
        $("input#wounds"              ).val(this.s_bonus + 2 * this.t_bonus + this.hardy * this.t_bonus + this.wp_bonus);
    }
    updateEncumbrance() {
        console.log("updateEncumbrance")
        var trapping_enc_sum = 0
        var armour_enc_sum = 0
        var weapons_enc_sum = 0
        $.each(this.#trappings, function(i, item) {
            console.log("updateEncumbrance trappings :"+item.is_in_inventory)
            if(item.is_in_inventory) {
                trapping_enc_sum += item.enc
            }
        });
        $.each(this.#armour, function(i ,item) {
            console.log("updateEncumbrance armour :"+item.is_in_inventory)
            if(item.is_in_inventory) {
                armour_enc_sum += item.encumbrance
            }
        });
        $.each(this.#weapon, function(i ,item) {
            console.log("updateEncumbrance weapon :"+item.is_in_inventory)
            if(item.is_in_inventory) {
                weapons_enc_sum += item.encumbrance
            }
        });
        $("input#encumbrance_trappings").val(trapping_enc_sum)
        $("input#encumbrance_armour").val(armour_enc_sum)
        $("input#encumbrance_weapons").val(weapons_enc_sum)
        $("input#encumbrance_total").val(trapping_enc_sum + armour_enc_sum + weapons_enc_sum)

    }
    append_ambitions_shortterm(ambitions_to_append) {
        let ambition = new Ambitions(ambitions_to_append['id'], ambitions_to_append['description'],
        ambitions_to_append['achieved'], true)
        this.#ambitions_shortterm.push(ambition);
        ambition.updateUI();
        return ambition
    }
    append_ambitions_longterm(ambitions_to_append) {
        let ambition = new Ambitions(ambitions_to_append['id'], ambitions_to_append['description'], ambitions_to_append['achieved'], false)
        this.#ambitions_longterm.push(ambition);
        ambition.updateUI();
        return ambition
    }
    appendNote(note) {
        let new_note = new Note(note['id'], note['datetime_create'], note['timestamp'], note['note_text']);
        this.#notes.push(new_note);
        new_note.updateUI();
    }
    saveNote(note) {
        let new_note = new Note(note['id'], note['datetime_create'], note['timestamp'], note['note_text']);
        this.#notes.push(new_note);
        new_note.save();
    }

    updateAmbition(ambition_id, achieved) {
        console.log("updateAmbition: ambition_id="+ambition_id+"; achieved="+achieved )
        for(let a in this.#ambitions_shortterm) {
            if(ambition_id == this.#ambitions_shortterm[a].id) {
                this.#ambitions_shortterm[a].achieved = achieved
                this.#ambitions_shortterm[a].updateUI();
                this.#ambitions_shortterm[a].save()
                this.experience_current += 50
                return
            }
        }
        for(let a in this.#ambitions_longterm) {
            if(ambition_id == this.#ambitions_longterm[a].id) {
                this.#ambitions_longterm[a].achieved = achieved
                this.#ambitions_longterm[a].updateUI();
                this.#ambitions_longterm[a].save()
                this.experience_current += 500
                return
            }
        }
    }
    deleteAmbition(ambition_id) {
        console.log("deleteAmbition: ambition_id="+ambition_id)
        for(let a in this.#ambitions_shortterm) {
            if(ambition_id == this.#ambitions_shortterm[a].id) {
                this.#ambitions_shortterm[a].deleted = true;
                return
            }
        }
        for(let a in this.#ambitions_longterm) {
            if(ambition_id == this.#ambitions_longterm[a].id) {
                this.#ambitions_longterm[a].deleted = true;
                return
            }
        }
    }
    save_currentXP() {
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveCurrentEp",
            data: {
                character_id: character_id,
                experience_current : this.experience_current,
            },
            success: function(data) {

            }
        });
    }
    save_wealth(wealth) {
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_saveWealth",
            data: {
                character_id: character_id,
                wealth : wealth,
            },
            success: function(data) {
                console.log(data)
                characterParameters.wealth = data['wealth']
            }
        });
    }
    put_on_armour(armour_id, checked) {
        var a
        $.each(this.#armour, function(i, item) {
            if(item.id == armour_id) {
                a = item
            }
        });

        $.each(this.#armour, function(i, item) {
            item.try_put_off(a.locations)
        });

        a.put_on = checked;
        a.put_on_update_ui();
    }
};
class Note{
    #id              = 0;
    #datetime_create = "";
    #timestamp       = 0;
    #note_text       = "";
    constructor(id, datetime_create, timestamp, note_text) {
        this.#id              = id;
        this.#datetime_create = datetime_create;
        this.#timestamp       = parseInt(timestamp);
        this.#note_text       = note_text;
    }
    get id() {
        return this.#id;
    }
    get datetime_create() {
        return this.#datetime_create;
    }
    get timestamp() {
        return this.#timestamp
    }
    get note_text() {
        return this.#note_text
    }
    set id(id) {
        if(typeof id === "number")
            this.#id = id;
        else
            throw "Note.id: \"" + id + "\" is not a number";
    }
    set datetime_create(datetime_create) {
        if(typeof datetime_create === "string")
            this.#datetime_create = datetime_create;
        else
            throw "Note.datetime_create: \"" + datetime_create + "\" is not a string";
    }
    set timestamp(timestamp) {
        if(typeof timestamp === "number")
            this.#timestamp = timestamp;
        else
            throw "Note.timestamp: \"" + timestamp + "\" is not a number";
    }
    set note_text(note_text) {
        if(typeof note_text === "string")
            this.#note_text = note_text;
        else
            throw "Note.note_text: \"" + note_text + "\" is not a string";
    }
    updateUI() {
        console.log("Note.updateUI: "+ this.datetime_create);
        if(!$('td#player_notes_timestamp__'+this.#timestamp).length) {
            var new_row = '<tr class="note_line">'
            new_row += '<td id="player_notes_timestamp__'+this.#timestamp+'" class="date">'+this.#datetime_create+'</td>'
            new_row += '<td>'+this.#note_text+'</td>'
            new_row += '</tr>'
            $("table#player_notes tr.block_header").after(new_row)
        } else {
            console.log("NOT Note.updateUI: "+ this.datetime_create);
        }
    }
    save() {
        var note = this;
        $.ajax({
            type: "POST",
            url: "/wfrpg_gm/ajax_savePlayerNote",
            async: false,
            cache: false,
            timeout: 30000,
            fail: function(){
                return true;
            },
            data: {
                character_id   : characterParameters.id,
                note_text   : this.#note_text
            },
            success: function(data) {
                console.log(data)
                note.id = data['id']
                note.datetime_create = data['datetime_create']
                note.timestamp = parseInt(data['timestamp'])
                console.log("Note.save: id="+note.id+"; datetime_create="+note.datetime_create+"; timestamp="+note.timestamp);
                note.updateUI();
                return true;
            }
        });
    }
}
const characterParameters = new CharacterParameters();
var character_id = 0
function get_characterData(){

    console.log("get_characterData")

    get_fullHairList();
    get_fullEyesList();
    get_fullSkillList();
    get_fullSpeciesList();
    get_fullClassList();

    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_view_getCharacterData",
        data: {
            character_id: character_id,
        },
        success: function(data) {
            console.log(data);
            characterParameters.id                           = data['character']["id"                           ]
            characterParameters.name                         = data['character']["name"                         ]
            characterParameters.species                      = data['character']["species"                      ]
            characterParameters.ch_class_id                  = data['character']["ch_class"                     ]
            characterParameters.career_id                    = data['character']["career"                       ]
            characterParameters.career_path_id               = data['character']["career_path"                  ]
            characterParameters.status                       = data['character']["status"                       ]
            characterParameters.career_level                 = data['character']["career_level"                 ]
            characterParameters.age                          = data['character']["age"                          ]
            characterParameters.height                       = data['character']["height"                       ]
            characterParameters.hair                         = data['character']["hair"                         ]
            characterParameters.eyes                         = data['character']["eyes"                         ]
            characterParameters.characteristics_ws_initial   = data['character']["characteristics_ws_initial"   ]
            characterParameters.characteristics_bs_initial   = data['character']["characteristics_bs_initial"   ]
            characterParameters.characteristics_s_initial    = data['character']["characteristics_s_initial"    ]
            characterParameters.characteristics_t_initial    = data['character']["characteristics_t_initial"    ]
            characterParameters.characteristics_i_initial    = data['character']["characteristics_i_initial"    ]
            characterParameters.characteristics_ag_initial   = data['character']["characteristics_ag_initial"   ]
            characterParameters.characteristics_dex_initial  = data['character']["characteristics_dex_initial"  ]
            characterParameters.characteristics_int_initial  = data['character']["characteristics_int_initial"  ]
            characterParameters.characteristics_wp_initial   = data['character']["characteristics_wp_initial"   ]
            characterParameters.characteristics_fel_initial  = data['character']["characteristics_fel_initial"  ]
            characterParameters.careers_advance_scheme_ws_initial   = data['careers_advance_scheme']["characteristics_ws_initial"   ]
            characterParameters.careers_advance_scheme_bs_initial   = data['careers_advance_scheme']["characteristics_bs_initial"   ]
            characterParameters.careers_advance_scheme_s_initial    = data['careers_advance_scheme']["characteristics_s_initial"    ]
            characterParameters.careers_advance_scheme_t_initial    = data['careers_advance_scheme']["characteristics_t_initial"    ]
            characterParameters.careers_advance_scheme_i_initial    = data['careers_advance_scheme']["characteristics_i_initial"    ]
            characterParameters.careers_advance_scheme_ag_initial   = data['careers_advance_scheme']["characteristics_ag_initial"   ]
            characterParameters.careers_advance_scheme_dex_initial  = data['careers_advance_scheme']["characteristics_dex_initial"  ]
            characterParameters.careers_advance_scheme_int_initial  = data['careers_advance_scheme']["characteristics_int_initial"  ]
            characterParameters.careers_advance_scheme_wp_initial   = data['careers_advance_scheme']["characteristics_wp_initial"   ]
            characterParameters.careers_advance_scheme_fel_initial  = data['careers_advance_scheme']["characteristics_fel_initial"  ]
            characterParameters.characteristics_ws_advances  = data['character']["characteristics_ws_advances"  ]
            characterParameters.characteristics_bs_advances  = data['character']["characteristics_bs_advances"  ]
            characterParameters.characteristics_s_advances   = data['character']["characteristics_s_advances"   ]
            characterParameters.characteristics_t_advances   = data['character']["characteristics_t_advances"   ]
            characterParameters.characteristics_i_advances   = data['character']["characteristics_i_advances"   ]
            characterParameters.characteristics_ag_advances  = data['character']["characteristics_ag_advances"  ]
            characterParameters.characteristics_dex_advances = data['character']["characteristics_dex_advances" ]
            characterParameters.characteristics_int_advances = data['character']["characteristics_int_advances" ]
            characterParameters.characteristics_wp_advances  = data['character']["characteristics_wp_advances"  ]
            characterParameters.characteristics_fel_advances = data['character']["characteristics_fel_advances" ]
            characterParameters.wounds                       = data['character']["wounds"                       ]
            characterParameters.fate_fate                    = data['character']["fate_fate"                    ]
            characterParameters.fate_fortune                 = data['character']["fate_fortune"                 ]
            characterParameters.resilience_resilience        = data['character']["resilience_resilience"        ]
            characterParameters.resilience_resolve           = data['character']["resilience_resolve"           ]
            characterParameters.resilience_motivation        = data['character']["resilience_motivation"        ]
            characterParameters.experience_current           = data['character']["experience_current"           ]
            characterParameters.experience_spent             = data['character']["experience_spent"             ]
            characterParameters.movement_movement            = data['character']["movement_movement"            ]
            characterParameters.movement_walk                = data['character']["movement_walk"                ]
            characterParameters.movement_run                 = data['character']["movement_run"                 ]
            characterParameters.wealth                       = data['character']["wealth"                       ]

            $("td#party_name").text(data['party']['name'])
            for(m in data['party']['members']) {
                $("td#party_members ul").append("<li>"+data['party']['members'][m]+"</li>")
            }
            for(a in data['party']['ambitions']['short_term']) {
                ambition = data['party']['ambitions']['short_term'][a]
                if(ambition.achieved)
                    $("td#party_ambitions_short_term ul").append("<li class='cross_out'>"+ambition.description+"</li>")
                else
                    $("td#party_ambitions_short_term ul").append("<li>"+ambition.description+"</li>")
            }
            for(a in data['party']['ambitions']['long_term']) {
                ambition = data['party']['ambitions']['long_term'][a]
                if(ambition.achieved)
                    $("td#party_ambitions_long_term ul").append("<li class='cross_out'>"+ambition.description+"</li>")
                else
                    $("td#party_ambitions_long_term ul").append("<li>"+ambition.description+"</li>")
            }

            for(let a in data['character']['ambitions_shortterm'] ) {
                characterParameters.append_ambitions_shortterm(data['character']['ambitions_shortterm'][a]);
            }
            for(let a in data['character']['ambitions_longterm'] ) {
                characterParameters.append_ambitions_longterm(data['character']['ambitions_longterm'][a]);
            }

            for(let k in data['skills'] ) {
                characterParameters.appendSkill(data['skills'][k])
            };
            characterParameters.updateSkillTable();

            for(let k in data['trappings'] ) {
                characterParameters.appendTrappings(data['trappings'][k])
            };
            characterParameters.updateTrappingsTable()

            for(let k in data['talents'] ) {
                characterParameters.appendTalent(data['talents'][k])
            };
            characterParameters.updateTalentsTable()
            characterParameters.updateWounds();
            data['armour'].forEach(element => {
                characterParameters.appendArmour(element)
            });
            data['spells'].forEach(element => {
                characterParameters.appendSpells(element)
            });
            data['weapon'].forEach(element => {
                characterParameters.appendWeapon(element)
            });

            data['notes'].forEach(element => {
                characterParameters.appendNote(element)
            });

            $("input").prop("readonly", true);
            $("select").prop("readonly", true);
            characterParameters.updateEncumbrance();
            turon_on_edit();
            $("input[type='checkbox'].armour_put_on").on("change", put_on_armour);
        }
    });
}
function updateCharacteristicsAdv() {
    var characteristics_id = $(this).attr('id');
    var characteristics_adv_val = parseInt($(this).val());
    console.log("updateCharacteristicsAdv: " + characteristics_id + ":"+ characteristics_adv_val)
    characterParameters.updateCharacterAdvVal(characteristics_id, characteristics_adv_val);
}
function updateCharacteristicsInitial() {
    var characteristics_id = $(this).attr('id');
    var characteristics_initial_val = parseInt($(this).val());
    console.log("updateCharacteristicsInitial: " + characteristics_id + ":"+ characteristics_initial_val)
    characterParameters.updateCharacterInitialVal(characteristics_id, characteristics_initial_val);
}
function updateSkill() {
    var skill_id = $(this).attr('skill_id');
    var skill_adv_val = parseInt($(this).val());
    // console.log("updateSkill: " + skill_id +":"+ skill_adv_val)
    characterParameters.updateSkillVal(skill_id, skill_adv_val)
}
function updateTalents() {
    var id = $(this).attr('talent_id');
    var adv_val = parseInt($(this).val());
    // console.log("updateSkill: " + skill_id +":"+ skill_adv_val)
    characterParameters.updateTalentVal(id, adv_val)
}
function updateFate_fate() {
    var val = parseInt($(this).val());
    console.log("updateFate_fate: val="+val)
    characterParameters.fate_fate = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveFate",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            fate_fate    : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateFate_fortune() {
    var val = parseInt($(this).val());
    console.log("updateFate_fortune: val="+val)
    characterParameters.fate_fortune = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveFortune",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            fate_fortune : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateResilience_resilience() {
    var val = parseInt($(this).val());
    console.log("updateResilience_resilience: val="+val)
    characterParameters.resilience_resilience = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveResilience",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            resilience_resilience : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateResilience_resolve() {
    var val = parseInt($(this).val());
    console.log("updateResilience_resolve: val="+val)
    characterParameters.resilience_resolve = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveResolve",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            resilience_resolve : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateResilience_motivation () {
    var val = $(this).val();
    console.log("updateResilience_motivation: val="+val)
    characterParameters.resilience_motivation = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveMotivation",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            resilience_motivation : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateExperience_current() {
    var val = parseInt($(this).val());
    console.log("updateExperience_current: val="+val)
    characterParameters.experience_current = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveExperience_current",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            experience_current : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateExperience_spent() {
    var val = parseInt($(this).val());
    console.log("updateExperience_spent: val="+val)
    characterParameters.experience_spent = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveExperience_spent",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            experience_spent : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateCharacter_sheet_name() {
    var val = $(this).val();
    console.log("updateCharacter_sheet_name: val="+val)
    characterParameters.name = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveName",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            name : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateAge() {
    var val = parseInt($(this).val());
    console.log("updateAge: val="+val)
    characterParameters.age = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveAge",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            age : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function updateHeight() {
    var val = parseInt($(this).val());
    console.log("updateHeight: val="+val)
    characterParameters.height = val;
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveHeight",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id : characterParameters.id,
            height : val
        },
        success: function(data) {
            console.log(data)
        }
    });
}
function turon_on_edit() {
    $("span.dot_not_editable").switchClass( "dot_not_editable", "dot_editable", 1000);

    $("input#characteristics_ws_initial ").addClass( "editable", 1000);
    $("input#characteristics_bs_initial ").addClass( "editable", 1000);
    $("input#characteristics_s_initial").addClass( "editable", 1000);
    $("input#characteristics_t_initial").addClass( "editable", 1000);
    $("input#characteristics_i_initial").addClass( "editable", 1000);
    $("input#characteristics_ag_initial ").addClass( "editable", 1000);
    $("input#characteristics_dex_initial").addClass( "editable", 1000);
    $("input#characteristics_int_initial").addClass( "editable", 1000);
    $("input#characteristics_wp_initial ").addClass( "editable", 1000);
    $("input#characteristics_fel_initial").addClass( "editable", 1000);
    $("input#characteristics_ws_advances ").addClass( "editable", 1000);
    $("input#characteristics_bs_advances ").addClass( "editable", 1000);
    $("input#characteristics_s_advances").addClass( "editable", 1000);
    $("input#characteristics_t_advances").addClass( "editable", 1000);
    $("input#characteristics_i_advances").addClass( "editable", 1000);
    $("input#characteristics_ag_advances ").addClass( "editable", 1000);
    $("input#characteristics_dex_advances").addClass( "editable", 1000);
    $("input#characteristics_int_advances").addClass( "editable", 1000);
    $("input#characteristics_wp_advances ").addClass( "editable", 1000);
    $("input#characteristics_fel_advances").addClass( "editable", 1000);
    $("input.skills_adv").addClass( "editable", 1000);
    $("input.talents_adv").addClass( "editable", 1000);
    $("select#add_armour").addClass( "editable", 1000);
    $("select#add_weapon").addClass( "editable", 1000);
    $("select#add_spell").addClass( "editable", 1000);
    $("select#add_talents").addClass( "editable", 1000);
    $("select#add_skills").addClass( "editable", 1000);
    $("select#add_trappings").addClass( "editable", 1000);
    $("select#species").addClass( "editable", 1000);
    $("select#class").addClass( "editable", 1000);
    $("select#career").addClass( "editable", 1000);
    $("select#hair").addClass( "editable", 1000);
    $("select#eyes").addClass( "editable", 1000);
    $("input#career_level").addClass( "editable", 1000);
    $("input#fate_fate").addClass( "editable", 1000);
    $("input#fate_fortune").addClass( "editable", 1000);
    $("input#resilience_resilience").addClass( "editable", 1000);
    $("input#resilience_resolve").addClass( "editable", 1000);
    $("input#resilience_motivation").addClass( "editable", 1000);
    $("input#wealth").addClass( "editable", 1000);
    $("input#experience_current").addClass( "editable", 1000);
    $("input#experience_spent").addClass( "editable", 1000);
    $("input#character_sheet_name").addClass( "editable", 1000);
    $("input#age").addClass( "editable", 1000);
    $("input#height").addClass( "editable", 1000);



    $("input#characteristics_ws_initial ").prop("readonly", false);
    $("input#characteristics_bs_initial ").prop("readonly", false);
    $("input#characteristics_s_initial").prop("readonly", false);
    $("input#characteristics_t_initial").prop("readonly", false);
    $("input#characteristics_i_initial").prop("readonly", false);
    $("input#characteristics_ag_initial ").prop("readonly", false);
    $("input#characteristics_dex_initial").prop("readonly", false);
    $("input#characteristics_int_initial").prop("readonly", false);
    $("input#characteristics_wp_initial ").prop("readonly", false);
    $("input#characteristics_fel_initial").prop("readonly", false);
    $("input#characteristics_ws_advances ").prop("readonly", false);
    $("input#characteristics_bs_advances ").prop("readonly", false);
    $("input#characteristics_s_advances").prop("readonly", false);
    $("input#characteristics_t_advances").prop("readonly", false);
    $("input#characteristics_i_advances").prop("readonly", false);
    $("input#characteristics_ag_advances ").prop("readonly", false);
    $("input#characteristics_dex_advances").prop("readonly", false);
    $("input#characteristics_int_advances").prop("readonly", false);
    $("input#characteristics_wp_advances ").prop("readonly", false);
    $("input#characteristics_fel_advances").prop("readonly", false);
    $("input.skills_adv").prop("readonly", false);
    $("input.talents_adv").prop("readonly", false);
    $("input.armour_put_on").prop("readonly", false);
    $("input#fate_fate").prop("readonly", false);
    $("input#fate_fortune").prop("readonly", false);
    $("input#resilience_resilience").prop("readonly", false);
    $("input#resilience_resolve").prop("readonly", false);
    $("input#resilience_motivation").prop("readonly", false);
    $("input#wealth").prop("readonly", false);
    $("input#experience_current").prop("readonly", false);
    $("input#experience_spent").prop("readonly", false);
    $("input#character_sheet_name").prop("readonly", false);
    $("input#age").prop("readonly", false);
    $("input#height").prop("readonly", false);
    $("input#career_level").prop("readonly", false);



    $("input#characteristics_ws_advances ").on("change",  updateCharacteristicsAdv);
    $("input#characteristics_bs_advances ").on("change", updateCharacteristicsAdv);
    $("input#characteristics_s_advances").on("change", updateCharacteristicsAdv);
    $("input#characteristics_t_advances").on("change", updateCharacteristicsAdv);
    $("input#characteristics_i_advances").on("change", updateCharacteristicsAdv);
    $("input#characteristics_ag_advances ").on("change", updateCharacteristicsAdv);
    $("input#characteristics_dex_advances").on("change", updateCharacteristicsAdv);
    $("input#characteristics_int_advances").on("change", updateCharacteristicsAdv);
    $("input#characteristics_wp_advances ").on("change", updateCharacteristicsAdv);
    $("input#characteristics_fel_advances").on("change", updateCharacteristicsAdv);
    $("input#characteristics_ws_initial ").on("change",  updateCharacteristicsInitial);
    $("input#characteristics_bs_initial ").on("change", updateCharacteristicsInitial);
    $("input#characteristics_s_initial").on("change", updateCharacteristicsInitial);
    $("input#characteristics_t_initial").on("change", updateCharacteristicsInitial);
    $("input#characteristics_i_initial").on("change", updateCharacteristicsInitial);
    $("input#characteristics_ag_initial ").on("change", updateCharacteristicsInitial);
    $("input#characteristics_dex_initial").on("change", updateCharacteristicsInitial);
    $("input#characteristics_int_initial").on("change", updateCharacteristicsInitial);
    $("input#characteristics_wp_initial ").on("change", updateCharacteristicsInitial);
    $("input#characteristics_fel_initial").on("change", updateCharacteristicsInitial);
    $("input.skills_adv").on("change", updateSkill);
    $("input.talents_adv").on("change", updateTalents);
    $("input#fate_fate").change(updateFate_fate)
    $("input#fate_fortune").change(updateFate_fortune)
    $("input#resilience_resilience").change(updateResilience_resilience)
    $("input#resilience_resolve").change(updateResilience_resolve)
    $("input#resilience_motivation").change(updateResilience_motivation)
    $("input#wealth").on("change", change_wealth);
    $("input#experience_current").change(updateExperience_current)
    $("input#experience_spent").change(updateExperience_spent)
    $("input#character_sheet_name").change(updateCharacter_sheet_name)
    $("input#age").change(updateAge)
    $("input#height").change(updateHeight)

    $("select#species").on("change", updateSpecies);
    $("select#class").on("change", updateClass);
    $("select#career").on("change", updateCareer);
    $("input#career_level").change(updateCareer_level);
    $("select#hair").on("change", updateHair);
    $("select#eyes").on("change", updateEyes);
}
function armour_add() {
    var armour_to_add = $("select#add_armour").val()
    console.log("armour_add: "+ armour_to_add);
    characterParameters.armour_add(armour_to_add);
    characterParameters.updateEncumbrance();
}
function weapon_add() {
    var weapon_to_add = $("select#add_weapon").val()
    console.log("add_weapon: "+ weapon_to_add);
    characterParameters.add_weapon(weapon_to_add);
    characterParameters.updateEncumbrance();
}
function spell_add() {
    var spell_to_add = $("select#add_spell").val()
    console.log("add_spell: "+ spell_to_add);
    characterParameters.add_spell(spell_to_add);
    characterParameters.updateEncumbrance();
}
function talent_add() {
    var talent_to_add = $("select#add_talents").val()
    console.log("add_talent: "+ talent_to_add);
    characterParameters.add_talent(talent_to_add);
    characterParameters.updateTalentsTable();
}
function trappings_add() {
    var trappings_to_add = $("select#add_trappings").val()
    console.log("trappings_add: "+ trappings_to_add);
    characterParameters.add_trappings(trappings_to_add);
}
function put_on_armour() {
    console.log("put_on_armour: id:"+$(this).attr('armour_id') + " checked="+$(this).prop('checked'))
    characterParameters.put_on_armour($(this).attr('armour_id'), $(this).prop('checked'));
}
function close_ambition() {
    var ambition_id = $(this).attr("close_ambitions_id")
    console.log("close_ambition:"+ ambition_id)
    characterParameters.updateAmbition(ambition_id, true)
    characterParameters.save_currentXP()
}
function delete_ambition() {
    var ambition_id = $(this).attr("delete_ambitions_id")
    console.log("delete_ambition:"+ ambition_id)
    characterParameters.deleteAmbition(ambition_id);
}
function ambitions_add() {
    $("div#main div.character_sheet div.ambitions table tr td.add").show(500)
    $("div#main div.character_sheet div.ambitions table tr td.add input").prop("readonly", false)
    $("div#main div.character_sheet div.ambitions table tr td.add input").off("click").click(function() {
        let ambitions_description = $("div#main div.character_sheet div.ambitions table tr td.add textarea#ambitions").val();
        if(ambitions_description.length == 0) {
            alert("no ambition")
            return
        }

        let target = $("div#main div.character_sheet div.ambitions table tr td.add input").attr("target")
        console.log(ambitions_description)
        let ambitions_to_append =  {
            'id': 0,
            'description': ambitions_description,
            'achieved': false
        }
        let ambition
        if(target == "shortterm") {
            ambition = characterParameters.append_ambitions_shortterm(ambitions_to_append)
        } else if(target == "longterm") {
            ambition = characterParameters.append_ambitions_longterm(ambitions_to_append)
        }
        ambition.save()
        ambition.updateUI()
        $("div#main div.character_sheet div.ambitions table tr td.add").hide(500)
    });
}
function ambitions_shortterm_add() {
    ambitions_add()
    $("div#main div.character_sheet div.ambitions table tr td.add input").attr("target", "shortterm")
}
function ambitions_longterm_add() {
    ambitions_add()
    $("div#main div.character_sheet div.ambitions table tr td.add input").attr("target", "longterm")
}
function note_add() {
    let n = tinyMCE.get('player_notes_textarea').getContent();
    let note = {
        "id": 0,
        "datetime_create": "",
        "timestamp": 0,
        "note_text": n
    }
    new_note = characterParameters.saveNote(note);
}
function change_wealth() {
    var wealth = $("input#wealth").val()
    characterParameters.save_wealth(wealth)
}
function get_fullSkillList() {
    console.log("get_characterData")

    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_fullSkillList",
        data: {
            character_id: character_id,
        },
        success: function(data) {
            console.log(data);
            for(let k in data['skills']) {
                $("select#add_skills").append($('<option>', {value: data['skills'][k]['id'], text: data['skills'][k]['name'] }));
            };

        }
    });
}
function get_fullSpeciesList() {
    console.log("get_fullSpeciesList")

    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_getSpeciesList",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: character_id,
        },
        success: function(data) {
            console.log(data);
            for(let k in data['species']) {
                $("select#species").append($('<option>', {value: data['species'][k]['id'], text: data['species'][k]['name'] }));
            };

        }
    });
}
function get_fullClassList() {
    console.log("get_fullClassList")

    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_getClassList",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: character_id,
        },
        success: function(data) {
            console.log(data);
            characterParameters.classModel = data['character_class']
            console.log("get_fullClassList:")
            console.log(data)
            for(let k in data['character_class']) {
                $("select#class").append($('<option>', {value: data['character_class'][k]['id'], text: data['character_class'][k]['name'] }));
            };
        }
    });

}
function get_fullHairList() {
    console.log("get_fullHairList")

    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_getHairList",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: character_id,
        },
        success: function(data) {
            console.log(data);
            for(let k in data['hair']) {
                $("select#hair").append($('<option>', {value: data['hair'][k]['id'], text: data['hair'][k]['name'] }));
            };
        }
    });
}
function get_fullEyesList() {
    console.log("get_fullEyesList")

    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_getEyesList",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: character_id,
        },
        success: function(data) {
            console.log(data);
            for(let k in data['eyes']) {
                $("select#eyes").append($('<option>', {value: data['eyes'][k]['id'], text: data['eyes'][k]['name'] }));
            };
        }
    });
}
function skill_add() {
    var add_skills = $("select#add_skills").val()
    console.log("add_skills: "+ add_skills);
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveSkill2Character",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: characterParameters.id,
            skill_id: add_skills,
        },
        success: function(data) {
            console.log(data);
            if(data['crated']) {
                characterParameters.appendSkill(data['skill'])
                characterParameters.updateSkillTable();
            } else {
                console.log('skill: \"'+data['skill']['name']+'\" already exists')
            }

        }
    });
}
function updateSpecies(){
    var val = $(this).val()
    console.log("updateSpecies: "+ val);
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveSpecies",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: characterParameters.id,
            species_id: val,
        },
        success: function(data) {
            console.log(data);
            characterParameters.species_id = data['species_id']
        }
    });
}
function updateClass(){
    $("select#class").off("change", updateClass);
    $("select#career").off("change", updateCareer);
    var val = $(this).val()
    console.log("updateClass: "+ val);
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveClass",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: characterParameters.id,
            class_id: val,
        },
        success: function(data) {
            console.log(data);
            characterParameters.ch_class_id = data['class_id']
            $("select#class").on("change", updateClass);
            $("select#career").on("change", updateCareer);
            alert("Update Career")
        }
    });
}
function updateCareer(){
    $("select#class").off("change", updateClass);
    $("select#career").off("change", updateCareer);
    var val = $(this).val()
    console.log("updateCareer: "+ val);
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveCareer",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: characterParameters.id,
            career_id: val,
        },
        success: function(data) {
            console.log(data);
            characterParameters.career_id = data['career_id']
            $("select#class").on("change", updateClass);
            $("select#career").on("change", updateCareer);
        }
    });
}
function updateCareer_level() {
    var val = $(this).val()
    console.log("updateCareer_level: "+ val);
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveCareer_level",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: characterParameters.id,
            career_level: val,
        },
        success: function(data) {
            console.log(data);
            characterParameters.career_level = parseInt(data['career_level'])
        }
    });
}
function updateHair() {
    var val = $(this).val()
    console.log("updateHair: "+ val);
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveHair",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: characterParameters.id,
            hair: val,
        },
        success: function(data) {
            console.log(data);
        }
    });
}
function updateEyes() {
    var val = $(this).val()
    console.log("updateEyes: "+ val);
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveEyes",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            character_id: characterParameters.id,
            eyes: val,
        },
        success: function(data) {
            console.log(data);
        }
    });
}
function main() {

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    character_id = $("input[name='character_id']").val()


    get_characterData();

    $("input").prop("readonly", true);
    $("select").prop("readonly", true);

    $("span.dot_not_editable").click(turon_on_edit);

    $("button#armour_add_button").click(armour_add);
    $("button#weapon_add_button").click(weapon_add);
    $("button#spells_add_button").click(spell_add);
    $("button#talents_add_button").click(talent_add);
    $("button#trappings_add_button").click(trappings_add);
    $("button#skills_add_button").click(skill_add);
    $("button#player_notes_add_button").click(note_add);
    $("input[type='checkbox'].armour_put_on").on("change", put_on_armour);
    $("img#ambitions_shortterm_add").click(ambitions_shortterm_add);
    $("img#ambitions_longterm_add").click(ambitions_longterm_add);
}
