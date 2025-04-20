import streamlit as st
import hashlib
import json
import os
from cryptography.fernet import Fernet

# --- Generate/load encryption key ---
KEY_FILE = "secret.key"
DATA_FILE = "data.json"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
        return key

KEY = load_key()
cipher = Fernet(KEY)

# --- Load/Save Data ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# --- App States ---
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
if "stored_data" not in st.session_state:
    st.session_state.stored_data = load_data()

# --- Hashing (PBKDF2 instead of SHA-256) ---
def hash_passkey(passkey, salt="somesalt"):
    return hashlib.pbkdf2_hmac("sha256", passkey.encode(), salt.encode(), 100000).hex()

# --- Encryption & Decryption ---
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    for key, value in st.session_state.stored_data.items():
        if key == encrypted_text and value["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    st.session_state.failed_attempts += 1
    return None

# --- UI Pages ---
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            st.session_state.stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            save_data(st.session_state.stored_data)
            st.success("✅ Data stored securely!")
            st.code(encrypted_text, language='text')
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            if st.session_state.failed_attempts >= 3 and not st.session_state.is_authenticated:
                st.warning("🔒 Too many failed attempts! Please login.")
            else:
                decrypted_text = decrypt_data(encrypted_text, passkey)
                if decrypted_text:
                    st.success(f"✅ Decrypted Data:")
                    st.code(decrypted_text, language='text')
                else:
                    attempts_left = 3 - st.session_state.failed_attempts
                    st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Replace this for real auth
            st.session_state.failed_attempts = 0
            st.session_state.is_authenticated = True
            st.success("✅ Reauthorized successfully! You can now try again.")
        else:
            st.error("❌ Incorrect password!")
