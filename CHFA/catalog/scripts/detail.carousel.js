//this will handle the logic of carouseling images


$(function() {
	// console.log("beginning");

	$('.pimage').first().removeClass('hide');

	$('.previous').click(function() {

		var current = $('.pimage:not(.hide)');
		var next = current.prev('.pimage');

		if (next.length == 0 ) {
			next = current.nextAll().last();
		}
		current.addClass('hide');
		next.removeClass('hide');

	}); // show images modal

	$('.next').click(function() {

		var current = $('.pimage:not(.hide)');
		var next = current.next('.pimage');

		if (next.length == 0 ) {
			next = current.prevAll().last();
		}
		current.addClass('hide');
		next.removeClass('hide');

	}); // show images modal

	// console.log("end");
});
