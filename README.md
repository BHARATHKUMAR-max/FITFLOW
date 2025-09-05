# FitFlow - Fitness & Supplement E-commerce Website

FitFlow is a fully-functional e-commerce website for fitness supplements and products built with Django, HTML, CSS, and JavaScript. It includes features for browsing products, managing a shopping cart, checkout process, and order management.

## Features

- Responsive modern UI with Bootstrap 5
- Product catalog with categories
- Search functionality
- Advanced filtering and sorting
- Shopping cart and checkout
- User authentication
- Order tracking
- Admin dashboard

## Technology Stack

- **Backend**: Django 5.2
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Database**: SQLite (default)

## Installation & Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fitflow.git
   cd fitflow
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Open your browser and go to http://127.0.0.1:8000/

## Admin Access

Access the admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created.

## Adding Products

1. Log in to the admin panel
2. Create categories first
3. Add products to the categories
4. Add product images

## License

This project is licensed under the MIT License - see the LICENSE file for details. 