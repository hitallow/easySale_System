$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('#id_cpf').mask('000.000.000-00', {reverse: true});


});

$(document).ready(function() {
  
  $(window).scroll(function () {
      //if you hard code, then use console
      //.log to determine when you want the 
      //nav bar to stick.  
      console.log($(window).scrollTop())
    if ($(window).scrollTop() > 280) {
      $('#nav_bar').addClass('navbar-fixed');
    }
    if ($(window).scrollTop() < 281) {
      $('#nav_bar').removeClass('navbar-fixed');
    }
  });
});

$(function(){
    var SetCarouselHeight = function() {
        $("#carouselExampleIndicators .item > img").height(function(){
            return $("#myCarousel").width() * 0.5;
        });
    }

    SetCarouselHeight();
    $(window).resize(function(){
        SetCarouselHeight();
    }); 
});