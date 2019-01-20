$("#edit").click(function () {
    var form = new FormData();
    form.append("username", $("input[name='username']").val());
    form.append("email", $("input[name='email']").val());
    $.ajax({
        url: '/user/edit',
        data: form,
        processData: false,
        type: 'POST',
        contentType: false,
        success: function (data) {
            if (data.status == 'ok') {
                $(".moncompte").attr("href","/profile/" + $("input[name='username']").val());
                $('.username').text($("input[name='username']").val());
                $('.email').text($("input[name='email']").val());
                $('.profile-card-name').text( "@" + $("input[name='username']").val());
                $(".alert").show();
                $(".alert .message").text("Success! : Edited !");
                $(".alert ").css("background-color", "#dff0d8");
                $(".alert ").css("color", "#3c763d");

                window.setTimeout(function() {
                    $(".alert").fadeTo(500, 1).slideUp(500, function(){
                        $(this).hide(); 
                    });
                }, 4000);

                window.history.pushState('page', 'Title', '/profile/' + $("input[name='username']").val());

            }
            else {
                $(".alert").show();
                $(".alert .message").text("Error!");
                $(".alert ").css("background-color", "red");
                $(".alert ").css("color", "#fff");

                window.setTimeout(function() {
                    $(".alert").fadeTo(500, 1).slideUp(500, function(){
                        $(this).hide(); 
                    });
                }, 4000);
            }
        }
    });
});