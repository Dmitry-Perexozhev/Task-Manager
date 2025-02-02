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
- PostgreSQL
- Poetry
- Make
- Docker, Docker Compose

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
3) Standard installation<br>
Create the .env file and set up values for environment variables:<br>
- **`SECRET_KEY`**: a secret key for your application.
- **`DATABASE_URL_dev`**: the connection string for your PostgreSQL database, formatted as `postgresql://username:password@localhost:5432/database_name`
- **`DEBUG`**: True or False<br>
- **`ALLOWED_HOSTS`**: localhost or ip server address for deployment
- **`ACCESS_TOKEN`**: add Rollbar token
If you choose to use SQLite DBMS, do not add DATABASE_URL variable.<br>

Install the required dependencies using Poetry:<br>
```
make install
```
Start the migration process. PostgreSQL must be running:<br>
```
make migrate
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
4) Installation using Docker<br>
Create the .env file and set up values for environment variables:<br>
- **`SECRET_KEY`**: a secret key for your application.
- **`DATABASE_URL_deploy`**: the connection string for your PostgreSQL database, formatted as `postgresql://username:password@localhost:5432/database_name`
- **`DEBUG`**: True or False
- **`POSTGRES_USER`**: postgres username 
- **`POSTGRES_PASSWORD`**: user password
- **`POSTGRES_DB`**: name database<br>
- **`ALLOWED_HOSTS`**: localhost or ip server address for deployment
- **`ACCESS_TOKEN`**: add Rollbar token<br>
Build the app. Gunicorn server is in use:
```
docker-compose up --build -d
```
