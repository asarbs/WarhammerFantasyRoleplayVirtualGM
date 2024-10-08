
function get_skill_description() {
    var skill_id = $(this).attr("skill_id")
    $.ajax({
        type: "POST",
        url: "/wfrpg_npc/ajax_npc_get_skill_description",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            skill_id: skill_id,
        },
        success: function(data) {
            console.log(data);
            desc = "<h2>"+data['skill']['name']+"</h2>"
            desc += "<b>Characteristic:</b> <span>"+data['skill']['characteristics']+"</span>"
            desc += "<span>"+data['skill']['description']+"</span>"
            desc += "<span class=\"ref\">"+data['skill']['ref']+"</span>"
            document.getElementById('detailsMsg').innerHTML = desc
            document.getElementById('detailsMsg_container').style.display = "block";

        }
    });
}
function get_talent_description() {
    var talent_id = $(this).attr("talent_id")
    $.ajax({
        type: "POST",
        url: "/wfrpg_npc/ajax_npc_get_talent_description",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            talent_id: talent_id,
        },
        success: function(data) {
            console.log(data);
            desc = "<h2>"+data['talent']['name']+"</h2>"
            desc += "<b>Test:</b><span>"+data['talent']['tests']+"</span>"
            desc += "<span>"+data['talent']['description']+"</span>"
            desc += "<span class=\"ref\">"+data['talent']['ref']+"</span>"
            document.getElementById('detailsMsg').innerHTML = desc
            document.getElementById('detailsMsg_container').style.display = "block";

        }
    });
}
function get_trapping_description() {
    var trapping_id = $(this).attr("trapping_id")
    $.ajax({
        type: "POST",
        url: "/wfrpg_npc/ajax_npc_get_trapping_description",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            trapping_id: trapping_id,
        },
        success: function(data) {
            console.log(data);
            desc = "<h2>"+data['trapping']['name']+"</h2>"
            desc += "<span>"+data['trapping']['description']+"</span>"
            document.getElementById('detailsMsg').innerHTML = desc
            document.getElementById('detailsMsg_container').style.display = "block";

        }
    });
}
function get_creatureTraits_description() {
    var creatureTraits_id = $(this).attr("creatureTraits_id")

    $.ajax({
        type: "POST",
        url: "/wfrpg_npc/ajax_npc_get_creatureTraits_description",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            creatureTraits_id: creatureTraits_id,
        },
        success: function(data) {
            console.log(data);
            desc = "<h2>"+data['trait']['name']+"</h2>"
            desc += "<span>"+data['trait']['description']+"</span>"
            desc += "<span class=\"ref\">"+data['trait']['ref']+"</span>"
            document.getElementById('detailsMsg').innerHTML = desc
            document.getElementById('detailsMsg_container').style.display = "block";

        }
    });
}
function get_spells_description() {
    var spell_id = $(this).attr("spell_id")

    $.ajax({
        type: "POST",
        url: "/wfrpg_npc/ajax_npc_get_spell_description",
        async: false,
        cache: false,
        timeout: 30000,
        fail: function(){
            return true;
        },
        data: {
            spell_id: spell_id,
        },
        success: function(data) {
            console.log(data);
            desc = "<h2>"+data['spell']['name']+"</h2>"
            desc += "<p><b>Spell List:</b><span>"+data['spell']['spellLists']+"</span></p>"
            desc += "<p><b>CN:</b><span>"+data['spell']['cn']+"</span></p>"
            desc += "<p><b>Range:</b><span>"+data['spell']['range']+"</span></p>"
            desc += "<p><b>Target:</b><span>"+data['spell']['target']+"</span></p>"
            desc += "<p><b>Duration:</b><span>"+data['spell']['duration']+"</span></p>"
            desc += "<p><b>Effect:</b><span>"+data['spell']['effect']+"</span></p>"
            document.getElementById('detailsMsg').innerHTML = desc
            document.getElementById('detailsMsg_container').style.display = "block";

        }
    });
}
function close_detailsMsg() {
    document.getElementById('detailsMsg_container').style.display = "none";
}

function note_add() {
    let n = tinyMCE.get('adventure_notes_textarea').getContent();
    let adventure_id = window.location.pathname.split("/")[3]
    $.ajax({
        type: "POST",
        url: "/Adventure/ajax_saveAdventureNotes",
        data: {
            adventure_id : adventure_id,
            note_text : n,
        },
        success: function(data) {
            console.log("note_add data="+data)
            if(!$('td#camaing_notes_timestamp__'+data['timestamp']).length) {
                var new_row = '<tr class="note_line">'
                new_row += '<td id="camaing_notes_timestamp__'+data['timestamp']+'" class="date">'+data['datetime_create']+'</td>'
                new_row += '<td>'+data['author']+'</td>'
                new_row += '<td>'+n+'</td>'
                new_row += '</tr>'
                $("table#campaign_notes tr.block_header").after(new_row)
            } else {
                console.log("NOT Note.updateUI: "+ this.datetime_create);
            }
        }
    });
}

function condition_save() {
    var condition_id = $(this).attr("condition_id")
    var adventure_id = $(this).attr("adventure_id")
    var npc_id = $(this).attr("npc_id")
    var adv2npc_id = $(this).attr("adv2npc_id")
    var checked = $(this).is(":checked")
    console.log("condition_id:"+condition_id+"; adventure_id="+adventure_id+"; npc_id="+npc_id+ "; adv2npc_id=" + adv2npc_id +"; checked="+checked)

    $.ajax({
        type: "POST",
        url: "/Adventure/ajax_saveConditionState",
        data: {
            adventure_id : adventure_id,
            condition_id: condition_id,
            npc_id: npc_id,
            adv2npc_id: adv2npc_id,
            checked : checked,
        },
        success: function(data) {

        }
    });
}

function current_wounds_save() {
    var adv2npc_id = $(this).attr("adv2npc_id")
    var current_wounds = $(this).val()
    console.log("adv2npc_id=" + adv2npc_id +"; current_wounds="+current_wounds)

    $.ajax({
        type: "POST",
        url: "/Adventure/ajax_saveCurrentWounds",
        data: {
            adv2npc_id: adv2npc_id,
            current_wounds : current_wounds,
        },
        success: function(data) {
            console.log(data)
        }
    });
}

const conditions = new Array();

function getConditionsDetails() {
    $.ajax({
        type: "POST",
        url: "/Adventure/ajax_getConditionsDetails",
        data: {},
        success: function(data) {
            console.log(data['status'])
            data['conditions'].forEach((element) => {
                conditions.push(element);
            });
        }
    });

}

function condition_help() {
    var condition_id = $(this).attr("condition_id")

    conditions.forEach( (element) => {
        if(element.id == condition_id) {
            desc = "<h2>"+element.name+"</h2>"
            desc += "<p><span>"+element.description+"</p>"
            document.getElementById('detailsMsg').innerHTML = desc
            document.getElementById('detailsMsg_container').style.display = "block";
        }
    });

}

function main() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $("span.npc_skill").click(get_skill_description);
    $("span.npc_talent").click(get_talent_description);
    $("span.npc_trapping").click(get_trapping_description);
    $("span.npc_creatureTraits").click(get_creatureTraits_description);
    $("span.npc_spells").click(get_spells_description);
    $("div#detailsMsg_ok").click(close_detailsMsg);
    $("button#adventure_notes_add_button").click(note_add);
    $("input.conditions").click(condition_save);
    $("label.conditions").click(condition_help);
    $("input.npc_characteristics_w").on("change", current_wounds_save);
    getConditionsDetails();


    // console.log(' href => ' + window.location.href);
    // console.log(' host => ' + window.location.host);
    // console.log(' hostname => ' + window.location.hostname);
    // console.log(' port => ' + window.location.port);
    // console.log(' protocol => ' + window.location.protocol);
    // console.log(' pathname => ' + window.location.pathname);
    // console.log(' hashpathname => ' + window.location.hash);
    // console.log(' search=> ' + window.location.search);
}