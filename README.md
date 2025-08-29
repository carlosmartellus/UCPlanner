# UCPlanner

UCPlanner is a desktop application designed to help students organize and track their academic plans at Pontificia Universidad Católica de Chile (PUC).

It provides a simple interface to manually register courses, visualize progress, and manage curricula according to the university’s structure.

> ⚠️ **Note**: This project is specifically tailored for PUC’s system. It does **not** work as a generic planner (e.g., Canvas). If you want to adapt it for another institution, you will need to update the models in `db/models` and `db/controllers`.

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/carlosmartellus/UCPlanner.git
   cd UCPlanner
   ```
2. **Set up Python 3.12.3 Environment**:
    ```bash
    pyenv install 3.12.3     # only if not already installed
    pyenv local 3.12.3       # sets Python version for the project
    python -m venv venv      # create virtual environment
    source venv/bin/activate # activate environment
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Setup Database**:
    ```bash
    alembic -c backend/db/alembic.ini revision --autogenerate -m "Initial migration"
    alembic -c backend/db/alembic.ini upgrade head
    ```
5. **Run the Backend**:
    ```bash
    uvicorn backend.main:app --reload
    ```

## 🛠️ Backend Notes

- The backend is written in Python 3.12.3

    - Uses:

    - SQLAlchemy for ORM

    - Alembic for migrations

    - ⚠️ If you're using a newer Python version (like 3.13), you may encounter errors when installing pydantic. Please stick to Python 3.12.3 for now.

## Updating Data Base
If a modification is needed, follow these steps:
1. Modify SQLAlchemy models in backend/db/models
2. Update Pyndantic schema
3. Create new Alembic migration:
```bash
alembic -c backend/db/alembic.ini revision --autogenerate -m "Add email to User"
``` 
4. Apply the migration:
```bash
alembic -c backend/db/alembic.ini upgrade head
```