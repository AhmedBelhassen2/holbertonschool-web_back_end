/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
  const Arr = [];
  for (const string of array) {
    Arr.push(appendString + string);
  }
  
  return Arr;
}
  