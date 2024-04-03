$(document).ready(function () {
  $('#add_item').click(function () {
    $('<li>').text('Item').appendTo('.my_list');
  });
});
