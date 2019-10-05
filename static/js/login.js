$(function () {
        var height = $(window).height();
        $('#left-image').height(height);

    $("#send").click(function () {
        email = $("#email").val()
        password = $("#password").val()
        api_key = $("#apikey").val()
        if (email && password && api_key) {
            $.ajax({
                type: 'POST',
                crossDomain: true,
                datatype: 'jsonp',
                url: 'http://127.0.0.1:5001/api/v1/auth_token',
                data: JSON.stringify({
                    "email": email,
                    "password": password,
                    "api_key": api_key
                }),
                header: {
                    "Access-Control-Allow-Headers" : "X-PINGOTHER"
                },
                contentType: 'application/json',
                success: function (data) {
                    console.log(data);   
                }
            });
        }

    });

})
