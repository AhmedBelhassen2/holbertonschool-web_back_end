export default function getStudentsByLocation(arrayofobjects, city) {
  return arrayofobjects.filter((i) => i.location === city);
}
