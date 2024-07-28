# OTP Validation FastAPI Project

This project is a FastAPI application for OTP (One-Time Password) validation. It provides endpoints for generating OTP, creating users, updating passwords, and generating access tokens.


## Project Structure
- **alembic**: Contains migration scripts for managing database schema changes using Alembic.
  - `env.py`: Configuration file for Alembic migrations.
- **main.py**: Entry point of the FastAPI application.
- **routes**: Contains API routers.
  - `auth_controller.py`: API routes for user authentication and token generation.
  - `user_controller.py`: API routes for user-related operations like user creation, OTP generation, and password updates.
- **services**: Contains business logic for various operations.
  - `create_new_user.py`: Logic for creating new users.
  - `change_user_password.py`: Logic for modifying user passwords.
  - `generate_user_otp.py`: Logic for generating and accessing OTPs.
  - `generate_token.py`: Logic for generating access tokens after successful OTP validation.
- **utils**: Contains utility functions used across the project.
  - `get_current_user.py`: Utility for retrieving current user information from JWT token.
  - `get_db.py`: Utility for managing database sessions.
  - `get_otp.py`: Utility for generating random OTPs.
  - `get_user.py`: Utility for retrieving user information from the database.
  - `password_security.py`: Utility for hashing passwords and verifying password hashes.
  - `send_otp.py`: Utility for sending OTPs via email.
  - `token_management.py`: Utility for JWT token handling, including token creation and verification.
- **database**: Contains database-related files.
  - `database_setup.py`: Setup for SQLAlchemy ORM and database session management.
- **models**: Contains SQLAlchemy models for database tables.
  - `UserData.py`: Model for user data.
- **schemas**: Contains Pydantic models for request/response data validation.
  - `oauth_schemas.py`: Pydantic models for authentication-related data.
  - `user_schemas.py`: Pydantic models for user-related data.

## Endpoints
- **Generate Token**: `/generate-token` - POST method to generate JWT access tokens.
- **Create User**: `/user/create_user` - POST method to create new user accounts.
- **OTP Generation**: `/user/otp_generation` - POST method to generate OTPs.
- **Update Password**: `/user/update_password` - PUT method to update user passwords.

## Dependencies

- **FastAPI**: Web framework for building APIs with Python.
- **Uvicorn[standard]**: ASGI server for running FastAPI applications.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Psycopg2**: PostgreSQL adapter for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Pydantic[email]**: Pydantic extension for email validation.
- **Python-Jose[cryptography]**: JSON Web Tokens (JWT) implementation in Python.
- **Passlib[bcrypt]**: Password hashing library for Python.
- **Alembic**: Database migration tool for SQLAlchemy.

  
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

4. Run 'main.py' file or Run the application using uvicorn in cmd:

    ```bash
    uvicorn main:app --reload
    ```

5. Access the API documentation at http://127.0.0.1:8000/docs to explore available endpoints and interact with the application.


