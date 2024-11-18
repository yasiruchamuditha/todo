# To-Do List Application

This is a simple To-Do List application built with Flask, MySQL, and a frontend using HTML, CSS, and JavaScript. It allows users to manage their tasks with features like creating, editing, deleting, and marking tasks as completed. The application includes user authentication to ensure task management is secure and personalized.

## Features

- User authentication (Sign Up and Login).
- Create, edit, delete, and mark tasks as completed.
- Responsive design for different screen sizes.
- Server-side form validation.
- Secure password storage using hashing.

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Bcrypt, Flask-Login.
- **Database**: MySQL.
- **Frontend**: HTML, CSS, JavaScript.
- **Other**: WTForms for form handling and validation.

## Installation

### Prerequisites

- Python 3.x.
- MySQL.
- pip (Python package installer).

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yasiruchamuditha/todo.git
    cd todo_app
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the application:**

    Edit the `config.py` file to match your MySQL server setup:
    ```python
        MYSQL_HOST = 'your-database-host'
        MYSQL_USER = 'your-database-username'
        MYSQL_PASSWORD = 'your-database-password'
        MYSQL_DB = 'your-database'
        SECRET_KEY = os.urandom(24)  # For session management
    ```

4. **Set up the MySQL database:**

    Open your MySQL command line interface and create the required database:
    ```sql
    CREATE DATABASE todo_db;
    ```

5. **Run the Flask application:**
    ```bash
    python app.py
    ```

6. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Sign Up**: Create a new user account.
2. **Log In**: Log in with your username and password.
3. **Add Task**: Use the form to add a new task.
4. **Mark Complete**: Click on a task to mark it as complete or incomplete.
5. **Delete Task**: Click the delete link next to a task to remove it.

## Contribution

Feel free to fork this repository and contribute by submitting a pull request. Ensure your changes are well-documented and tested.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
