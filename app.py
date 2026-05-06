from flask import Flask, request, jsonify, render_template 
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

DB = "users.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("Landing_page.html")

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    # data = request.json
    # email = data.get("email")
    # password = data.get("password")
    
    # conn = get_db()
    # conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    # conn.commit()
    # conn.close()
    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    ).fetchone()
    conn.close()

    if user:
        return render_template("login.html")
    else:
        return jsonify({"error": "Invalid credentials"}), 401



if __name__ == "__main__":
    app.run(debug=True)
