// loads the modal
$(function() {  

  $('#view_more_images').click(function(e) {
    e.preventDefault();
    // load the login content
    $.loadmodal({
      url: $(this).attr('href'), //this is the url to be loaded into the modal. url: $(this).attr('href') or url: '/catalog/detail.carousel/'
      id: 'carouselmodal',
      title: 'Look Pictures!',
      width: 500,
    });
    
  });//click

  $('#buyform').load('/catalog/cart.add/${product.id}'); //should load up the html from /catalog/cart.add/
  console.log($('#buyform'));
  
});//ready