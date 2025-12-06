# User Management System

A growing login system written in **Python 3**, now featuring both a **CLI app** and a **Tkinter GUI app**, an expanding admin panel, improved verification logic, and a persistent SQLite database for storing users.

This began as a challenge idea from my friend **kwphil**, and has developed into a modular, expandable authentication system with real password hashing and data management.

---

## 🧩 Requirements

- **Python 3**
- **bcrypt** for password hashing  
- **sqlite3** (bundled with Python)
- **tkinter** for the GUI (bundled on most systems)

Install bcrypt if you don’t have it already:

```bash
pip install bcrypt
```

---

## ⚙️ How to Run

Clone or download the project:

```bash
git clone https://github.com/zachariahstauffer/user.git
cd user
```

Run the **CLI version**:

```bash
python3 CliApp.py
```

Or open the **GUI version**:

```bash
python3 GuiApp.py
```

Both use the same backend logic stored in the `CoreFunctions` folder.

---

## 🪄 Features

### ✅ Sign-Up System
- Creates a new account with a username + password  
- Passwords are hashed using bcrypt  
- Detailed password requirements (uppercase, lowercase, number, special character, no spaces, length limits)

### ✅ Login System
- Checks stored hashed passwords  
- Loads user data from `data.db`  
- Returns a `User` object representing the session  
- Distinguishes between *normal users* and *admin* (admin = user with ID 0)

### ✅ Admin Features
Admins (ID = 0) unlock extra options:

- Delete any user  
- List all users in the database  
- Wipe all users except admin  
- Eventually expandable for more controls

### ✅ User Features
Regular users can:

- Change their password  
- Delete their account  
- Log out

These options appear automatically based on the user’s ID.

### ✅ GUI Version (Tkinter)
- Clean layout with sign-up and login pages  
- Text fields for username and password  
- Displays verification messages inside the window  
- Same backend logic used by the CLI version

### ✅ Database System
Uses SQLite (`data.db`) with a simple table:

```
id | username | password_hash
```

Handles:
- Saving new users  
- Checking existing usernames  
- Loading specific users  
- Listing all users  
- Deleting users  
- Wiping non-admin accounts

---

## 🧠 How It Works (Simplified)

1. When a user signs up, their password gets hashed with bcrypt.  
2. The system stores the username and the hash in `data.db`.  
3. When logging in, the password entered is hashed again and compared to the stored hash.  
4. If it matches, access is granted and a `User` object is created to represent the logged-in account.  
5. The CLI and GUI both rely on the same core modules:
   - `Data.py`
   - `Verify.py`
   - `Login.py`
   - `SignUp.py`
   - `User.py`
   - `AdminSettings.py`

---

## 📦 Project Structure

```
CoreFunctions/
    Data.py
    Verify.py
    Login.py
    SignUp.py
    AdminSettings.py
    User.py

CliApp.py
GuiApp.py
README.md
data.db (auto-created)
```

---

## 🚧 Planned Improvements

- Cleaner GUI layout  
- Improved error messages  
- Password change through GUI  
- Admin options inside the GUI  
- Logging system and event history  
- Stronger verification for existing usernames  

---

## 👥 Credits

- **Developer:** zachariahstauffer  
- **Challenge idea:** [**kwphil**](https://github.com/kwphil)

---

## 📜 License

Open-source.  
Use, modify, or expand it with credit to the original author.

