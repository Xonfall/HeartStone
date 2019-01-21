
$(".follow").click(function () {
    $target = $(this);
    $.post("/user/" + $target.attr('data-follow'), {followed: $target.attr('data-user')}, function (data) {
        if (data.status == 'ok') {
            if ($target.attr('data-follow') == 'follow') {
                $target.attr('data-follow', 'unfollow');
                $target.text('unfollow');
                $(".followers-number").text(parseInt($(".followers-number").text()) + 1);
            }
            else {
                $target.attr('data-follow', 'follow')
                $target.text('follow');
                $(".followers-number").text(parseInt($(".followers-number").text()) - 1);
            }
        }
    });
  });