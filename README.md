# School Management System with Role-Based Access Control

## Project Description
This project is a School Management System built using Django. It allows users to perform CRUD operations to manage student details, library history, and fees history. The system implements role-based access control (RBAC) with different user roles: School Admin, Office Staff, and Librarian. Each role has specific permissions to access and manage various aspects of the system.

## Features
- **Authentication**: User login functionality using Django's authentication framework.
- **Admin Dashboard**:
  - Manage (create, edit, delete) Office Staff and Librarian accounts.
  - Perform CRUD operations on student, library, and fees records.
- **Office Staff Dashboard**:
  - View all student details.
  - Manage fees history.
  - View library history for students.
- **Librarian Dashboard**:
  - View-only access to student and library history.
  - Manage library borrowing records for students.
- **Student Management**: Create, update, view, and delete student details.
- **Library History**: View and manage (add, edit, delete) library borrowing records.
- **Fees History**: View and manage (add, edit, delete) fees records.

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file for environment variables (if any):**
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=your_database_url
    ```

5. **Run migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

8. **Access the application:**
    Open a web browser and go to `http://127.0.0.1:8000/`

## Libraries Used
- Django
- djangorestframework
- django-environ
