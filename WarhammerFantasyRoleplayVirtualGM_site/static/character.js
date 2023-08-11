
var character_creation_state = {
    bonus_xp: 0,

    characteristics_ws_initial     : 0,
    characteristics_bs_initial     : 0,
    characteristics_s_initial      : 0,
    characteristics_t_initial      : 0,
    characteristics_i_initial      : 0,
    characteristics_ag_initial     : 0,
    characteristics_dex_initial    : 0,
    characteristics_int_initial    : 0,
    characteristics_wp_initial     : 0,
    characteristics_fel_initial    : 0,
    characteristics_ws_advances    : 0,
    characteristics_bs_advances    : 0,
    characteristics_s_advances     : 0,
    characteristics_t_advances     : 0,
    characteristics_i_advances     : 0,
    characteristics_ag_advances    : 0,
    characteristics_dex_advances   : 0,
    characteristics_int_advances   : 0,
    characteristics_wp_advances    : 0,
    characteristics_fel_advances   : 0,

    character_creation_step: 0,
    class_selection_random: 0,
}



const character_creation_steps = ["step_1_species", "step_2_class", "step_3_characteristics"]
const character_creation_steps_header = ["Species", "Class", "Characteristics"]

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
    $("input#experience_current").val(character_creation_state['bonus_xp']);

    $("input#characteristics_ws_initial"  ).val(character_creation_state["characteristics_ws_initial" ])
    $("input#characteristics_bs_initial"  ).val(character_creation_state["characteristics_bs_initial" ])
    $("input#characteristics_s_initial"   ).val(character_creation_state["characteristics_s_initial"  ])
    $("input#characteristics_t_initial"   ).val(character_creation_state["characteristics_t_initial"  ])
    $("input#characteristics_i_initial"   ).val(character_creation_state["characteristics_i_initial"  ])
    $("input#characteristics_ag_initial"  ).val(character_creation_state["characteristics_ag_initial" ])
    $("input#characteristics_dex_initial" ).val(character_creation_state["characteristics_dex_initial"])
    $("input#characteristics_int_initial" ).val(character_creation_state["characteristics_int_initial"])
    $("input#characteristics_wp_initial"  ).val(character_creation_state["characteristics_wp_initial" ])
    $("input#characteristics_fel_initial" ).val(character_creation_state["characteristics_fel_initial"])

    $("input#characteristics_ws_advances"  ).val(character_creation_state["characteristics_ws_advances" ])
    $("input#characteristics_bs_advances"  ).val(character_creation_state["characteristics_bs_advances" ])
    $("input#characteristics_s_advances"   ).val(character_creation_state["characteristics_s_advances"  ])
    $("input#characteristics_t_advances"   ).val(character_creation_state["characteristics_t_advances"  ])
    $("input#characteristics_i_advances"   ).val(character_creation_state["characteristics_i_advances"  ])
    $("input#characteristics_ag_advances"  ).val(character_creation_state["characteristics_ag_advances" ])
    $("input#characteristics_dex_advances" ).val(character_creation_state["characteristics_dex_advances"])
    $("input#characteristics_int_advances" ).val(character_creation_state["characteristics_int_advances"])
    $("input#characteristics_wp_advances"  ).val(character_creation_state["characteristics_wp_advances" ])
    $("input#characteristics_fel_advances" ).val(character_creation_state["characteristics_fel_advances"])

    $("input#characteristics_ws_current"  ).val(character_creation_state["characteristics_ws_initial" ] + character_creation_state["characteristics_ws_advances" ] )
    $("input#characteristics_bs_current"  ).val(character_creation_state["characteristics_bs_initial" ] + character_creation_state["characteristics_bs_advances" ] )
    $("input#characteristics_s_current"   ).val(character_creation_state["characteristics_s_initial"  ] + character_creation_state["characteristics_s_advances"  ] )
    $("input#characteristics_t_current"   ).val(character_creation_state["characteristics_t_initial"  ] + character_creation_state["characteristics_t_advances"  ] )
    $("input#characteristics_i_current"   ).val(character_creation_state["characteristics_i_initial"  ] + character_creation_state["characteristics_i_advances"  ] )
    $("input#characteristics_ag_current"  ).val(character_creation_state["characteristics_ag_initial" ] + character_creation_state["characteristics_ag_advances" ] )
    $("input#characteristics_dex_current" ).val(character_creation_state["characteristics_dex_initial"] + character_creation_state["characteristics_dex_advances"] )
    $("input#characteristics_int_current" ).val(character_creation_state["characteristics_int_initial"] + character_creation_state["characteristics_int_advances"] )
    $("input#characteristics_wp_current"  ).val(character_creation_state["characteristics_wp_initial" ] + character_creation_state["characteristics_wp_advances" ] )
    $("input#characteristics_fel_current" ).val(character_creation_state["characteristics_fel_initial"] + character_creation_state["characteristics_fel_advances"] )
}


function nextStep() {
    console.log("div#"+ character_creation_steps[character_creation_state['character_creation_step']]);
    $("div#"+ character_creation_steps[character_creation_state['character_creation_step']]).hide(200);
    character_creation_state['character_creation_step']++
    $("div#"+ character_creation_steps[character_creation_state['character_creation_step']]).show(200);
    $("div.create_character div.header h1").text(character_creation_steps_header[character_creation_state['character_creation_step']])
}

function randomClass() {
    if(character_creation_state['class_selection_random'] == 0) {
        character_creation_state['bonus_xp'] += 50
        character_creation_state['class_selection_random']++
    }
    else if(character_creation_state['class_selection_random'] == 1) {
        character_creation_state['bonus_xp'] -= 50
        character_creation_state['bonus_xp'] += 25
        character_creation_state['class_selection_random']++
    }
    else if(character_creation_state['class_selection_random'] == 2) {
        character_creation_state['bonus_xp'] -= 25
        character_creation_state['bonus_xp'] += 0
        character_creation_state['class_selection_random'] = 3
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
        }
    });
}

function saveName(e) {
    n = $("input#character_sheet_name").val();

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

function attributes() {
    console.log("attributes")

    characer_id = $("input[name='characer_id']").val()
    $.ajax({
        type: "POST",
        url: "ajax_saveAttributes",
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
    $("img#img_character_creaton_next").click(nextStep);

    $("img#img_random_species").click(randomSpecies);
    $("div#"+ character_creation_steps[0]).show();
    $("img#img_random_class").click(randomClass);
    $("input#character_sheet_name").keyup(saveName);
    $("img#img_random_characteristics").click(attributes);

    setInterval(updateBonusExperiencePoints, 100);
}
