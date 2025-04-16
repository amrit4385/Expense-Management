# Expense Management System

This repository serves as documentation for the **Expense Management System** project. The system is designed to help users track and manage their daily expenses using an intuitive interface and robust backend services.

The entire project is implemented using **Python** as the core technology, alongside **MySQL** and **FastAPI**, with a user interface powered by **Streamlit**.

**Note:** Raw data and user logs are not uploaded to this repository for privacy and compliance reasons.

---

## Contents
- [Project Objective](#project-objective)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Screenshots & Recordings](#screenshots--recordings)
- [Contact](#contact)

---

## Project Objective

The primary goal of this project is to build a seamless and scalable **Expense Management System** where users can:
- Log their expenses with custom notes and categories.
- Analyze spending habits.
- Export reports.
- Use a clean and interactive web-based interface.

---

## Tech Stack

### **Core Language**
- **Python** – Used for both frontend and backend logic.

### **Backend**
- **FastAPI** – For handling API requests.
- **Uvicorn** – ASGI server for running FastAPI applications.

### **Frontend**
- **Streamlit** – Python library to build interactive web applications.

### **Database**
- **MySQL** – Data storage for expenses and user information.

### **Supporting Libraries**
- **Pydantic** – For data validation.
- **Requests** – For HTTP operations.
- **Logging** – For server-side logging and debugging.
- **pandas** - for creating graphs

---

## Features

- Add or update daily expenses with details like amount, category, and notes.
- Analyze expenses over a date range with visualizations.
- Store expense data in a MySQL database.
- Backend powered by FastAPI for handling requests.
- Frontend built with Streamlit for a user-friendly experience.
- Secure authentication and user management.
- Export expenses as CSV or Excel for record-keeping.

---

## Project Structure

```bash
Expense_Tracking/
├── backend/
│   ├── server.py
│   ├── server.log
│   ├── db_helper.py
│   ├── logging_setup.py
│
├── frontend/
│   ├── app.py
│   ├── add_update_tab.py
│   ├── analytics_category.py
│   ├── analytics_month.py
│   ├── debugging.py
│
├── database/
│   ├── init_db.sql
│   ├── db_config.py
│   └── migrations/
│       ├── 001_create_expenses_table.sql
│       └── 002_add_indexes.sql
│
├── tests/
│   ├── __init__.py
│   └── backend/
│       ├── test_db_helper.sql
│
├── requirements.txt
├── README.md
```

---

## Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/amrit4385/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic.git
cd expense-management-system
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Initialize SQL Server**
- Open SQL Workbench and import the `init_db.sql` file from the `database/` folder.
- Ensure correct host, user, and password settings.

4. **Run the FastAPI Server**
```bash
uvicorn backend.server:app --reload
```

5. **Run the Streamlit Frontend**
```bash
streamlit run frontend/app.py
```

---

## API Endpoints

- `GET /expenses/{expense_date}`: Fetch expenses for a specific date.
- `PUT /expenses/{expense_date}`: Update expenses for a specific date.
- `POST /analytics/`: Fetch expense summary for a date range.
- `POST /export/`: Export expense data as CSV or Excel.

---

## Screenshots & Recordings

📸 **Screenshots:**
- ***Adding/Updating Data***
![Analytics Screenshot](https://github.com/amrit4385/Expense-Management/blob/main/Screenshots/add_update_tab.png)
- SQL Database Structure
![Analytics Screenshot](https://github.com/amrit4385/Expense-Management/blob/main/Screenshots/mysql.png)
- Server Logs
- Category Analytics
- Monthly Analytics

🎥 **Demo Recording:**
- _Coming Soon – Upload demo to a public link and update this section._

---

## Contact

- 📧 **Email:** amrit4385@gmail.com
- 🐛 **GitHub Issues:** [Issue Tracker](https://github.com/amrit4385/Expense-Management/issues)

