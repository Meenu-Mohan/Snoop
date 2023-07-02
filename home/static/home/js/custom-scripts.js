$(document).ready(function(){
  'use strict';


  //===== Responsive Header =====//
  $('.rspn-mnu-btn').on('click', function () {
    $('.rsnp-mnu').addClass('slidein');
    return false;
  });
  $('.rspn-mnu-cls').on('click', function () {
    $('.rsnp-mnu').removeClass('slidein');
    return false;
  });
  $('.rspn-item').on('click', function () {
    var url = $(this).attr('href');
    window.location.href = url;
    $('.rsnp-mnu').removeClass('slidein');
    return false;
  });


  //===== Scrollbar =====//
  if ($('.rsnp-mnu').length > 0) {
    var ps = new PerfectScrollbar('.rsnp-mnu');
  }

  //===== LightBox =====//
  if ($.isFunction($.fn.fancybox)) {
    $('[data-fancybox],[data-fancybox="gallery"]').fancybox({});
  }

  //===== Select =====//
  if ($('select').length > 0) {
    $('select').selectpicker();
  }

  //===== Count Down =====//
  if ($.isFunction($.fn.downCount)) {
    $('.countdown').downCount({
      date: '12/12/2020 12:00:00',
      offset: +5
    });
  }

  //===== Counter Up =====//
  if ($.isFunction($.fn.counterUp)) {
    $('.counter').counterUp({
      delay: 10,
      time: 2000
    });
  }

  //===== Owl Carousel =====//
  if ($.isFunction($.fn.owlCarousel)) {

    //=== Video Carousel ===//
    $('.vdo-car').owlCarousel({
      autoplay: true,
      smartSpeed: 3000,
      loop: true,
      items: 4,
      dots: false,
      slideSpeed: 2000,
      autoplayHoverPause: true,
      nav: true,
      margin: 10,
      navText: [
      "<i class='fa fa-angle-left'></i>",
      "<i class='fa fa-angle-right'></i>"
      ],
      responsive:{
        0:{items: 1,nav: false},
        481:{items: 2,margin: 10},
        780:{items: 2,margin: 10},
        981:{items: 3,margin: 10},
        1025:{items: 4,margin: 10},
        1200:{items: 4}
      }
    });

    //=== Latest Event Carousel ===//
    $('.ltst-evnt-car').owlCarousel({
      autoplay: true,
      smartSpeed: 3000,
      loop: true,
      items: 1,
      dots: false,
      slideSpeed: 5000,
      autoplayHoverPause: true,
      nav: true,
      margin: 0,
      animateIn: 'fadeIn',
      animateOut: 'fadeOut',
      navText: [
      "<i class='fa fa-angle-left'></i>",
      "<i class='fa fa-angle-right'></i>"
      ],
    });
	
	$('.featured-car').owlCarousel({
		loop:true,
		margin:0,
		responsive:{
			0:{
				items:1
			},
			600:{
				items:1
			},
			1000:{
				items:1
			}
		}
	});

  }

  //===== Slick Carousel =====//
  if ($.isFunction($.fn.slick)) {

    $('.wrk-gal-mn').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: false,
      arrows: false,
      slide: 'li',
      fade: false,
      asNavFor: '.wrk-gal-nv'
    });
    
    $('.wrk-gal-nv').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      asNavFor: '.wrk-gal-mn',
      dots: false,
      arrows: false,
      slide: 'li',
      vertical: false,
      centerMode: true,
      centerPadding: '0',
      focusOnSelect: true,
      responsive: [
      {
        breakpoint: 770,
        settings: {
          slidesToShow: 5,
          slidesToScroll: 1,
          infinite: true,
          centerMode: true
        }
      },
      {
        breakpoint: 490,
        settings: {
          slidesToShow: 5,
          slidesToScroll: 1,
          infinite: true,
          centerMode: true
        }
      }
      ]
    });
  }

});//===== Document Ready Ends =====//


jQuery(window).on('load',function() {
  'use strict';

  //===== PageLoader =====//
  $(".preloader").fadeOut("slow");
});//===== Window onLoad Ends =====//


//===== Sticky Header =====//
$(window).on('scroll',function () {
  'use strict';

  var menu_height = $('header').innerHeight();
  var scroll = $(window).scrollTop();
  if (scroll >= menu_height) {
    $('.stick').addClass('sticky');
  } else {
    $('.stick').removeClass('sticky');
  }
});
$(window).on('scroll',function () {
  'use strict';

  var menu_height = $('.rspn-hdr').innerHeight();
  var scroll = $(window).scrollTop();
  if (scroll >= menu_height) {
    $('.stick').addClass('sticky2');
  } else {
    $('.stick').removeClass('sticky2');
  }
});//===== Window onScroll Ends =====//
// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

