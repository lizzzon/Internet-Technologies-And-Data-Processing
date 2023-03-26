$(document).ready(function () {
    $('a[href*=#]').bind('click', function (e) {
        e.preventDefault();

        let target = $(this).attr("href");

        $('html, body').stop().animate({scrollTop: $(target).offset().top}, 500, function () {
            location.hash = target;
        });

        return false;
    });
});