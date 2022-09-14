export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get() {
    return this;
  }

  cloneCar() {
    const NewObj = this.constructor;
    return new NewObj();
  }
}
