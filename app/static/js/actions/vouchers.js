const refreshVouchers = async () => {
  await request('POST', '/voucher/refresh');
  setTimeout(() => {
    refreshVouchers();
  }, 5000);
};

const uploadVouchers = () => {
  new Ping().ping('https://google.com', async function(err, data) {
    if (!err && getStorage('Authorization')) {
      await request(
        'POST',
        '/voucher/upload',
        {},
        {
          Authorization: getStorage('Authorization')
        }
      );
    }
  });

  setTimeout(() => {
    uploadVouchers();
  }, 5000);
};
