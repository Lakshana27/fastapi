# OTP Validation FastAPI Project

This project is a FastAPI application for OTP (One-Time Password) validation. It provides endpoints for generating OTP, creating users, updating passwords, and generating access tokens.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables by creating a `.env` file in the root directory and adding the following variables:

    ```plaintext
    DB_PATH = <database_connection_string>
    SECRET_KEY = <your_secret_key>
    ALGORITHM = <your_preferred_algorithm>
    ACCESS_TOKEN_EXPIRE_MINUTES = <token_expiry_duration>
    OTP_TIME_LIMIT = <otp_time_limit>
    SENDER_EMAIL = <your_email>
    SENDER_PASSWORD = <your_email_password>
    ```

4. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

## Project Structure

- **main.py**: Entry point of the FastAPI application.
- **routes**: Contains API routers.
  - **auth_controller.py**: API endpoints for authentication, such as generating access tokens.
  - **user_controller.py**: API endpoints for user-related operations, such as creating users and updating passwords.
- **services**: Contains business logic.
  - **access_otp.py**: Logic for accessing OTP.
  - **create_new_user.py**: Logic for creating new users.
  - **modify_password.py**: Logic for modifying passwords.
  - **generate_access_token.py**: Logic for generating access tokens.
- **utils**: Contains utility functions.
  - **get_current_user.py**: Function to get the current user from the token.
  - **get_otp.py**: Function to generate OTP.
  - **get_session.py**: Function to get the database session.
  - **get_user.py**: Function to retrieve user information from the database.
  - **jwt_handling.py**: Functions for JWT token handling.
  - **password_auth.py**: Functions for password hashing and verification.
  - **send_otp.py**: Function to send OTP via email.
- **database**: Contains database setup and models.
  - **orm_setup.py**: Database engine setup.
- **models**: Contains SQLAlchemy models.
  - **UserTable.py**: Model for the user table.
- **schemas**: Contains Pydantic schema definitions.
  - **auth_schemas.py**: Defines authentication-related schemas.
  - **user_schemas.py**: Defines user-related schemas.

## Dependencies

- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- uvicorn: ASGI server for running FastAPI applications.
- python-dotenv: Python library for parsing environment variables from .env files.
- passlib: Password hashing library.
- pyjwt: JSON Web Token implementation.
