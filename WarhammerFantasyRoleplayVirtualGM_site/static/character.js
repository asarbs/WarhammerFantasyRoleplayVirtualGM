
var character_creation_state = {
    bonus_xp: 0,
    character_creation_step: 0,
    class_selection_random: 0,
}



const character_creation_steps = ["step_1_species", "step_2_class"]

function species_change() {
    val = $(this).find(":selected").val()
    characer_id = $("input[name='characer_id']").val()

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $.ajax({
        type: "POST",
        url: "ajax_save_character_species",
        data: {
            characer_id: characer_id,
            species_id: val
        },
        success: function(data) {
            $("select#species").val(data['species_id']);
            character_creation_state['bonus_xp'] = 0;
        }
    });

}

function randomSpecies() {
    console.log("randomSpecies")
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    characer_id = $("input[name='characer_id']").val()

    $.ajax({
        type: "POST",
        url: "ajax_randomSpecies",
        data: {
            characer_id: characer_id,
        },
        success: function(data) {
            val = $("select#species").val();
            console.log("status: " + data['status'] + "; species_id: " + val + " -> " + data['species_id']);
            $("select#species").val(data['species_id']);
            character_creation_state['bonus_xp'] = 20;
            $("input#character_sheet_name").val(data['name'])
            $("input#character_sheet_name_1").val(data['name'])
        }
    });
}

function updateBonusExperiencePoints() {
    $("span#BonusExperiencePoints").text(character_creation_state['bonus_xp']);
}


function nextStep() {
    console.log("div#"+ character_creation_steps[character_creation_state['character_creation_step']]);
    $("div#"+ character_creation_steps[character_creation_state['character_creation_step']]).hide(200);
    character_creation_state['character_creation_step']++
    $("div#"+ character_creation_steps[character_creation_state['character_creation_step']]).show(200);
}

function randomClass() {
    if(character_creation_state['class_selection_random'] == 0) {
        character_creation_state['bonus_xp'] += 50
        character_creation_state['class_selection_random']++
        $("li#create_character_steps_li_1").css({'font-weight': 'bold'});

    }
    else if(character_creation_state['class_selection_random'] == 1) {
        character_creation_state['bonus_xp'] -= 50
        character_creation_state['bonus_xp'] += 25
        character_creation_state['class_selection_random']++
        $("li#create_character_steps_li_2").css({'font-weight': 'bold'});
    }
    else if(character_creation_state['class_selection_random'] == 2) {
        character_creation_state['bonus_xp'] -= 25
        character_creation_state['bonus_xp'] += 0
        character_creation_state['class_selection_random'] = 3
        $("li#create_character_steps_li_3").css({'font-weight': 'bold'});
    }

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_randomClass",
        data: {
            characer_id: characer_id,
        },
        success: function(data) {
            $("input#carrer").val(data['career_name']);
            $("input#class").val(data['ch_class_name']);
            $("li#create_character_steps_li_"+character_creation_state['class_selection_random']+" p:first").text( data['ch_class_name']+ " / " + data['career_name'])
        }
    });
}

function saveName(e) {
    n = $("input#character_sheet_name_1").val();
    $("input#character_sheet_name").val(n)

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

function main() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $("select[name='species']").on("change", species_change);
    $("img#img_random_species").click(randomSpecies);

    $("img#img_character_creaton_next").click(nextStep);
    $("div#"+ character_creation_steps[0]).show();
    $("img#img_random_class").click(randomClass);
    $("input#character_sheet_name_1").keyup(saveName);

    setInterval(updateBonusExperiencePoints, 100);
}
