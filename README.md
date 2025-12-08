# User Management System

A growing login system written in **Python 3**, now featuring a **FastAPI web app**, a **CLI app**, and a dedicated **developer maintenance script** for managing users manually.  
The system includes an admin panel, expanded verification logic, templated HTML pages, and a persistent SQLite database for secure user storage.

This began as a challenge idea from my friend **kwphil**, and has developed into a modular, expandable authentication framework with password hashing, session handling, and both browser and console interfaces.

---

## 🧩 Requirements

Install all dependencies with:

    pip install -r requirements.txt

---

## create a virtual evironment(requried on some os)

    python -m venv .venv

---

## ⚙️ How to Run

Clone or download the project:

    git clone [https://github.com/zachariahstauffer/user.git](https://github.com/zachariahstauffer/user.git)
    cd user

### 🖥️ Web Version (FastAPI)

Run the web app:

    python3 WebApp.py

Then open your browser at:

    http://localhost:8000

You’ll see a homepage with **Login** and **Sign Up** buttons.  
The system automatically starts a local Uvicorn server and manages user sessions.

### 💻 CLI Version

If you prefer console use:

    python3 CliApp.py

Both the web and CLI versions share the same authentication backend inside the `CoreFunctions` folder.

### 🧰 Developer Management Script

A standalone developer-only utility is available for advanced database operations:

    python3 Manage_users.py list
    python3 Manage_users.py wipe
    python3 Manage_users.py create-admin

⚠️ **Use this only for development and maintenance.**  
This tool directly modifies the SQLite database and bypasses normal verification logic.

---

## 🪄 Features

### ✅ Sign-Up System
- Register a new username and password  
- Passwords are hashed using bcrypt  
- Strong password requirements enforced (uppercase, lowercase, number, special symbol, no spaces, and length limits)  
- Immediate feedback through both CLI and browser interface

### ✅ Login System
- Authenticates using the hashed password from `data.db`  
- Returns a persistent user session (via FastAPI or Python objects)  
- Creates a `User` instance representing the active login  
- Handles incorrect logins gracefully with alert messages

### ✅ Admin Features
Admins unlock additional tools:
- Promote/demote accounts  
- Delete any user  
- Wipe all non-admin users  
- View active user statistics  
- Fully accessible through both CLI and core logic

### ✅ User Features
Regular users can:
- Change their password  
- Delete their account  
- Log out  
Web users can do all of this from the **User Settings** page.

### ✅ Web Interface (FastAPI)
- Clean HTML frontend using **Jinja2** templates  
- Uses `SessionMiddleware` for secure login persistence  
- Dynamic feedback messages for actions  
- Organized templates:
  - `HomePage.html`
  - `SignUp.html`
  - `Login.html`
  - `UserSettings.html`
- Styled via `/static/css/style.css` for consistent dark theme and alert formatting

### ✅ Database System
Uses SQLite (`data.db`) with a single user table schema:

    id | admin | username | password_hash

Includes:
- Auto-table creation on launch  
- Safe and persistent storage  
- Built-in admin/user distinction  
- Tools for deletion, password updates, and administrative wipes  

---

## 🧠 How It Works (Simplified)

1. The user signs up—passwords are validated for strength and hashed with bcrypt.  
2. The system stores the hash and other details in `data.db`.  
3. During login, the password is compared against the stored hash using bcrypt verification.  
4. If it matches, a user session or `User` object is created.  
5. The FastAPI and CLI apps interact with the same modules:
   - `Data.py`
   - `Verify.py`
   - `Login.py`
   - `SignUp.py`
   - `User.py`
   - `AdminSettings.py`

The `Manage_users.py` file extends this foundation for developer-only database inspection and cleanup.

---

## 📦 Project Structure

    CoreFunctions/
        Data.py
        Verify.py
        Login.py
        SignUp.py
        AdminSettings.py
        User.py

    Templates/
        HomePage.html
        SignUp.html
        Login.html
        UserSettings.html

    static/
        css/
            style.css

    CliApp.py
    WebApp.py
    Manage_users.py
    README.md
    data.db (auto-created)

---

## 🚧 Planned Improvements

- Admin control panel accessible through the web  
- Enhanced web visuals and template structure  
- Full-feature FastAPI-based admin dashboard  
- More robust error pages and redirects  
- Optional email verification and recovery  
- Inline logging of account activities  

---

## 👥 Credits

- **Developer:** zachariahstauffer  
- **Challenge idea:** [**kwphil**](https://github.com/kwphil)

---

## 📜 License

Open-source.  
Use, modify, or expand it with credit to the original author.
