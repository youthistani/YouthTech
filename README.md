# YouthTech

YouthTech is a Django web application designed to manage various aspects of a technical institution. It includes features for blogging, blood donation management, user accounts, administrative tasks, and the main website content.

## Project Structure

The project is organized into several Django applications:

-   `Youthtect`: This is the main project directory, containing the core settings, URL configurations, and other project-level files.
-   `Blogs`: This app is responsible for managing blog posts, allowing administrators to create, update, and delete articles. It likely includes features for displaying blog content to users.
-   `BloodBank`: This app handles the management of blood donations and donor information. It may include functionalities for registering donors, tracking blood stock, and facilitating donation requests.
-   `accounts`: This app manages user authentication and authorization. It includes features for user registration, login, logout, and potentially profile management.
-   `admin_work`: This app is dedicated to administrative tasks and workflows. This could involve managing user accounts, overseeing content on the site, or handling specific administrative processes related to the institution.
-   `website`: This app manages the public-facing content of the website, such as the homepage, about Us page, contact information, and potentially information about programs or courses offered by the institution.

## Setup and Installation (Development)

These steps are for setting up and running the project in a development environment.

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd YouthTech
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    .env\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/` in your web browser.

## Docker (Development)

To run the application using Docker for development:

1.  **Build the Docker image:**

    ```bash
    docker build -t youthtech .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 youthtech
    ```

    The application will be accessible at `http://localhost:8000/` in your web browser.

## Production Deployment with Docker

For a production deployment, it is highly recommended to use a robust WSGI server (like Gunicorn, which is included in the Dockerfile) and a separate web server (like Nginx) for serving static/media files and acting as a reverse proxy.

**Key considerations for Production:**

*   **Environment Variables:** Set the following environment variables in your production environment:
    *   `DJANGO_SECRET_KEY`: A strong, unique secret key.
    *   `DJANGO_ALLOWED_HOSTS`: A comma-separated list of your production domains (e.g., `your_domain.com,www.your_domain.com`).
    *   `DATABASE_URL`: Your database connection string (e.g., `postgres://user:password@host:port/dbname`).

*   **Database:** Switch from SQLite to a production-ready database like PostgreSQL or MySQL.

*   **Static and Media Files:** Django is not designed to serve static and media files efficiently in production. Configure a web server (e.g., Nginx) to serve `STATIC_ROOT` and `MEDIA_ROOT` directly.

*   **HTTPS:** Ensure your application is served over HTTPS in production.

**Steps to build and run for Production:**

1.  **Build the Docker image:**

    ```bash
    docker build -t youthtech-production .
    ```

2.  **Run the Docker container (example with environment variables):**

    ```bash
    docker run -p 8000:8000 \
      -e DJANGO_SECRET_KEY='your_super_secret_key' \
      -e DJANGO_ALLOWED_HOSTS='your_production_domain.com,www.your_production_domain.com' \
      -e DATABASE_URL='postgres://user:password@host:port/dbname' \
      youthtech-production
    ```

    *Replace the example environment variable values with your actual production values.* The application will be served by Gunicorn inside the container, typically fronted by a web server like Nginx for optimal performance and security.
