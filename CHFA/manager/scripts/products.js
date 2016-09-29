$(function() {
  
  /* Put a yes/no dialog on the delete button */
  $('.delete_button').click(function() {
    
    // get the href from the element and place it on the confirm button
    var href = $(this).attr('href');
    $('#confirm_delete_button').attr('href', href);
    
    // show the dialog
    $('#delete_modal').modal();
    
    // cancel the normal submission
    return false;
    
  });//click
  

  // enable the refresh quantity ajax
  $('.refresh_quantity_button').click(function(e) {
    // prevent the default click behavior
    e.preventDefault();
    
    // get the href of the clicked <a> (I stored the item id in that href)
    var href = $(this).attr('href');
    
    // select the quantity (sibling of the clicked button), then load the new quantity into its text.
    // load() calls ajax and automagically places the response in the selected item (.quantity in this case).
    $(this).siblings('.quantity').load(href);
    
  });//click

});//ready

