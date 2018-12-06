$(document).ready(function() {
  
  $(window).scroll(function () {
      console.log($(window).scrollTop())
    if ($(window).scrollTop() > 280) {
      $('#nav_bar').addClass('navbar-fixed');
    }
    if($(window).scrollTop() < 281) {
      $('#nav_bar').removeClass('navbar-fixed');
    }
  });

});


$(function(){
    if ($("#modal-information").length){ 
        console.log("O elemento existe no DOM");
     
    }else {
 
        console.log("Ops! Elemento não existe no DOM");
 
    }    });
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
