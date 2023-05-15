# Learner Management System
## Software Stack

* Python (Django)
* Django REST API
* MySQL

## REST Endpoints
Remember to always append a slash

### Get list of students
GET /students/

### Get a particular student
GET /students/<id>

### Create a student record
POST /students/
pay load:
```
{
    "name": "john",
    "surname": "smith"
}
```

### Update a student's record
PUT /students/<id>/
payload:
```
{
    "name": "name",
    "surname": "surname"
}
```

### Delete a student's record
DELETE /students/<id>/
payload: none

### Get list of teachers
GET /teachers/

### Get a particular teacher
GET /teachers/<id>

### Create a teacher record
POST /teachers/
payload:
```
{
    "name": "teacher name"
}
```

### Update a teacher record
PUT /teachers/<id>/
payload:
```
{
    "name": "new name"
}
```

### Delete a teacher record
DELETE /teachers/<id>/

### Assign a student to a teacher

### List a teacher's students

### Remove/Unassign a student from a teacher
