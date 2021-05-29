function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$(document).ready(function() {

    $("#deletePast").click(function () {
        console.log('aeogd');
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/excursions/delete/past",
            data: {csrfmiddlewaretoken: getCookie('csrftoken')}
        })
    })
})