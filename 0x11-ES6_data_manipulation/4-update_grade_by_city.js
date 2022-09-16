export default function updateStudentGradeByCity(arrayofstudents, city, new_grades) {
    return arrayofstudents.filter((i) => i.location === city).map((i) => {
        const [newGrade] = new_grades.filter((item) => item.studentId === i.id);
        return { ...i, grade: newGrade ? newGrade.grade : 'N/A' };
      });
    }