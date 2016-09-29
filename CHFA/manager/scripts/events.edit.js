$(function() {
  // set up the date time picker gui
  $('#id_start_date,#id_end_date').datetimepicker({
  	mask:'9999-19-39',
  	timepicker: false,
  	format: 'Y-m-d',
    allowBlank: true,
  });//datetimepicker
  
  
  
  /* Put a yes/no dialog on the delete button */
  $('.delete_area_button').click(function() {
    
    // get the href from the element and place it on the confirm button
    var href = $(this).attr('href');
    $('#confirm_delete_button').attr('href', href);
    
    // show the dialog
    $('#delete_modal').modal();
    
    // cancel the normal submission
    return false;
    
  });//click
  
  
  
  // set up the loadmodal for the edit/create form
  $('.edit_area_button').click(function(e) {
    e.preventDefault();
    
    // load the login content
    $.loadmodal({
      url: $(this).attr('href'),
      id: 'areamodal',
      title: 'Event Area:',
      width: 500,
    });

  });//click  
  
});//ready