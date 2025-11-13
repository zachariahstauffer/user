# User

A small but growing login system project written in **Python 3**, now updated with both **CLI** and **GUI** versions for different user experiences.  
Originally made as a **challenge idea from my friend [kwphil](https://github.com/kwphil)**.

This project lets you:
- Sign up with a username and password  
- Log in securely using stored credentials  
- Save and verify user data from a local database (`data.db`)  
- Convert text to hashed values using bcrypt  
- Choose between a command-line or graphical interface for login management  

---

## 🧩 Requirements

- **Python 3** (any recent version works)
- The **bcrypt** library for password hashing
- The **sqlite3** module (included with Python)
- **tkinter** (comes with most Python installations, used for the GUI)

Install bcrypt if needed:
```bash
pip install bcrypt
```

---

## ⚙️ How to Run

1. Download or clone this repository:
   ```bash
   git clone https://github.com/zachariahstauffer/user.git
   cd user
   ```

2. Run the **CLI version**:
   ```bash
   python3 CliApp.py
   ```

3. Or, launch the **GUI version**:
   ```bash
   python3 GuiApp.py
   ```

---

## 🪄 How to Use

Both versions let you sign up, log in, and manage user data — the only difference is how you interact with them.

### Command-Line Example (Main.py)
```
sign-up or login: sign-up
Make Username: zach
Make Password: Mypassword!1
User created successfully!

sign-up or login: login
Username: zach
Password: mypassword
user found, checking password...
zach has logged in
```

### Graphical Example (App.py)
A small window appears with buttons and text boxes for creating or logging into an account.  
You can enter your username and password, click “Sign Up” or “Login,” and see the results directly in the GUI.

---

## 🧠 File Overview

- **Main.py** → Command-Line Interface (CLI) version of the program.  
- **App.py** → Graphical User Interface (GUI) version using tkinter.  
- **User.py** → Defines the User class and manages account data.  
- **Data.py** → Handles reading, writing, and managing stored data in `data.db`.  
- **Verify.py** → Contains verification logic for user credentials.  
- **Txt_to_hash.py** → Utility for converting plain text to bcrypt hashes.  
- **data.db** → Local SQLite database that stores usernames and hashed passwords.  
- **.gitignore** → Keeps unnecessary files out of version control.

---

## 💾 How It Works (Simplified Explanation)

- Usernames and hashed passwords are stored securely inside an SQLite database (`data.db`).  
- Passwords are hashed using **bcrypt**, which prevents direct recovery of the original password.  
- During login, the entered password is hashed again and compared to the saved hash.  
- If the hashes match — access granted; if not — access denied.  
- Both the CLI and GUI versions rely on the same backend modules for logic and data handling.

---

## 🧰 Features

- Secure password handling using bcrypt  
- Modular design separating logic, data, and interface  
- Both GUI and CLI options for flexibility  
- Local SQLite database persistence  
- Text-to-hash converter utility  

---

## 🚧 Planned Improvements

- Add password reset functionality  
- Enhanced GUI layout and visuals  
- Better error handling and exception reporting  
- Logging system for admin use  

---

## 👥 Credits

- **Developer:** zachariahstauffer  
- **Challenge idea:** [**kwphil**](https://github.com/kwphil)

---

## 📜 License

This project is open-source.  
You’re free to use, modify, or share it with credit to the original authors.
