# UCPlanner

UCPlanner is a desktop application designed to help students organize and track their academic plans at Pontificia Universidad Católica de Chile (PUC).

It provides a simple interface to manually register courses, visualize progress, and manage curricula according to the university’s structure.

⚠️ Note: This project is specifically tailored for PUC’s system. It does not work as a generic planner (e.g., Canvas). If you want to adapt it for another institution, you will need to update the models in db/models and db/controllers.

## Installation

1. Clone the repository:

    `git clone https://github.com/carlosmartellus/UCPlanner.git`

    `cd UCPlanner`

2. Install dependencies:

    `pip install -r requirements.txt`

3. Generate database migrations:

    `alembic -c backend/src/db/alembic.ini revision --autogenerate -m "Description"`

    `alembic -c backend/src/db/alembic.ini upgrade head`

4. Run backend:

    `python -m backend.src.main`

## Backend Notes
- Backend is written in `Python 3.12+`, using `SQLAlchemy` for ORM and `Alembic` for migrations
