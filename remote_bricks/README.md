# User Management API using FastAPI and MongoDB

This is a FastAPI-based user management API that provides endpoints for registering, logging in, linking IDs, and deleting users.

## Features

* User registration with email and password
* User login with email and password
* Linking of IDs to existing users
* Joining of user data with linked IDs
* Deletion of users and associated data

## Technology Stack

* FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
* Pydantic: A library for building robust, type-safe data models in Python.
* MongoDB: A NoSQL database for storing user data.
* Passlib: A password hashing library for securely storing passwords.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/user-management-api.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with the following variables:
	* `DB_PATH`: The MongoDB connection string
	* `DB_NAME`: The name of the MongoDB database
	* `USERS_COLLECTION`: The name of the users collection
	* `LINKING_IDS_COLLECTION`: The name of the linking IDs collection
4. Run the application: `uvicorn main:app --host 0.0.0.0 --port 8000`

## API Endpoints

### Register User

* **POST /users/register**
	+ Request Body: `RegisterRequest` model
	+ Response: `{"message": "User registered successfully", "id": str}`

### Login User

* **POST /users/login**
	+ Request Body: `LoginRequest` model
	+ Response: `{"message": "User logged in successfully"}`

### Link ID

* **POST /users/link_id**
	+ Request Body: `LinkingIDRequest` model
	+ Response: `{"message": "Linked ID linked successfully"}`

### Join User Data

* **GET /users/join-user-data/{user_id}**
	+ Response: `JoinResponseModel` model

### Delete User

* **DELETE /users/delete-user/{user_id}**
	+ Response: `{"message": "User deleted successfully"}`

## Contributing

Contributions are welcome! Please open a pull request to contribute to the project.
