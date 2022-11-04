const { expect } = require('chai');
const sinon = require('sinon');

const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi function', () => {
    it('validate the usage of the Utils function', () => {

    const stubUtils = sinon.stub(Utils, 'calculateNumber');stubUtils.returns(10);
    const spyConsole = sinon.spy(console, 'log');
    
        sendPaymentRequestToApi(100, 20);
    expect(spyUtils.calledOnce).to.be.true;
    expect(spyUtils.calledWith('SUM', 100, 20)).to.be.true;
    spyUtils.restore()
    spyConsole.restore();
  });
});