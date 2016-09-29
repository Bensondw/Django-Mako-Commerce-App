$(function() {

  /* Show/hide specialized fields depending on the type */
  $('#id_ptype').change(function() {
    var ptype = $(this).val();
    $('.RentalProductField').closest('tr').toggle(ptype == 'RentalProduct');
    $('.IndividualProductField').closest('tr').toggle(ptype == 'IndividualProduct');
    $('.BulkProductField').closest('tr').toggle(ptype == 'BulkProduct');
  });//change
  
  // trigger when the page loads
  $('#id_ptype').change();
  
  
  // set up the date time picker gui
  $('#id_purchase_date').datetimepicker({
  	format: 'Y-m-d H:m:s',
    allowBlank: true,
  });//datetimepicker

});//ready