# 🛡️ Secure Data Encryption System Using Streamlit

## 🔰 Project Overview

This Streamlit-based Python application is designed to **securely store and retrieve text data** using **Fernet encryption** and **hashed passkeys**. The system features:

- Data encryption & decryption
- In-memory & JSON-based persistent storage
- Passkey protection with PBKDF2 hashing
- Limited login attempts
- Simple login-based reauthorization

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 🔐 **Secure Data Storage** | Users can enter text and secure it using a unique passkey |
| 🧠 **Strong Passkey Hashing** | PBKDF2 used instead of SHA-256 for added security |
| 🔄 **Fernet Encryption** | Encrypted data using Fernet symmetric encryption |
| 📂 **JSON Data Persistence** | Data is stored in a `data.json` file, retaining entries even after restart |
| ❌ **Failed Attempts Handling** | Only 3 allowed attempts to retrieve data |
| 🔑 **Reauthorization** | After 3 failed attempts, users must log in using a master password |
| 💡 **User-Friendly UI** | Intuitive layout using Streamlit components |

---

## 🛠️ Technologies Used

- **Python 3.9+**
- **Streamlit** for building the web UI
- **cryptography (Fernet)** for encryption
- **hashlib (PBKDF2)** for secure passkey hashing
- **JSON** for persistent local storage

---

## 📁 Project Structure

```
secure_data_app.py      # Main application file
secret.key              # Fernet encryption key
data.json               # Encrypted data storage
README.md               # Project documentation
```

---

## ⚙️ How to Run

1. **Install required libraries** (if not already installed):

```bash
pip install streamlit cryptography
```

2. **Run the app:**

```bash
streamlit run secure_data.py
```

---

## 🔒 Usage Flow

1. **Store Data**:
   - Navigate to “Store Data”
   - Enter your secret message and passkey
   - Your encrypted data will be displayed and saved

2. **Retrieve Data**:
   - Paste the encrypted data
   - Enter the original passkey
   - After 3 incorrect attempts, login is required

3. **Login**:
   - Go to “Login”
   - Enter master password: `admin123` (demo purpose)
   - After login, retry decryption

---

## 📌 Notes

- This app is for **educational/demo purposes**.
- In a production-grade system:
  - Store encryption key securely (use environment variables).
  - Implement proper user authentication.
  - Use secure login and password management.

---

## ✅ Assignment Objectives Covered

- ✔️ Data Storage in Memory + JSON
- ✔️ Passkey Hashing with PBKDF2
- ✔️ Fernet Encryption
- ✔️ Reauthorization after 3 failed attempts
- ✔️ Streamlit-Based UI
- ✔️ Secure Decryption Flow
- ✔️ Optional: Persistence and Advanced Hashing Implemented

---

## 👩‍💻 Developed By

**Neha Fahim**  
Frontend Developer | Python Learner | Educator  
✨ Passionate about building secure & user-friendly applications.
