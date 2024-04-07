# User Registration and Authentication with FastAPI

This project implements a user registration and authentication system using FastAPI, PostgreSQL for database management, and JWT (JSON Web Tokens) for secure authorization. It allows users to register, authenticate, manage their profiles, and access protected routes based on role-based permissions.

## Features

- **User Registration**: New users can sign up securely by providing essential details such as username, name, email, and password. User data is stored securely in a PostgreSQL database.

- **Authentication with JWT**: Authentication is handled using JSON Web Tokens (JWT), providing a secure method for users to access protected routes. JWT tokens are generated upon successful login and are used to authenticate subsequent requests.

- **Role-Based Permissions**: Role-based access control (RBAC) is implemented to manage user permissions effectively. Users can be assigned roles such as Admin or User, each with distinct access levels and privileges within the application.

- **Profile Management**: Users can update their profile information, including their name and email address, ensuring accurate user data management.

## Project Structure

- **main.py**: The main entry point of the FastAPI application, defining routes and starting the server.
  
- **routes.py**: Contains route definitions for user registration, authentication, and profile management.

- **user_services.py**: Implements user-related services such as user creation, profile updates, and activity status management.

- **oauth_services.py**: Handles user authentication and JWT token generation.

- **utils.py**: Utility functions including password hashing and token verification.

- **database.py**: Configures the PostgreSQL database connection and provides session management.

- **models.py**: Defines SQLAlchemy models for user data storage.

- **user_schemas.py**: Contains Pydantic schemas for user-related data validation and serialization.

- **oauth_schemas.py**: Defines Pydantic schemas for authentication data serialization.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>

2. Install dependecies:

   ```bash
   pip install -r requirements.txt

3. Set up environment variables:
Set up environment variables by creating a '.env' file and providing values for 'DB_PATH', 'SECRET_KEY', 'ALGORITHM', and 'ACCESS_TOKEN_EXPIRE_MINUTES'.

4. Run 'main.py' file

5. Access the API documentation at http://127.0.0.1:8000/docs to explore available endpoints and interact with the application.
