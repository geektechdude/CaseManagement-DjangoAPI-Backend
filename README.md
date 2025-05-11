![Django App Tests](https://github.com/geektechdude/CaseManagement-DjangoAPI-Backend/actions/workflows/test_django.yml/badge.svg)

![Test Coverage](https://github.com/geektechdude/CaseManagement-DjangoAPI-Backend/actions/workflows/test_coverage.yml/badge.svg)


# Case Management DjangoAPI Backend
Backend for a Case Management system. The backend is written in Python using Django and Django Frameworks to deliver the backend via APIs.

# User Requirements
The backend should be able to:

- Create a task with the following properties: 'Title', 'Description (optional)', 'Status', 'Due Date/Time'

- Retrieve a task by ID

- Retrieve all tasks

- Update the status of a task

- Delete a task

# Running the Case Management DjangoAPI Backend
- Clone the repository
- Open the repository (change to the repository directory)
- Create a Virtual Environment using the command "python3 -m venv ./venv"
- Activate the Virtual Environment using the command "source ./venv/bin/activate"
- Install the required Python modules using the command "pip install -r requirements.txt"
- Run Django server using command "python manage.py runserver"

# Accessing the API Endpoints
By default Django serves via port 8000.

- /api/v1/tasks/ 
Lists all tasks when used with the GET method. Using the POST method a new task can be added.

- /api/v1/task/(id)
Replace id with the interget id of the task. The GET method returns the task details. The PUT method updates the task details. The DELETE method deletes the task.