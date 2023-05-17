# Learner Management System
## Software Stack

* Python (Django)
* Django REST API
* MySQL

## Setting up the project
* Clone this repository
* `cd` into the project root
* Install dependencies with `pip-sync`
* Create a MySQL user with database CREATE rights. Note the username and
  password
* Create a MySQL database, for the project, and assign it to the user
  above
* Create a file named `.env` at the root of the project and add the
  following (fill in values where you see `<..>`):
```
DATABASE_URL="mysql2://<username>:<password>@localhost/<database name>"
SECRET_KEY="<a random string of letter, numbers and punctuation>"
```
* Activate the virtual environment with `source .venv/bin/activate`
* Start the application with `./manage.py runserver`
The app should start running via port `8000`


## REST Endpoints
The following actions are supported via the REST endpoints:
* Student Creation/Reading/Updating/Deletion
* Teacher Creation/Reading/Updating/Deletion
* Assigning students to a teacher

Note: Remember to always append a slash to the URLs

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
