

$(function() {
  
  $('p').click(function () {
    $(this).slideUp(1000);
  });//click
  
  $('#content_left').click(function() {
    $('p').show(1000);
  });//click

});//ready