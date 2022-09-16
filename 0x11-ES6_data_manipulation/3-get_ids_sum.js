export default function getListStudentIds(array1) {
  return array1.reduce((previousValue, currentValue) => previousValue + currentValue.id, 0);
}
