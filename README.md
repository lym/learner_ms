# Learner Management System
## Software Stack

* Python (Django)
* Django REST API
* MySQL

## Setting up the project
* Clone this repository
* `cd` into the project root
* Install dependencies with `pip-sync`
* Activate the virtual environment with `source .venv/bin/activate`
* Start the application with `./manage.py runserver`
The app should start running via port `8000`

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
POST /teachers/<teacher id>/students/
payload:
```
[
    {"name": "name 1", "surname": "surname 1"},
    {"name": "name 2", "surname": "surname 2"}
]
```

### List a teacher's students
GET /teachers/<teacher id>/students/
response: Array of students

## Testing the UI
The entry point is at _http://127.0.0.1:8000/academia/_
