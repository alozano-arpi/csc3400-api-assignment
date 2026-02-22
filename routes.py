from fastapi import APIRouter, HTTPException
from models import Student
from database import get_connection, dict_from_row

router = APIRouter()

@router.get("/students")
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students')
    row = cursor.fetchall()
    conn.close()

    students = []
    for row in row:
        students.append(dict_from_row(row))

    return {"students": students, "count": len(students)}

@router.get("???")  # TODO: Replace ??? with correct endpoint path
def get_students_by_major(major: str):
    # TODO: Implement this
    pass

@router.get("???")  # TODO: Replace ??? with correct endpoint path
def get_students_by_gpa(min_gpa: float):
    # TODO: Implement this
    pass

@router.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students WHERE id= ?', (student_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Student with ID "+ str(student_id) + " not found")
    
    return dict_from_row(row)

@router.post("/students", status_code=201) 
def create_student(student: Student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO students (name, email, major, gpa, enrollment_year)' \
    ' VALUES (?,?, ?, ?, ?)', (student.name, student.email, student.major, student.gpa, student.enrollment_year))
    student_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
        "id": student_id,
        "name": student.name,
        "email": student.email,
        "major": student.major,
        "gpa": student.gpa,
        "enrollment_year": student.enrollment_year
    }


@router.put("???")  # TODO: Replace ??? with correct endpoint path
def update_student(student_id: int, student: Student):
    # TODO: Implement this
    pass

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
        conn = get_connection()
        cursor = conn.cursor()
    
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        row = cursor.fetchone()
    
        if row is None:
            raise HTTPException(status_code=404, detail="Student with ID " + str(student_id) + " not found")
    
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
        conn.close()
    
        return {"message": "Student deleted successfully"}