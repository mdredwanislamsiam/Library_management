# Library Management System API

A **Library Management System** built using **Django REST Framework (DRF)** that provides RESTful APIs to manage books, authors, categories, members, and borrowing records. The project includes **JWT-based authentication**, **role-secured endpoints**, and **interactive API documentation** using Swagger.

---

## 🚀 Features

* 📖 Manage **Books**
* ✍️ Manage **Authors**
* 🗂️ Manage **Categories**
* 👤 Manage **Members**
* 🔄 Track **Borrowing & Returning Records**
* 🔐 **JWT Authentication** using **Djoser**
* 📑 **Swagger API Documentation** using **drf_yasg**
* 🧩 Fully RESTful CRUD APIs
* 🕒 Track borrow and return dates

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** JWT (Djoser + SimpleJWT)
* **Database:** SQLite (can be replaced with PostgreSQL/MySQL)
* **API Documentation:** drf_yasg (Swagger & ReDoc)

---

## 📂 Project Structure (Overview)

```
Library_Management/
│
├── api/                  # Central API routing
├── books/                # Book, author, category, borrow logic
├── users/                # User & authentication logic
├── Library_Management/   # Project settings & configuration
├── staticfiles/
├── manage.py
└── requirements.txt

```

---

## 📊 Database Models

### 📘 Book

| Field               | Type        |
| ------------------- | ----------- |
| id                  | Primary Key |
| title               | CharField   |
| author              | ForeignKey  |
| ISBN                | CharField   |
| category            | ForeignKey  |
| availability_status | CharField   |

### ✍️ Author

| Field     | Type        |
| --------- | ----------- |
| id        | Primary Key |
| name      | CharField   |
| biography | TextField   |

### 🗂️ Category

| Field       | Type        |
| ----------- | ----------- |
| id          | Primary Key |
| name        | CharField   |
| description | TextField   |

### 👤 Member

| Field           | Type        |
| --------------- | ----------- |
| id              | Primary Key |
| name            | CharField   |
| email           | EmailField  |


### BorrowRecord

| Field       | Type        |
| ----------- | ----------- |
| id          | Primary Key |
| book        | ForeignKey  |
| member      | ForeignKey  |
| borrow_date | DateField   |
| return_date | DateField   |

---

## 🔐 Authentication

* JWT Authentication implemented using **Djoser**
* Token-based login & registration
* Secured endpoints for authenticated users

### Auth Endpoints

```
POST   /auth/jwt/create/
POST   /auth/jwt/refresh/
POST   /auth/users/
GET    /auth/users/me/
```

---


##  API Endpoints (`/api/`)

###  Authors

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| GET    | /api/authors/      | List authors    |
| POST   | /api/authors/      | Create author   |
| GET    | /api/authors/{id}/ | Retrieve author |
| PUT    | /api/authors/{id}/ | Update author   |
| PATCH  | /api/authors/{id}/ | Partial update  |
| DELETE | /api/authors/{id}/ | Delete author   |

---

###  Books

| Method | Endpoint         | Description    |
| ------ | ---------------- | -------------- |
| GET    | /api/books/      | List books     |
| POST   | /api/books/      | Create book    |
| GET    | /api/books/{id}/ | Retrieve book  |
| PUT    | /api/books/{id}/ | Update book    |
| PATCH  | /api/books/{id}/ | Partial update |
| DELETE | /api/books/{id}/ | Delete book    |

---

###  Borrowed Records

| Method | Endpoint                    | Description            |
| ------ | --------------------------- | ---------------------- |
| GET    | /api/borrowed_records/      | List borrowed records  |
| POST   | /api/borrowed_records/      | Borrow a book          |
| GET    | /api/borrowed_records/{id}/ | Retrieve record        |
| PUT    | /api/borrowed_records/{id}/ | Update record          |
| PATCH  | /api/borrowed_records/{id}/ | Partial update         |
| DELETE | /api/borrowed_records/{id}/ | Return / delete record |

---

###  Categories

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| GET    | /api/categories/      | List categories   |
| POST   | /api/categories/      | Create category   |
| GET    | /api/categories/{id}/ | Retrieve category |
| PUT    | /api/categories/{id}/ | Update category   |
| PATCH  | /api/categories/{id}/ | Partial update    |
| DELETE | /api/categories/{id}/ | Delete category   |

---

##  API Documentation

Swagger UI is available at:

```
/swagger/
/redoc/
```

You can explore and test all endpoints interactively.

---

##  Installation & Setup

###  Clone the Repository

```bash
git clone https://github.com/mdredwanislamsiam/Library_management.git
cd Library_management
```

###  Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

###  Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

##  Testing the API

* Use **Swagger UI**
* Use **Postman**
* Authenticate using JWT token in headers:

```
Authorization: Bearer <your-token>
```

---

## Future Enhancements

* Role-based permissions (Admin / Librarian / Member)
* Fine calculation for late returns
* Book search & filtering
* Pagination and ordering
* Email notifications

---

## Author

**Your Name**
Backend Developer | Django REST Framework

---

## 📜 License

This project is licensed under the MIT License.

