# Django Blog App Project

A comprehensive blog application built with Django, designed to provide a seamless blogging experience with powerful features.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts
- Commenting system for each post
- Rich text editor for creating posts
- Tagging system for posts
- User profiles with bio and avatar
- Responsive design for mobile and desktop
- Pagination for blog posts
- Search functionality for posts

## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Virtualenv

### Installation Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/servetisikli/django-blog-app-project.git
    ```

2. Navigate to the project directory:

    ```sh
    cd django-blog-app-project
    ```

3. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```sh
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```sh
    python manage.py runserver
    ```

8. Open your browser and visit `http://127.0.0.1:8000` to see the application in action.

## Usage

1. Register a new account or log in with an existing account.
2. Create a new blog post using the rich text editor.
3. Add tags to your posts to categorize them.
4. Comment on posts and interact with other users.
5. Manage your profile, including updating your bio and avatar.
