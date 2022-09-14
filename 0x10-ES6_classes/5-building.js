export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
    if (this.constructor !== Building) {
      if (!this.evacuationWarningMessage) { throw Error('Class extending Building must override evacuationWarningMessage'); }
    }
  }

  get sqft() {
    return this._sqft;
  }
}
