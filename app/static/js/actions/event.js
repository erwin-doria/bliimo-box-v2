const downloadVouchers = async isRemoveOld => {
  new Ping().ping('https://google.com', async function(err, data) {
    if (!err && getStorage('Authorization')) {
      $('#download-voucher-modal').modal('toggle');
      $('#load-vouchers').show();
      const data = JSON.parse(
        await request(
          'POST',
          window.location.pathname,
          { isRemoveOld, id: $('.hidden-id').val() },
          { Authorization: getStorage('Authorization') }
        )
      );

      $('.event-title').hide();
      $('#download-btn').prop('disabled', true);
      if (data.length > 0) {
        $('.download-logo').attr('src', '/static/img/check.png');
        $('#download-btn').text('Successfully downloaded vouchers');
      } else {
        $('.download-logo').attr('src', '/static/img/x.png');
        $('#download-btn').html(
          'No vouchers available in this event<br>Please try again'
        );
      }

      setTimeout(() => {
        $('#load-vouchers').hide();
      }, 1000);

      setTimeout(() => {
        $('.download-logo').attr('src', '/static/img/bliimo.png');
        $('#download-btn').text('Download vouchers');
        $('#download-btn').prop('disabled', false);
        $('.event-title').show();
      }, 4000);
    } else {
      alert('No internet connection');
    }
  });
};

$('#download-voucher-modal').on('show.bs.modal', function(event) {
  var button = $(event.relatedTarget);
  var id = button.data('id');
  var modal = $(this);
  modal.find('.hidden-id').val(id);
});
