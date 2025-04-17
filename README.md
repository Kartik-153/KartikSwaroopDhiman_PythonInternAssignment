# Kartik Swaroop Dhiman — Python Intern Assignment 🚀

This project is a complete solution for the provided backend + system simulation assignment. It includes:

- A Flask-based backend API (Task 1)
- PostgreSQL database integration (Task 2)
- Android Emulator automation to simulate a virtual Android device (Task 3)
- Networking logic to connect that virtual system to the backend (Task 4)

---

## ✅ Task 1 & 2: Backend API + PostgreSQL Database

### 📌 Features

- `POST /add-app`: Add app metadata
- `GET /get-app/<id>`: Get app by ID
- `DELETE /delete-app/<id>`: Delete app by ID

### 🔧 Tech Stack

- Python 3
- Flask
- PostgreSQL
- psycopg2

### 📂 Setup Instructions

1. Install dependencies and make a virtual enviroment (https://code.visualstudio.com/docs/python/environments):
    ```bash
    pip install -r requirements.txt
    ```

2. Create a PostgreSQL DB and table and also give any privilege to the database:

    ```sql
    CREATE DATABASE app;

    \c apps

    CREATE TABLE info (
        id SERIAL PRIMARY KEY,
        app_name TEXT NOT NULL,
        version TEXT NOT NULL,
        description TEXT NOT NULL
    );
    ```

3. Create `.env` file in:

    ```env
    DB_NAME=<android_system>
    DB_USER=<your_user>
    DB_PASSWORD=<your_password>
    DB_HOST=<localhost>
    DB_PORT=<5432>
    ```

4. Run the API:

    ```bash
    python main.py
    ```

5. Access it at: `http://127.0.0.1:5000`

---

## ✅ Task 3 & 4: Virtual Android System Simulation and Basic Networking

### 📌 Features

- Launches an Android emulator via AVD
- Waits for full boot
- Installs an APK - depends if APK is already installed
- Extracts and logs:
  - OS version
  - Device model
  - Available memory
  - Installed app version
- Stores the data into database with the API 

### 📦 Prerequisites

- Android Studio + AVD created
- `adb` and `emulator` available in your system or full paths defined in script


## 🏳️ Run 

- Activate virtual enviroment by entering 
```bash
 ./.venv/scripts/activate
```
- Make two terminal and :
  - In first terminal do
  ```bash
    cd task1_2
    python main.py
  ```

  - In second terminal run:
  ```bash
    cd task3_4
    python main.py    
    ```
