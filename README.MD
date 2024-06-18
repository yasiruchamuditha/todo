# To-Do List Application

This is a simple To-Do List application built with Flask, MySQL, and a frontend using HTML, CSS, and JavaScript. It allows users to create, edit, delete, and mark tasks as completed. The application also includes user authentication to manage individual user tasks.

## Features

- User authentication (sign up and log in)
- Create, edit, delete, and mark tasks as completed
- Responsive design for different screen sizes
- Server-side form validation
- Secure password storage using hashing

## Technologies Used

- Backend: Flask, Flask-SQLAlchemy, Flask-Bcrypt, Flask-Login
- Database: MySQL
- Frontend: HTML, CSS, JavaScript
- Other: WTForms for form handling and validation

## Installation

### Prerequisites

- Python 3.x
- MySQL
- pip (Python package installer)

### Steps

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/yasiruchamuditha/todo.git>
    cd todo_app
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the MySQL database:**

    Open your MySQL command line interface and create a database:
    ```sql
    CREATE DATABASE todo_db;
    ```

4. **Configure the application:**

    Open the `config.py` file and ensure the MySQL configuration matches your MySQL server setup:
    ```python
    import os

    class Config:
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = 'root'
        MYSQL_DB = 'todo_db'
        SECRET_KEY = os.urandom(24)
    ```

5. **Set up the database tables:**

    Use the Flask CLI to create the database tables. Open a Python shell and run:
    ```python
    from app import db
    db.create_all()
    ```

6. **Run the Flask application:**
    ```bash
    python app.py
    ```

7. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:5000`.

## Folder Structure


Certainly! Here's a README.md file for your To-Do List application:

markdown
Copy code
# To-Do List Application

This is a simple To-Do List application built with Flask, MySQL, and a frontend using HTML, CSS, and JavaScript. It allows users to create, edit, delete, and mark tasks as completed. The application also includes user authentication to manage individual user tasks.

## Features

- User authentication (sign up and log in)
- Create, edit, delete, and mark tasks as completed
- Responsive design for different screen sizes
- Server-side form validation
- Secure password storage using hashing

## Technologies Used

- Backend: Flask, Flask-SQLAlchemy, Flask-Bcrypt, Flask-Login
- Database: MySQL
- Frontend: HTML, CSS, JavaScript
- Other: WTForms for form handling and validation

## Installation

### Prerequisites

- Python 3.x
- MySQL
- pip (Python package installer)

### Steps

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/yasiruchamuditha/todo.git>
    cd todo_app
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the MySQL database:**

    Open your MySQL command line interface and create a database and create the database tables:
    ```sql
    CREATE DATABASE todo_db;

    USE todo_app;

    CREATE TABLE user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );

    CREATE TABLE task (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        completed BOOLEAN NOT NULL DEFAULT FALSE,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES user(id)
    );
    ```

4. **Configure the application:**

    Open the `config.py` file and ensure the MySQL configuration matches your MySQL server setup:
    ```python
    import os

    class Config:
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = 'root'
        MYSQL_DB = 'todo_db'
        SECRET_KEY = os.urandom(24)
    ```

5. **Run the Flask application:**
    ```bash
    python app.py
    ```

6. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:5000`.

## Folder Structure

todo_app/
│
├── app.py
├── config.py
├── models.py
├── routes.py
├── forms.py
├── templates/
│ ├── login.html
│ ├── signup.html
│ ├── index.html
│ └── layout.html
└── static/
├── css/
│ └── style.css
└── js/
└── script.js


## Usage

- **Sign Up:** Create a new user account.
- **Log In:** Log in with your username and password.
- **Add Task:** Use the form to add a new task.
- **Mark Complete:** Click on a task to mark it as complete or incomplete.
- **Delete Task:** Click the delete link next to a task to remove it.

## Contribution

Feel free to fork this repository and contribute by submitting a pull request. Please ensure your changes are well-documented and tested.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

