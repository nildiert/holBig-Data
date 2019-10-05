$(function () {
    var height = $(window).height();
    $('#left-image').height(height);
    alert("Si sirve esta mierda")
    $("#send").click(function () {
        console.log("Enviando")
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5001/api/v1/auth_token',
            data: JSON.stringify({
                email = "730@holbertonschool.com",
                api_key = "20377af8fe61e278d8113bdcccd118d9",
                password = "kmzwa8awaa.Nba"
            }),
            contentType: 'application/json',
            success: function (data) {
                console.log("sdfsdf");
                
            },
            failure: function (data) {
                console.log(data)
            }
        });
    });

})
