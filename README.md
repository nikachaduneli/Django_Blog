# Django Blog

This is a simple web application built using Django for creating a blogging platform. It allows users to create, edit, and delete blog posts. Users can register and log in to manage their own posts, while the admin can manage all posts and users.

## Features

- User authentication (registration, login, logout)
- CRUD (Create, Read, Update, Delete) operations for blog posts
- Admin panel for managing posts and users

## Installation

To install and run the project locally:

1. Clone the repository:  
   `git clone https://github.com/nikachaduneli/Django_Blog.git`
   
2. Install the dependencies:  
   `pip install django django-crispy-forms django-cleanup pillow`
   
3. Apply database migrations:  
   `python manage.py migrate`
   
4. Create a superuser to access the admin interface:  
   `python manage.py createsuperuser`
   
5. Run the development server:  
   `python manage.py runserver`

Access the app at `http://127.0.0.1:8000`.

## License

This project is open-source and available under the MIT License.

Built with Django, a powerful Python web framework.
