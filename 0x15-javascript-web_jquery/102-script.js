$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      method: 'GET',
      data: { lang: languageCode },
      success: function (response) {
        $('#hello').text(response.hello);
      },
      error: function () {
        $('#hello').text('Failed to fetch translation');
      }
    });
  });
});
