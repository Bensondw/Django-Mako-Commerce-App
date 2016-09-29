
$(function() {  
  $('#loginbutton').click(function() {
    
    // load the login content
    $.loadmodal({
      url: '/account/login/',
      id: 'loginmodal',
      title: 'Welcome! Login here:',
      width: 500,
    });
    
  });//click
  
});//ready