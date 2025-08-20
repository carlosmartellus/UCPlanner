from setuptools import setup, find_packages

setup(
    name="UCPlanner",
    version="0.0.1",
    description="Planner for UC",
    author="Carlos Martel",
    url="https://github.com/carlosmartellus/UCPlanner.git",
    install_requires=[
        "PySide6>=6.9.1",
        "SQLAlchemy>=2.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "ucplanner=UCPlanner.__main__:main",
        ],
    },
)
