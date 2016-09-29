$(function() {

  $('#id_birth_date').datetimepicker({
  	mask:'9999-19-39',
  	timepicker: false,
  	format: 'Y-m-d',
    allowBlank: true,
  });//datetimepicker
  
  
  // set up the loadmodal for password form
  $('#change_password_button').click(function(e) {
    e.preventDefault();
    
    // load the login content
    $.loadmodal({
      url: $(this).attr('href'),
      id: 'change_password',
      title: 'Change Password',
      width: 500,
    });
    
  });//click
  
  

});//ready