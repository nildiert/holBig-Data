$(document).ready(function () {
    let dicto = {};
    $('#enviar').click(function(){
        console.log("Hizo click");
        email = $("#email").val()
        pass = $("#pass").val()
        key = $("#key").val()
        var settings = {
            'cache': false,
            'dataType': "jsonp",
            "async": true,
            "crossDomain": true,
            "url": "https://holbigdata-api.herokuapp.com/users",
            "method": "POST",
            "headers": {
                "accept": "application/javascript",
                "Access-Control-Allow-Origin":"*"
            }
        }
  
        $.ajax(settings).done(function (response) {
            console.log(response);
  
        }).fail(function (response) {
            console.log(response)
        });
        });
    });

    