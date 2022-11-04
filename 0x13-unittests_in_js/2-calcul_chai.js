const calculateNumber = (type, a, b) => { 
    const ard = Math.round(a);
    const brd = Math.round(b);
if (type === 'SUBTRACT') {
    return ard - brd;
  }

  if (type === 'DIVIDE') {
    if (brd === 0) {
      return 'Error';
    }
    return ard / brd;
  }

  return ard + brd;
};

module.exports = calculateNumber;