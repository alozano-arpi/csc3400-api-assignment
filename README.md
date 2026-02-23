## Student Record API
A RESTful API that manages student records for a university system using FastAPI and SQLite. The API will allow users to create, read, update, and delete student information, as well as filter by major or GPA threshold.

## Installation Instructions
1. Clone the repository 
```
https://github.com/alozano-arpi/csc3400-api-assignment.git
```
2. Create virtual environment 
```bash
python -m venv .venv
```
3. Activate virtual environment
```bash
source .venv/Scripts/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Start development server
```
uvicorn main:app --reload
```

## API Endpoints 

| HTTP Method | URL path | Description | Status Codes
| --- | --- | --- |--- |
| GET | /students | To retrieve all students in database | 200 OK
| GET | /students/by-major | To retrieve students by their major | 200 OK, 404 Not Found
| GET | /students/by-gpa | To retrieve students by a minimum gpa | 200 OK, 400 Bad Request
| GET | /students/{student_id} | To retrieve a student by their unique ID | 200 OK, 400 Bad Request
| POST | /students | To create a new student record | 201 Created, 400 Bad Request
| PUT | /students/{student_id} | To update a student record | 200 OK, 404 Not Found
| DELETE | /students/{student_id} | To delete a student record | 200 OK, 204 No Content, 404 Not Found

## Testing Instructions 
1. Start the server 
```
uvicorn main:app --reload
```
2. Open FastAPI's docs for API testing 
`
http://127.0.0.1:8000/docs
`
3. Test Endpoints
    - Click on desired endpoint to test.
    - Click "Try it out"
    - Fill in request body or given parameters. 
    - Click "Execute"

**Note**
- The database (`students.db`) is automatically created when a student record is added.
- Data will persist when server restarts.

## Example Usage
### Create a New Student 
#### **POST /students**

**Request Body Example:**
```json
{
  "name": "Carol White",
  "email": "carol.white@university.edu",
  "major": "Physics",
  "gpa": 3.9,
  "enrollment_year": 2023
}
```

**Response Example (Success):**

```json
{
  "id": 3,
  "name": "Carol White",
  "email": "carol.white@university.edu",
  "major": "Physics",
  "gpa": 3.9,
  "enrollment_year": 2023
}
```
**Response (Not Found):**

```json 
{
   "detail":"Name cannot be empty"
}
```
```json 
{
    "detail":"Major cannot be empty"
}
```
```json 
{
    "detail":"GPA must be between 0.0 and 4.0"       
}
```
**Status Code: 400 Bad Request**

---

### Delete a Student
**DELETE /students{student_id}**

**Path Parameter:**

- `student_id`: Integer (student's unique ID)

**Response (Success):**

```json
{
  "message": "Student deleted successfully"
}
```

**Status Code:** 200 OK (or 204 No Content with no response body)

**Response (Not Found):**

```json
{
  "detail": "Student with ID 999 not found"
}
```
**Status Code: 404 Not Found**

---
### Retrieve a Student by Their GPA
**GET /students/by-gpa**

**Query Parameter:**

- `min_gpa`: Float (minimum GPA threshold)

**Response Format Example:**

```json
{
  "students": [...],
  "count": 2,
  "min_gpa": 3.5
}
```

**Status Code:** 200 OK

**Response Example (Invalid GPA):**

```json
{
  "detail": "GPA must be between 0.0 and 4.0"
}
```
**Status Code:** 400 Bad Request
