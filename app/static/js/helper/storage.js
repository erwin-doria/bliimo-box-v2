const setStorage = data => {
  localStorage.setItem(data['key'], data['value']);
};

const getStorage = key => {
  return localStorage.getItem(key);
};
