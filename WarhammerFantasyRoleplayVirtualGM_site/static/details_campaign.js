function submit_ambitions_shortterm() {
    let ambitions_description = $("textarea#ambitions_shortterm").val();
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveCampaignAmbitions",
        data: {
            camaing_id : camaing_id,
            is_shortterm : "true",
            ambitions_id : 0,
            achieved: "false",
            description : ambitions_description
        },
        success: function(data) {
            console.log("submit_ambitions_shortterm data="+data)
            $("ol#list_ambitions_shortterm").append("<li ambition_id="+data['id']+">"+data['description']+"<img src=\"/static/img/tick.png\" ambition_id="+data['id']+"></li>")
            $("ol#list_ambitions_shortterm li img[ambition_id='"+data['id']+"']").click(aa);
        }
    });
}
function submit_ambitions_longterm() {
    let ambitions_description = $("textarea#ambitions_longterm").val();
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveCampaignAmbitions",
        data: {
            camaing_id : camaing_id,
            is_shortterm : "false",
            ambitions_id : 0,
            achieved: "false",
            description : ambitions_description
        },
        success: function(data) {
            console.log("submit_ambitions_longterm data="+data)
            $("ol#list_ambitions_longterm").append("<li ambition_id="+data['id']+">"+data['description']+"<img src=\"/static/img/tick.png\" ambition_id="+data['id']+"></li>")
            $("ol#list_ambitions_longterm li img[ambition_id='"+data['id']+"']").click(aa);
        }
    });
}
function update_ambitions_shortterm() {
    let id = $(this).attr("ambition_id")
    let ambitions_description = $("ol#list_ambitions_shortterm li[ambition_id='"+id+"']").val();
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveCampaignAmbitions",
        data: {
            camaing_id : camaing_id,
            is_shortterm : "true",
            ambitions_id : id,
            achieved: "true",
            description : ambitions_description
        },
        success: function(data) {
            console.log("submit_ambitions_longterm data="+data)
            $("ol#list_ambitions_shortterm li[ambition_id='"+data['id']+"']").addClass( "cross_out", 500);
            $("ol#list_ambitions_shortterm liimg[ambition_id='"+data['id']+"']").remove()
        }
    });

}
function update_ambitions_longterm() {
    let id = $(this).attr("ambition_id")
    let ambitions_description = $("ol#list_ambitions_longterm li[ambition_id='"+id+"']").val();
    $.ajax({
        type: "POST",
        url: "/wfrpg_gm/ajax_saveCampaignAmbitions",
        data: {
            camaing_id : camaing_id,
            is_shortterm : "false",
            ambitions_id : id,
            achieved: "true",
            description : ambitions_description
        },
        success: function(data) {
            console.log("submit_ambitions_longterm data="+data)
            $("ol#list_ambitions_longterm li[ambition_id='"+data['id']+"']").addClass( "cross_out", 500);
            $("ol#list_ambitions_longterm liimg[ambition_id='"+data['id']+"']").remove()
        }
    });
}

var camaing_id = 0

function main() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    camaing_id = $("input[name='camaing_id']").val()
    $("input#submit_ambitions_shortterm").click(submit_ambitions_shortterm);
    $("input#submit_ambitions_longterm").click(submit_ambitions_longterm);
    $("ol#list_ambitions_shortterm li img").click(update_ambitions_shortterm);
    $("ol#list_ambitions_longterm li img").click(update_ambitions_longterm);
}