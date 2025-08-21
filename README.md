# UCPlanner

## Version
**0.0.1**

## Libraries
- `setuptools`: tested with version `80.9.0` (should work with `>=64`).
- `PySide6`: tested with version `6.9.1`, might or might not work with other versions.
- `SQLAlchemy`: tested with version `2.0.43`, might or might not work with other versions.
- `pytest`: Optional but useful for testing. Tested with version `8.4.1`

## Considerations
It is made in base of Pontificia Universidad Católica de Chile 's system so this won't work as Canvas or other typical planner. If you want to use this code for your own planner, modify `db/models` and `db/controllers`

Since university has not provided a database, in this version courses must be registered manually.

## Issues
Feel free to publish any issue in https://github.com/carlosmartellus/UCPlanner/issues