# User

A small login system project using **Python 3** and **bcrypt** for password hashing.  
Originally made as a **challenge project** from my friend [**kwphil**](https://github.com/kwphil).

This program lets you:
- Sign up with a username and password  
- Log in using your credentials  
- Save and load user data from a local file (`data.dat`)  
- Wipe all saved login data if needed  

---

## 🧩 Requirements

- **Python 3** (any recent version works)
- The **bcrypt** library for password hashing  

If you don’t have bcrypt, install it by running this command in your terminal:

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
2. Run the program:
   ```bash
   python3 Main.py
   ```

---

## 🪄 How to Use

When the program starts, it’ll ask you to type one of the following commands:

- **sign-up** → Create a new account  
- **login** → Log in with an existing username and password  
- **wipe** → Erase all saved user data  

Example run:

```
sign-up or login: sign-up
Make Username: zach
Make Password: mypassword
```

Then, to log in:

```
sign-up or login: login
Username: zach
Password: mypassword
user found, checking password
zach has logged in
```

---

## 💾 How It Works (Simplified Explanation)

- User information (username and hashed password) is stored in a file called `data.dat` using Python’s **pickle** module.  
- Passwords are never saved directly — they’re **hashed** using `bcrypt` so the original password can’t be read from the file.  
- The `verify` class uses `bcrypt.checkpw()` to compare your entered password to the saved hash.  
- The program reads and saves users automatically through the `data` class.

---

## 👥 Credits

Created by **Zach**, inspired by a challenge from [**kwphil**](https://github.com/kwphil).  
