$(function () {

    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:5001/api/v1/',
        data: JSON.stringify({
        }),
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
            
        }
    });
})
