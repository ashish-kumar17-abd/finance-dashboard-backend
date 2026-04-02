# 💰 Finance Dashboard Backend (DRF)

## 📌 Overview

This project is a backend system for a finance dashboard application. It provides APIs for managing financial records, user roles, and generating analytics data for dashboard visualization.

The system is designed with a focus on clean architecture, role-based access control (RBAC), and efficient data processing.

---

## 🚀 Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* SQLite (can be replaced with PostgreSQL/MySQL)
* JWT Authentication (SimpleJWT)

---

## 🔐 Authentication & Roles

The system supports role-based access control:

| Role    | Permissions                               |
| ------- | ----------------------------------------- |
| Viewer  | Read-only access to dashboard and records |
| Analyst | Can create, update, and view records      |
| Admin   | Full access (manage records and users)    |

Authentication is implemented using JWT tokens.

---

## 💰 Financial Records API

Each financial record includes:

* Amount
* Type (INCOME / EXPENSE)
* Category
* Date
* Notes

### Supported Operations:

* Create record
* View records
* Update record
* Delete record
* Filter records by:

  * Category
  * Type
  * Date range

---

## 📊 Dashboard Analytics API

Provides aggregated data for frontend dashboards:

* Total Income
* Total Expenses
* Net Balance
* Category-wise expenses (Pie chart ready)
* Monthly trends (Line chart ready)
* Recent transactions

---

## 🔒 Access Control

Custom permission classes are implemented to enforce role-based restrictions:

* Viewer → Read-only
* Analyst/Admin → Full CRUD access

---

## 🔍 Filtering Support

Records can be filtered using query parameters:

```
/api/records/?category=Food
/api/records/?type=EXPENSE
/api/records/?start_date=2026-04-01&end_date=2026-04-30
```

---

## 📡 API Endpoints

### Auth

* POST `/api/register/`
* POST `/api/login/`

### Records

* GET `/api/records/`
* POST `/api/records/`
* PUT `/api/records/{id}/`
* DELETE `/api/records/{id}/`

### Dashboard

* GET `/api/dashboard/`

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone https://github.com/ashish-kumar17-abd/finance-dashboard-backend.git
cd finance-dashboard-backend
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run migrations:

```
python manage.py migrate
```

5. Start server:

```
python manage.py runserver
```

---

## 🧠 Design Decisions

* Used Django REST Framework for scalable API development
* Implemented custom permissions for role-based access control (RBAC)
* Organized project into modular apps (accounts, records, dashboard)
* Optimized queries using aggregation functions for analytics

---

## ✨ Future Improvements

* Pagination
* Advanced filtering
* API documentation (Swagger/OpenAPI)
* Deployment (Render / AWS)

---

## 📌 Conclusion

This project demonstrates backend design, API structuring, role-based access control, and analytics processing for a real-world finance dashboard system.

---
