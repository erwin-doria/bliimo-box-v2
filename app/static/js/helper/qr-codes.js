const generateQRCode = () => {
  if (document.getElementById('bliimo-qr') !== null) {
    new QRCode(document.getElementById('bliimo-qr'), {
      text: window.location.hostname + ':' + window.location.port,
      width: 70,
      height: 65,
      colorDark: '#000000',
      colorLight: '#ffffff',
      correctLevel: QRCode.CorrectLevel.H
    });
  }
};
