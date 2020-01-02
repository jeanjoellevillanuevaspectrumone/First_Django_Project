$(document).ready(function() {

    $('#about-btn').click(function() {
        alert('You clicked the button using JQuery!')
    });

    $('p').hover(
        function() {
            $(this).css('color', 'cyan');
        },
        function() {
            $(this).css('color', 'black');
    });

    $("#about-btn").click(function() {
        msgStr = $("#msg").html()
        msgStr = msgStr + " ooo, fancy!"
        $("#msg").html(msgStr)
    });
});