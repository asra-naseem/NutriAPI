# NutriAPI
# Smoothie API Documentation

## Overview

The Smoothie API is a RESTful service that provides endpoints for creating, reading, updating, and deleting smoothie recipes and their ingredients. Built with Django and Django REST Framework, the API offers a reliable and scalable solution for managing your smoothie data.

## Features

- **List All Smoothies**: Retrieve a list of all available smoothie recipes.
- **Retrieve a Smoothie**: Fetch details of a single smoothie by its ID.
- **Create a New Smoothie**: Add a new smoothie recipe.
- **Update a Smoothie**: Modify details of an existing smoothie.
- **Delete a Smoothie**: Remove a smoothie from the database.
- **Ingredient Management**: Handle CRUD operations for smoothie ingredients.

## Technologies Used

- Django
- Django REST Framework
- Python

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/smoothie-api.git
    ```
2. Navigate to the project folder:
    ```bash
    cd smoothie-api
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```


    ```



Feel free to customize this README file according to your project's requirements. A well-documented README can go a long way in explaining how to use and contribute to your project.
