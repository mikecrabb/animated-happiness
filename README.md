# animated-happiness

This project contains various Flask API demos, each demonstrating different features and functionalities of building APIs with Flask and Flask-RESTful.

## Setup

To get started with this project in GitHub Codespaces, follow these steps:

1. **Open Codespaces:**
   - Click on the `Code` button in your repository.
   - Select `Open with Codespaces` and create a new Codespace.

2. **Install Flask and Flask-RESTful:**
   - Open the terminal in Codespaces.
   - Run the following commands to install the required packages:
     ```bash
     pip install Flask Flask-RESTful
     ```

## Demos

### 01_firstAPI
This demo showcases a simple "Hello, World!" API using Flask and Flask-RESTful.

- **File:** `01_firstAPI/app.py`
- **Endpoint:** `GET /`
- **Description:** Returns a JSON message `{"message": "Hello, World!"}`.

### 02_CRUD_API
This demo demonstrates a basic CRUD (Create, Read, Update, Delete) API for managing tasks.

- **File:** `02_CRUD_API/app.py`
- **Endpoints:**
  - `GET /task/<int:task_id>`: Retrieve a task by ID.
  - `POST /task/<int:task_id>`: Create a new task.
  - `PUT /task/<int:task_id>`: Update an existing task.
  - `DELETE /task/<int:task_id>`: Delete a task by ID.
- **Description:** Provides endpoints to create, read, update, and delete tasks.

### 03_EasyMiddleware
This demo shows how to use middleware in Flask to log incoming requests.

- **File:** `03_EasyMiddleware/app.py`
- **Endpoint:** `GET /`
- **Description:** Logs incoming requests and returns a JSON message `{"message": "Hello, World!"}`.

### 04_API_Keys
This demo illustrates how to secure API endpoints using API keys.

- **Files:**
  - `04_API_Keys/app.py`
  - `04_API_Keys/readme.md`
- **Endpoints:**
  - `POST /get-api-key`: Generate a new API key for a user.
  - `GET /secure-data`: Access secured data (requires a valid API key).
- **Description:** Demonstrates generating API keys and securing endpoints with them.

### 05_HATEOAS
This demo demonstrates how to implement HATEOAS (Hypermedia as the Engine of Application State) in a Flask API.

- **File:** `05_HATEOAS/app.py`
- **Endpoints:**
  - `GET /team`: Retrieve all teams with HATEOAS links.
  - `GET /team/<int:team_id>`: Retrieve a specific team by ID with HATEOAS links.
  - `GET /driver`: Retrieve all drivers with HATEOAS links.
  - `GET /driver/<int:driver_id>`: Retrieve a specific driver by ID with HATEOAS links.
- **Description:** Provides endpoints to retrieve teams and drivers with HATEOAS links.

Each demo is self-contained and can be run independently to explore the specific feature it demonstrates.