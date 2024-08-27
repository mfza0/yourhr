# YourHR Job Search Service

## Project Overview
YourHR is a job search service that helps job seekers find ideal job roles based on their qualifications and preferences.

## Setup Instructions
1. Clone the repository.
2. Navigate to the `yourhrApp/` directory.
3. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate or venv\Scripts\activate
    pip install flask pymongo
    ```
4. Activate MongoDB locally     
5. Start the Flask server:
    ```bash
    python app.py
    ```
6. Access the web application at `http://127.0.0.1:5000`.

## Folder Structure
- `yourhrApp/templates`: Contains the HTML, CSS, and JavaScript files.
- `yourhrApp/static`: Contains the CSS files.
- `yourhrApp/`: Contains the Flask app and MongoDB configurations along with templates and static folders

## Features
- User signup form with resume upload.
- Stores user data in MongoDB.
