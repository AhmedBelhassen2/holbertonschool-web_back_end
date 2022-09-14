export default function getListStudentIds(arrayofids) {
  if (!Array.isArray(arrayofids)) return [];
  return arrayofids.map((i) => i.id);
}
