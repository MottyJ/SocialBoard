function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});


$("#login").bind("click", tryLogin);

function tryLogin() {
    $.ajax("/login/", {
        type: "POST",
        data: {
            "username": $("#username").val(),
            "password": $("#password").val(),
            "next": $("#next").val()
        },
        success: console.log("yay!")
    });
}


$(document).ready(function () {
    var d = new Date();

    var month = d.getMonth() + 1;
    var day = d.getDate();

    var output = d.getFullYear() + '/' +
        (month < 10 ? '0' : '') + month + '/' +
        (day < 10 ? '0' : '') + day;

    $("#date").html(output)

    $("#newpost").click(function(){
        $("#my-form").css("display", "flex")
        $("#options").css("display", "flex")
        $("#plus").css("display", "none")
    });

    $("#cancel").click(function(){
        $("#options").css("display", "none")
        $("#plus").css("display", "flex")
    });

    $("#post").click(function(){
        $("#options").css("display", "none")
        $("#plus").css("display", "flex")
        $("#my-form").css("display", "none")
        $.ajax("/new_post/", {
            type: "POST",
            data: {
                "title": $("#title").val(),
                "content": $("#content").val(),
                "author": $("#author").val()
            },
            success: function(){
                location.reload();
            }
        });
    });

});