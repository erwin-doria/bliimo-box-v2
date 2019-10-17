const showClaims = () => {
  claimsTable = $('#claims-table').DataTable({
    processing: false,
    serverSide: false,
    scrollY: '50vh',
    scrollCollapse: true,
    ajax: {
      url: '/claims',
      type: 'POST'
    },
    columns: [
      { data: 'vouchers.name' },
      { data: 'vouchers.email' },
      { data: 'vouchers.voucher' },
      { data: 'vouchers.type' },
      { data: 'vouchers.maxPax' },
      { data: 'vouchers.events_day' },
      { data: 'pax' },
      { data: 'actions' }
    ]
  });

  $('#search').keyup(function() {
    claimsTable.search($(this).val()).draw();
  });

  setInterval(function() {
    claimsTable.ajax.reload(null, false);
  }, 5000);
};

const claim = async id => {
  const data = JSON.parse(
    await request('POST', '/claim/vouchers', {
      id
    })
  );

  data['id']
    ? snackbar('Successfully claimed vouchers')
    : snackbar('Unable to claim vouchers please try again');
};

const deleteClaims = async id => {
  const conf = confirm('Are you sure you want to delete this claim?');
  if (conf) {
    const data = JSON.parse(
      await request('DELETE', '/claim/delete', {
        id
      })
    );
    snackbar('Successfully deleted claims');
  }
};

const uploadVouchers = () => {
  new Ping().ping('https://google.com', async function(err, data) {
    if (!err && getStorage('Authorization')) {
      const data = JSON.parse(await request(
        'POST',
        '/voucher/upload',
        {},
        {
          Authorization: getStorage('Authorization')
        }
      ));
      data.length > 0 ? snackbar('Successfully uploaded vouchers') : snackbar('No vouchers uploaded')
      $('#uploadBtn').hide();
    }
  });
};

  const isNeedToUpload = async ()=>{
    const data = JSON.parse(await request(
      'GET',
      '/claim/unredeemed',
    ));

    data.length > 0 ? $('#uploadBtn').show() : $('#uploadBtn').hide()

    setTimeout(()=>{
      isNeedToUpload();
    },5000)

  }


$(document).ready(function() {
  showClaims();
  isNeedToUpload();
});
