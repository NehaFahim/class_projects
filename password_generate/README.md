# 🔐 Simple Password Generator

A simple yet powerful password generator built using **Python** and **Streamlit**, created as part of a UV assignment. This app allows users to generate secure passwords based on custom options like length, inclusion of digits, and special characters.

---

## 🚀 Features

- Choose password length (between 6 to 32 characters)
- Option to include:
  - Numbers (0-9)
  - Special characters (!@#$%^&* etc.)
- Clean and interactive UI built with **Streamlit**
- Randomized secure password output

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit**
- **Random** and **String** (Python built-in libraries)

---

## 📦 Installation & Setup
First, install **UV** (if not already installed):
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```sh
uv --version
```

---
### 2️⃣ Create and Initialize the Project

```sh
uv init password-generator
cd password-generator
```

---

### 3️⃣ Install Sreamlit (Dependency)

```sh
uv add streamlit
```

---
### 5️⃣ Run Password Generator

```sh
streamlit run password.py
```
