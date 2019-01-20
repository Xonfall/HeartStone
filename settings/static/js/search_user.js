$('#s_fn').keyup(function(){
    $.get('/user/user_search/', {username: $('#s_fn').val()}, function(data){
        $('#search_results').html(data);
    });
});