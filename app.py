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
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        conn = get_db()
        conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        return jsonify({"message": "User registered"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "User already exists"}), 400


# LOGIN
@app.route("/login", methods=["POST"])
def login():
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
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


# DELETE USER
@app.route("/delete", methods=["POST"])
def delete_user():
    data = request.json
    email = data.get("email")

    conn = get_db()
    conn.execute("DELETE FROM users WHERE email=?", (email,))
    conn.commit()
    conn.close()

    return jsonify({"message": "User deleted"})


# UPDATE PASSWORD
@app.route("/update", methods=["POST"])
def update_password():
    data = request.json
    email = data.get("email")
    new_password = data.get("password")

    conn = get_db()
    conn.execute("UPDATE users SET password=? WHERE email=?", (new_password, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Password updated"})


if __name__ == "__main__":
    app.run(debug=True)