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
| GET | `/menu/` | Get all menu items | ❌ No |
| GET | `/menu/<id>/` | Get single menu item | ❌ No |

---

### **User Table Booking**

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| POST | `/bookings/` | Create a new booking | ✔ Yes (User) | `{ "customer_name": "", "customer_email": "", "booking_date": "", "number_of_people": 0 }` |
| GET | `/bookings/history/` | Get user's booking history based on user token | ✔ Yes (User) | None |

---

## 🛠️ Admin APIs

### **Menu Management (Admin Only)**

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| POST | `/menu/` | Create a menu item | ✔ Admin | `{ "title": "", "price": 0, "description": "" }` |
| GET | `/menu/` | List all menu items | ❌ Public | - |
| GET | `/menu/<id>/` | Get single menu item | ❌ Public | - |
| PATCH | `/menu/<id>/` | Update menu item | ✔ Admin | (Partial fields)`{ "title": "", "price": 0, "description": "" }` |
| DELETE | `/menu/<id>/` | Delete menu item | ✔ Admin | - |

---

### **Table Booking Management (Admin Only)**

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| GET | `/bookings/` | Get all bookings | ✔ Admin | - |
| GET | `/bookings/<id>/` | Get single booking | ✔ Admin | - |
| PATCH | `/bookings/<id>/` | Update booking | ✔ Admin | (Partial fields) `"customer_name": "", "customer_email": "", "booking_date": "", "number_of_people": 0 }`  |
| DELETE | `/bookings/<id>/` | Delete booking | ✔ Admin | - |

---

