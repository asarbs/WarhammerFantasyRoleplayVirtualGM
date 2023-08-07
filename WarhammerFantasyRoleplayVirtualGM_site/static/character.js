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
            alert("status: " + data['status']);
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
        }
    });
}


function main() {
    $("select[name='species']").on("change", species_change);
    $("img#img_random_species").click(randomSpecies);

}
