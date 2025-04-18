# 🧮 Unit Converter

This is a simple and interactive **Unit Converter** built using **Python** ,**UV** and **Streamlit**. It allows users to convert values between different units of measurement such as length, weight, and temperature.

---

## 🚀 Features

- Convert between:
  - Length units: meters, kilometers, miles, feet, inches
  - Weight units: kilograms, grams, pounds, ounces
  - Temperature units: Celsius, Fahrenheit, Kelvin
- User-friendly interface with dropdown menus
- Instant conversion as values are entered
- Built with Python and Streamlit

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**

---

## Getting Started

### 1️⃣ Install UV

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
uv init unit-converter
cd unit-converter
```

---

### 3️⃣ Install Sreamlit (Dependency)

```sh
uv add streamlit
```

---

### 5️⃣ Run Unit Converter

```sh
streamlit run uc.py
```
