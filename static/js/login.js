//$(function () {
//var height = $(window).height();
//$('#left-image').height(height);

    function loadzonematch(pdata) {
      console.log("loadzonematch > ");
      console.log(pdata);
      $.post("zonematch", pdata, function (data, status) {
        $("body > .container").html(data);
	loadzonematchsec2(pdata)
      });
    }

    function loadzonematchsec2(pdata) {
      console.log("loadzonematchsec2 > ");
      console.log(pdata);
      $.post("zonematchramdom", pdata, function (data, status) {
        $(".card").html(data);
        setTimeout(function(){
          $(".btn-nonlike img").click(function(){$(".card").html("Loading..."); loadzonematchsec2(pdata);});
          $(".btn-like img").click(function(){$(".card").html("Loading...");loadzonematchsec2(pdata);});
        },1000);
      });
    }

    function checkloginform() {
        email = $("#email").val()
        password = $("#password").val()
        api_key = $("#apikey").val()
        if (email && password && api_key) {
            $.ajax({
                type: 'POST',
                crossDomain: true,
                datatype: 'jsonp',
                url: 'http://fesusrocuts.tech:5001/api/v1/auth_token',
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
		    loadzonematch(data);
                }
            });
        }
    }
    function checkapi(token,uri) {
            $.ajax({
                type: 'POST',
                crossDomain: true,
                datatype: 'jsonp',
                url: 'http://127.0.0.1:5001/api/v1/' + uri,
                data: JSON.stringify({
                    "token": token
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
    window.onload = function() {
      $.get("login", function (data, status) {
        $(".card").html(data);
        setTimeout(function(){
          $("#send").click(checkloginform);
	},1000);
      });
    }

//})
