const sinon = require('sinon');

const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi function', () => {
  const spyUtils = sinon.spy(Utils, 'calculateNumber');
  const spyConsole = sinon.spy(console, 'log');


  it('validate the usage of the Utils function', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;

    spyUtils.restore();
    spyConsole.restore();  
});
});