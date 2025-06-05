 
# Patient Management System (PAMS) - Django Project

This is a basic Django application built as part of the assessment for the Associate Software Engineer role at ClaimBuddy Technologies.

## 📌 Project Overview

The Patient Management System is a Django-based web app that displays a list of patients and their insurance details using the **Stisla Admin Dashboard Template**.

---

## 🛠️ Features Implemented

- ✅ Django project setup with app: `pams`
- ✅ `Patient` model with:
  - Full Name
  - Age
  - Gender (with choices)
  - Insurance Provider
  - Policy Number
- ✅ Dummy data for 5 patients
- ✅ View and template to list all patients in a responsive table
- ✅ Integrated Stisla admin dashboard theme
- ✅ Dynamic rendering of patient data in the UI
- ✅ Environment variables used for sensitive configurations

---

## 📸 Screenshot

![Screenshot 2025-06-06 015154](https://github.com/user-attachments/assets/efa79919-f01e-4b57-b964-7c2b4925b806)


---

## 💡 Tech Stack

- Python 3.x
- Django
- HTML/CSS/JS (from Stisla Template)
- Bootstrap (via Stisla)
- SQLite (default)



## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/pams.git
   cd pams

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run migrations and seed data**
   ```bash
   python manage.py migrate
   python manage.py loaddata patients.json  # if using fixture

5. **Run the server**
    ```bash
   python manage.py runserver

6. **Visit the app**
   http://127.0.0.1:8000/




