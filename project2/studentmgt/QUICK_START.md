# 🚀 Quick Start Guide

## Before Running:

### 1. **Update MySQL Password in settings.py**

Open: `studentmgt/settings.py` (line 82)

Change:
```python
'PASSWORD': 'your_mysql_password',  # ← Put your actual MySQL root password here
```

### 2. **Make sure MySQL is running**

Check MySQL Workbench or start MySQL service.

### 3. **Create the database**

In MySQL Workbench, run:
```sql
CREATE DATABASE studentmgt_db;
```

## Run the Application:

### Step 1: Create database tables
```bash
cd c:\Users\Admin\Desktop\project2\studentmgt
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create admin user
```bash
python manage.py createsuperuser
```
Enter your email, username, and password.

### Step 3: Start the server
```bash
python manage.py runserver
```

### Step 4: Open browser
Go to: **http://127.0.0.1:8000/**

---

## Check Database Connection:

### In Django shell:
```bash
python manage.py shell
```

Then type:
```python
from django.db import connection
connection.ensure_connection()
print("✓ Connected to:", connection.settings_dict['NAME'])
```

### In MySQL Workbench:
1. Connect to localhost
2. Click on `studentmgt_db` database
3. After migrations, you'll see tables like:
   - students_user
   - students_student  
   - students_course
   - django_* tables

---

**You're all set!** 🎉
