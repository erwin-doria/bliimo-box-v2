const response = data => {
  let img = '';
  let txt = '';

  if (data['status'] == 1) {
    img = 'check';
    txt = 'Thank you for waiting.';
  } else {
    img = 'x';
    txt = 'Please scan again.';
  }

  setTimeout(() => {
    $('#bliimo-img').attr('src', '/static/img/' + img + '.png');
    $('.home-welcome').text(data['description']);
    $('.home-p').text(txt);
  }, 1000);

  setTimeout(() => {
    $('#bliimo-img').attr('src', '/static/img/bliimo.png');
    $('.home-welcome').text('Welcome to Bliimo box');
    $('.home-p').text('Waiting for the QR code to scan.');
  }, 3500);
};

const deleteResponse = async id =>
  await request('POST', '/response/delete', { id });

const showResponse = async () => {
  const resp = JSON.parse(await request('GET', '/response'));
  if (Object.keys(resp).length > 0) {
    deleteResponse(resp['id']);
    response(resp);
  }
  setTimeout(() => {
    showResponse();
  }, 2000);
};

const snackbar = text => {
  const toast = $('#snackbar');
  toast.text(text);
  toast.addClass('show');
  setTimeout(() => {
    toast.removeClass('show');
  }, 3000);
};
