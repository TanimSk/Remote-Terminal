function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submit_data(endpoint, payload) {

    let csrftoken = getCookie('csrftoken');

    console.log('provoked!');

    fetch(endpoint, {
        method: "POST",
        headers: {
            'Accept': 'application/json, text/plain',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
        },
        credentials: 'include',
        body: JSON.stringify(payload)
    });
}