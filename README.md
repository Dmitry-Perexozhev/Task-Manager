[![Actions Status](https://github.com/Dmitry-Perexozhev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Dmitry-Perexozhev/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b4975e07f182c91a4872/maintainability)](https://codeclimate.com/github/Dmitry-Perexozhev/python-project-52/maintainability)
<div align="center">
<img src="https://github.com/Dmitry-Perexozhev/python-project-52/blob/main/img/task-manager-banner.svg" alt="logo" width="270" height="auto" />
<h1>Task Manager</h1>
</div>

Task Manager is a Dajngo-based web application that enables users to build work processes more efficiently

### Key Features:

- Set tasks, statuses, labels
- Assign performers of task
- Change task statuses
- Set multiple tasks labels
- Filtering tasks
- User authentication and registration
- Admin panel

### More details

The main functionality of the system is available after **registration** and **authorization**. Only the user himself can change and delete a user.<br />

**Statuses** - helps to understand at what stage the task is currently - new, in progress, in testing, completed.<br />

**Labels** - allows you to group tasks by different characteristics such as bugs, features, and so on. Labels are related to the task of relating many to many.<br />

**Task** is the main entity in the project. When creating, the fields described above are available, as well as the name, description, and performer.
Also, each task has mandatory fields - **author** (set automatically when creating the task) and status.<br />

To find the necessary tasks, a **filtering system** is used. It allows you to filter both one by one and by several parameters such as - status, performer, label, only your tasks.<br />

Additionally, it is impossible to delete a user, label, or status in the system if they are specified in at least one task.

### Installation requirements

- Python
- Django
- Bootstrap 5
- PostgreSQL
- Poetry
- Gunicorn
- Make

### Getting Started
#### Installation

1) Clone the project repository to your local device:
```
git@github.com:Dmitry-Perexozhev/python-project-52.git
```
2) Go to the project directory:
```
cd python-project-52
```
3) Set up environment variables.
Create the .env file in the root folder and set the value of the **SECRET_KEY** and **DATABASE_URL** keys
```dotenv
DATABASE_URL=postgresql://postgres:password@db:5432/postgres
SECRET_KEY={your secret key}
```
If you choose to use SQLite DBMS, do not add DATABASE_URL variable.<br />

4) Install the required dependencies using Poetry and make a migration. PostgreSQL must be running:
```
make build
```

### Usage

- Run the server locally in development mode 
```
make dev
```
- Run the production Gunicorn server
```
make start
```