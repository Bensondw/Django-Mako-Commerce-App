$(function(){
	$('.add_form > form').ajaxForm({
		// target identifies the element(s) to update with the server response
		target: $('#buyform'),
	});



	// update the shopping cart icon on load 
	$('#shopping_cart_button > #num_items').text('${ request.shopping_cart.get_item_count() }'); 


	

}); //ready