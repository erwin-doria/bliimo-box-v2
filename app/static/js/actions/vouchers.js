const refreshVouchers = async () => {
  await request('POST', '/voucher/refresh');
  setTimeout(() => {
    refreshVouchers();
  }, 5000);
};
