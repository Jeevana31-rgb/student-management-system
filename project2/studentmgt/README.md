# Student Management System

A comprehensive Django-based web application for managing students, courses, and academic records with MySQL database integration.

## Features

- 🎓 **Student Registration & Management**: Add, edit, view, and delete student records
- 📚 **Course Management**: Create and manage courses
- 🔐 **Secure Authentication**: User registration and login system
- 📊 **Dashboard**: Overview of total students and courses
- 💾 **MySQL Database**: Persistent data storage using MySQL Workbench

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- MySQL Server 8.0 or higher
- MySQL Workbench (optional, for database management)
- pip (Python package manager)

## Installation & Setup

### Step 1: Install MySQL

1. Download and install MySQL Server from [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
2. During installation, set a root password (remember this password!)
3. Optionally install MySQL Workbench for GUI database management

### Step 2: Create Database

Open MySQL Workbench or MySQL Command Line and run:

```sql
CREATE DATABASE studentmgt_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Step 3: Install Python Dependencies

Navigate to the project directory and install required packages:

```bash
cd studentmgt
pip install -r requirements.txt
```

**Note for Windows users**: If `mysqlclient` installation fails, you may need to:
1. Download the appropriate `.whl` file from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
2. Install it using: `pip install mysqlclient-X.X.X-cpXX-cpXX-win_amd64.whl`

### Step 4: Configure Database Settings

Open `studentmgt/settings.py` and update the database configuration with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studentmgt_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',  # Change this!
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

### Step 5: Run Migrations

Create database tables by running:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Admin)

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### Step 7: Create Initial Data (Optional)

You can add some initial courses through the Django admin panel or using the web interface.

### Step 8: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## Usage

### User Registration & Login

1. Navigate to `http://127.0.0.1:8000/`
2. Click "Sign Up" to create a new account
3. Fill in your details and create an account
4. Login with your email and password

### Managing Students

1. After logging in, go to the "Students" page
2. Click "➕ Add Student" to add a new student
3. Fill in student details (name, email, age, course)
4. Use "Edit" to modify student information
5. Use "Delete" to remove students

### Managing Courses

1. Go to the "Courses" page from the sidebar
2. Click "➕ Add Course" to create a new course
3. Enter the course name and save
4. Courses can be deleted if no longer needed

### Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` using your superuser credentials for advanced management options.

## Database Structure

### Tables Created

1. **students_user**: Custom user model for authentication
2. **students_course**: Course information
3. **students_student**: Student records linked to courses
4. Plus Django's default tables (auth, sessions, etc.)

## Project Structure

```
studentmgt/
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── students/                      # Main application
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── urls.py                    # URL routing
│   ├── forms.py                   # Django forms
│   ├── admin.py                   # Admin configuration
│   └── ...
└── studentmgt/                    # Project settings
    ├── settings.py                # Django settings (database config here)
    ├── urls.py                    # Main URL configuration
    ├── templates/                 # HTML templates
    │   ├── index.html             # Login page
    │   ├── signup.html            # Registration page
    │   ├── dashboard.html         # Dashboard
    │   ├── students.html          # Student list
    │   ├── add-student.html       # Add student form
    │   ├── edit-student.html      # Edit student form
    │   ├── courses.html           # Courses page
    │   ├── forgot.html            # Forgot password
    │   └── logout.html            # Logout page
    └── ...
```

## Troubleshooting

### MySQL Connection Error

If you get a connection error:
1. Verify MySQL server is running
2. Check username and password in `settings.py`
3. Ensure the database `studentmgt_db` exists
4. Check if the MySQL port (3306) is correct

### mysqlclient Installation Issues

On Windows, if pip install fails:
```bash
# Install Visual C++ Build Tools first, or use pre-built wheel
pip install mysqlclient-X.X.X-cpXX-cpXX-win_amd64.whl
```

### Migration Errors

If migrations fail:
```bash
# Reset migrations (use with caution)
python manage.py migrate --run-syncdb
```

### Port Already in Use

If port 8000 is busy:
```bash
python manage.py runserver 8080
```

## Security Notes

⚠️ **Important**: This is a development setup. For production:
1. Set `DEBUG = False` in settings.py
2. Change the `SECRET_KEY`
3. Use environment variables for sensitive data
4. Set proper `ALLOWED_HOSTS`
5. Use HTTPS
6. Configure proper password validators
7. Set up proper authentication backends

## Technologies Used

- **Backend**: Django 5.1.4
- **Database**: MySQL 8.0+
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Authentication**: Django's built-in auth system

## Features in Detail

### Authentication System
- Custom user model using email as username
- Secure password hashing
- Session-based authentication
- Login/Logout functionality

### Student Management
- CRUD operations (Create, Read, Update, Delete)
- Form validation (client and server-side)
- Email uniqueness validation
- Age validation

### Course Management
- Add/Delete courses
- Course name uniqueness
- Courses linked to students via foreign key

### Dashboard
- Real-time count of students and courses
- Quick navigation links
- Responsive design

## License

This project is open-source and available for educational purposes.

## Support

For issues and questions:
1. Check the Troubleshooting section
2. Verify all installation steps were followed
3. Check MySQL server status
4. Review Django logs for error details

---

**Developed with ❤️ using Django and MySQL**
