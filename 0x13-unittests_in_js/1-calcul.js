const calculateNumber = (a, b) => { Math.round(a) + Math.round(b);
if (type === 'SUBTRACT') {
    return aRound - bRound;
  }

  if (type === 'DIVIDE') {
    if (bRound === 0) {
      return 'Error';
    }
    return aRound / bRound;
  }

  return aRound + bRound;
};

module.exports = calculateNumber;