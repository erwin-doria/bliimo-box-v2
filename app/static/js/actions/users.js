const login = async credentials => {
  const resp = $('#resLogin');
  const data = JSON.parse(await request('POST', '/login', credentials));

  if (data['accessToken']) {
    setStorage({
      key: 'Authorization',
      value: `${data['tokenType']} ${data['accessToken']}`
    });

    resp.text('Successfully logged in');
    resp.removeClass('text-danger');
    resp.addClass('text-success');

    setTimeout(() => {
      window.location.replace('/');
    }, 1200);
  } else {
    resp.text('Invalid email or password');
    resp.addClass('text-danger');
    resp.removeClass('text-success');
  }
};

const logout = () => {
  localStorage.clear();
  window.location.reload();
};

const isLoggedIn = () => {
  const auth = getStorage('Authorization');
  if (!auth && window.location.pathname != '/login') {
    window.location.replace('/login');
  } else if (auth && window.location.pathname == '/login') {
    window.location.replace('/');
  }
};
