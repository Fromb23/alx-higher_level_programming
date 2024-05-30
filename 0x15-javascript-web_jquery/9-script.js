$(document).ready(function() {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        var helloTranslation = data.hello;
        $('#hello').text(helloTranslation);
    });
});