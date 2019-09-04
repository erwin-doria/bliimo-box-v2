# bliimo-box-v2

**INSTALLATIONS**

1. Install dependencies
   **pip3 install**
   - flask_sqlalchemy
   - sqlalchemy
   - flask_migrate
   - marsmallow
2. Create database `bliimov2`
3. Change the `database` credentials in `instance/config.py`
4. Migrate database by running `flask db upgrade` **NOTE** If installing from raspberry pi please import bliimo.sql
5. Run the application `python3 app.py`
