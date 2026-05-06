# AI Agency Website

Welcome to the AI Agency Website! This is a simple, modern web application built for an AI Automation Agency. It includes a beautiful landing page and a functional user authentication system (Login and Registration).

## 🛠️ Built With

*   **Frontend**: HTML, CSS, and vanilla JavaScript.
*   **Backend**: Python using the Flask web framework.
*   **Database**: SQLite (built-in with Python, no extra setup needed).

## ✨ Features

*   **Modern Landing Page**: A beautifully designed home page highlighting services, stats, and a "Schedule a Call" popup.
*   **User Registration**: Users can create a new account which is saved to a local database.
*   **User Login**: Existing users can log in using their credentials.
*   **Clean Code Structure**: CSS styles and HTML are neatly separated for easy editing.

## 🚀 How to Run the Project

It's very easy to get this project running on your own computer.

### Prerequisites
Make sure you have **Python** installed on your computer.

### Step-by-Step Instructions

1.  **Open the Project**: Open your terminal (or command prompt) and navigate to the project folder.
2.  **Install Required Libraries**: The project uses a couple of Python libraries. You can install them by running:
    ```bash
    pip install flask flask-cors
    ```
3.  **Run the Server**: Start the backend server by running the main Python file:
    ```bash
    python app.py
    ```
4.  **View the Website**: Once the server is running, open your web browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

*Note: The very first time you run `app.py`, it will automatically create a `users.db` file in your folder to store your registered users!*

## 📁 Project Structure

*   **`app.py`**: The main Python backend server that handles URLs and the database.
*   **`templates/`**: Contains all the HTML structure files (`Landing_page.html`, `login.html`, `register.html`).
*   **`static/`**: Contains the external CSS files for designing the pages (`style.css`, `auth.css`).
*   **`users.db`**: The SQLite database file where user emails and passwords are saved.
