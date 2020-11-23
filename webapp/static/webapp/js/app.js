// Scroll to
// Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 500, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });

  $('<div></div>')
		.attr('id','scrolltotop')
		.hide()
		.css({'z-index':'1000','position':'fixed','bottom':'25px','right':'25px','cursor':'pointer','width':'40px','height':'40px','background':'#11ffee00'})
		.appendTo('body')
		.click(function(){
			$('html,body').animate({scrollTop: 0}, 'slow');
		});
	$('<div></div>')
		.css({'width':'15px','height':'15px','transform':'rotate(-135deg)','border':'solid #e45643','border-width':'0 3px 3px 0','padding':'2px','margin-top':'16px','margin-left':'12px'})
		.appendTo('#scrolltotop');
	$(window).scroll(function(){
		if($(window).scrollTop()<500){
			$('#scrolltotop').fadeOut();
		}else{
			$('#scrolltotop').fadeIn();
		}
	});