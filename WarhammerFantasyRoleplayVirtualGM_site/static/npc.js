
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
            desc += "<span>"+data['skill']['ref']+"</span>"
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
            desc += "<span>"+data['talent']['ref']+"</span>"
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
            desc += "<span>"+data['trait']['ref']+"</span>"
            document.getElementById('detailsMsg').innerHTML = desc
            document.getElementById('detailsMsg_container').style.display = "block";

        }
    });
}
function close_detailsMsg() {
    document.getElementById('detailsMsg_container').style.display = "none";
}
function main() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $("span.npc_skill").click(get_skill_description);
    $("span.npc_talent").click(get_talent_description);
    $("span.npc_trapping").click(get_trapping_description);
    $("span.npc_creatureTraits").click(get_creatureTraits_description);
    $("div#detailsMsg_ok").click(close_detailsMsg);
}