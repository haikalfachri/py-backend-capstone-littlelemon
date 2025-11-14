# 🍋 Little Lemon API Documentation

This document describes all available API endpoints for the **Little Lemon Backend Capstone Project**.

---

## 📄 Useful Command
``` 
python -m pipenv install django djangorestframework djoser mysqlclient
python -m pipenv shell
django-admin startproject <<littlelemon>> .
python manage.py startapp <<restaurant>>
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py test -v 3
```

## 🏠 Homepage

`http://127.0.0.1:8000/api/`

## 🔐 Authentication

### **Auth Endpoints**

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| POST | `/auth/token/login` | Login and receive tokens | ❌ No | `{ "username": "", "password": "" }` |
| POST | `/auth/users/` | Register a new user | ❌ No | `{ "username": "", "email": "", "password": "" }` |

---

## 👤 User APIs

### **Menu (Public Endpoints)**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/menu/` | Get all menu items | ❌ No |
| GET | `/api/menu/<id>/` | Get single menu item | ❌ No |

---

### **User Table Booking**

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| POST | `/api/bookings/` | Create a new booking | ✔ Yes (User) | `{ "customer_name": "", "customer_email": "", "booking_date": "", "number_of_people": 0 }` |
| GET | `/bookings/history/` | Get user's booking history based on user token | ✔ Yes (User) | None |

---

## 🛠️ Admin APIs

### **Menu Management (Admin Only)**

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| POST | `/api/menu/` | Create a menu item | ✔ Admin | `{ "title": "", "price": 0, "description": "" }` |
| GET | `/api/menu/` | List all menu items | ❌ Public | - |
| GET | `/api/menu/<id>/` | Get single menu item | ❌ Public | - |
| PATCH | `/api/menu/<id>/` | Update menu item | ✔ Admin | (Partial fields)`{ "title": "", "price": 0, "description": "" }` |
| DELETE | `/api/menu/<id>/` | Delete menu item | ✔ Admin | - |

---

### **Table Booking Management (Admin Only)**

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| GET | `/api/bookings/` | Get all bookings | ✔ Admin | - |
| GET | `/api/bookings/<id>/` | Get single booking | ✔ Admin | - |
| PATCH | `/api/bookings/<id>/` | Update booking | ✔ Admin | (Partial fields) `"customer_name": "", "customer_email": "", "booking_date": "", "number_of_people": 0 }`  |
| DELETE | `/api/bookings/<id>/` | Delete booking | ✔ Admin | - |

---

