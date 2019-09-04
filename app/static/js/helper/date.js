const convertDate = date => {
  const months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
  ];

  const dateArr = date.split('-');
  return `${months[parseInt(dateArr[1])]} ${dateArr[2]}, ${dateArr[0]}`;
};
