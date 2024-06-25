# TeamCollab
TeamCollab is building a robust project management tool designed to enhance team collaboration on various projects. The API is a crucial component of this tool, providing seamless integration with the front-end web and mobile applications. This is a Django-based project management application that allows users to manage projects, tasks, and team members. The application includes user authentication, project and task management, role-based access control, and commenting features.

## Features
- User authentication and registration
- Project creation and management
- Task creation, assignment, and tracking
- Role-based access control for project members (admin and member roles)
- Commenting on tasks
## Requirements
- Django (4.2, 5.0)
- Python (3.8, 3.9, 3.10, 3.11, 3.12)
- PostgreSQL (optional, you can use SQLite for development)
## Installation
### 1. Clone the repository
```sh
git clone https://github.com/anmabrar/teamCollab.git
cd teamCollab
```
### 2. Install Pipenv
If you don't have pipenv installed, you can install it using pip:
```sh
pip install pipenv
```
### 3. Install Dependencies
Use pipenv to install the required dependencies:
```sh
pipenv install
```
### 4. Activate the Virtual Environment
Activate the virtual environment created by pipenv:
```sh
pipenv shell
```
### 5. Apply Migrations
Run the following command to apply database migrations:
```sh
python manage.py migrate
```
### 6. Create a Superuser
Create a superuser to access the Django admin interface:
```sh
python manage.py createsuperuser
```
Follow the prompts to set up the superuser credentials.
### 7. Run the Development Server 
Start the Django development server:
```sh
python manage.py runserver
```
## Usage
- Access the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials.
- Create users, projects, and tasks through the admin interface or implement the frontend as needed.
## Contributing
If you want to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements, whether they are code improvements, bug fixes, or documentation enhancements.
## API Documentation
- `http://127.0.0.1:8000/swagger/` 
- `http://127.0.0.1:8000/redoc/` 

## Additional Notes

-  **Database Configuration**: If you need to use a different database (other than SQLite), make sure to update the `DATABASES` setting in the `settings.py` file.
-  **Static Files**: If you are serving static files, ensure you have set up the static files directory and collected static files using:
   ```bash
   python manage.py collectstatic
    ```
## Additional packages
  - Django Rest Framework
  - Simple JWT
  - drf-nested-routers
  - Swagger 

## Swegger Documentation preview
![screencapture-127-0-0-1-8000-swagger-2024-06-25-10_22_07](https://github.com/anmabrar/teamCollab/assets/86479721/3068f285-20bb-47db-a1e9-aa04d441c539)

