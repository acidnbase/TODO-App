# TODO-App
A lightweight, high-performance REST API built with FastAPI. This project serves as a foundational example of how to implement CRUD (Create, Read, Update, Delete) operations with a SQL database integration.

## ✨ Features

  * **Full CRUD**: Create, view, update, and delete tasks.
  * **Database Integration**: Uses **SQLAlchemy** ORM with a **SQLite** backend.
  * **Automatic Documentation**: Interactive Swagger UI available at `/docs`.
  * **Data Validation**: Powered by **Pydantic** for robust request/response handling.

-----

## 🛠️ Tech Stack

  * **Language:** Python 3.8+
  * **Framework:** FastAPI
  * **ORM:** SQLAlchemy
  * **Database:** SQLite
  * **Server:** Uvicorn

-----

## 🏃 Getting Started

### 1\. Clone the repository

```bash
git clone https://github.com/your-username/TODO-App.git
cd fastapi-task-manager
```

### 2\. Set up a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3\. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### 4\. Run the Application

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

-----

## 📖 API Endpoints

Once the server is running, you can test these endpoints manually or via the **Interactive Docs** at `http://127.0.0.1:8000/docs`.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/tasks/` | Retrieve all tasks |
| `POST` | `/tasks/` | Create a new task |
| `PUT` | `/tasks/{id}` | Update an existing task |
| `DELETE` | `/tasks/{id}` | Remove a task |

-----

## 📂 Project Structure

```text
.
├── main.py          # FastAPI app and route definitions
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic schemas for data validation
├── database.py      # Database engine and session configuration
└── sql_app.db       # SQLite database file (generated automatically)
```

-----

## 📝 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

-----
