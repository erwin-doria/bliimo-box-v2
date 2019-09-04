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

$(document).ready(function() {
  showClaims();
});
