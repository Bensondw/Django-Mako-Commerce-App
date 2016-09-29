$(function(){
	



	// update the shopping cart icon on load 
	$('#shopping_cart_button > #num_items').text('${ request.shopping_cart.get_item_count() }'); 


	

}); //ready