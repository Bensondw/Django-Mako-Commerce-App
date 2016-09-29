console.log(1);

$(function() {
  console.log(2);
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
  
});//ready