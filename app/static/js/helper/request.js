const request = async (method, url, body, header) => {
  headers = { 'Content-Type': 'application/json' };
  if (typeof header == 'object') headers = { ...headers, ...header };
  const request = {
    method,
    body: method == 'GET' ? undefined : JSON.stringify(body),
    headers
  };
  return await fetch(url, request).then(res => {
    return res.text();
  });
};
