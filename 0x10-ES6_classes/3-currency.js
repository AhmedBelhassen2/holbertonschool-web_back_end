export default class Currency {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  set name(name) {
    this._name = name;
  }

  set code(code) {
    this._code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
