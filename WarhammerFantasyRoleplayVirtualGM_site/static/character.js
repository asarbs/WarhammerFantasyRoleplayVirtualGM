function species_change() {
    alert("The text has been changed.");
}

function main() {
    alert("main");
    $('species').change(species_change);
}
