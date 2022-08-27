$(document).ready(function(){
	$('.accordion-heading').click(function(){
		if($(this).attr('data-open') == 'open'){
			$('.accordion-body').slideUp("slow");
			$(this).next().slideDown();
			$('.accordion-heading').attr('data-open','open');
			$(this).attr('data-open','close');
		} else {
			$(this).next().slideUp("slow");
			$('.accordion-heading').attr('data-open','open');
		}
	});

	$('.section').hide();

    setTimeout(function () {

      $('.section').fadeIn();

      $('.loader').fadeOut();

    },3000)
	
});
