# Oracle Flask API

This repository contains a Flask application that interfaces with an Oracle database using `cx_Oracle`. It allows executing SQL queries through HTTP requests.

## Description

The Flask application is set up to connect to an Oracle database using environment variables to specify the Oracle client directory. It exposes a single endpoint `/query` that accepts SQL queries in JSON format via POST requests and returns the query results in JSON format.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running:
pip install Flask cx_Oracle

markdown
Copy code
4. Download the appropriate Oracle Instant Client for your system and place it in the `instantclient_21_11` directory within your project folder.

## Setting Up Oracle Instant Client

The application requires Oracle Instant Client to connect to the Oracle database. Follow these steps to download, unpack, and set up the client for your operating system, including setting the necessary environment variables.

### For Windows

1. **Download the Oracle Instant Client:**
   - Visit the [Oracle Instant Client Downloads page](https://www.oracle.com/database/technologies/instant-client.html).
   - Select "Instant Client for Microsoft Windows (x64)".
   - Download `instantclient-basic-windows.x64-21.13.0.0.0dbru.zip` (or the latest version available).

2. **Unpack the ZIP File:**
   - Unpack the ZIP file to your desired location, e.g., `C:\oracle\instantclient_21_13`.

3. **Set Environment Variables:**
   - **PATH:** Add the Instant Client directory to the system's PATH environment variable.
   - **LD_LIBRARY_PATH** and **ORACLE_HOME** (For the application to recognize the Instant Client location, these variables are typically used in Linux/Unix environments. For Windows, setting the PATH is usually sufficient, but if you're adapting the application for cross-platform use, you might need equivalent settings.)

   **Setting PATH in Windows:**
   - Right-click on 'This PC' or 'Computer' on the desktop or in File Explorer, then click 'Properties'.
   - Click 'Advanced system settings'.
   - In the System Properties window, click the 'Environment Variables...' button.
   - In the Environment Variables window, find the 'Path' variable under 'System variables', select it, and click 'Edit...'.
   - Click 'New' and add the path to the directory where you unpacked the Instant Client, e.g., `C:\oracle\instantclient_21_13`.
   - Click 'OK' on all windows to apply the changes.

### Additional Steps for the Flask Application

# Set Oracle client directory relative to the script file for cross-platform compatibility
oracle_client_dir = 'YOUR_INSTANT_CLIENT_DIRECTORY_PATH'  # For Windows, it might be 'C:\\oracle\\instantclient_21_13'
os.environ["LD_LIBRARY_PATH"] = oracle_client_dir  # Mainly for Linux/Unix
os.environ["ORACLE_HOME"] = oracle_client_dir  # Mainly for Linux/Unix

# Make sure these lines are executed before importing cx_Oracle or creating a cx_Oracle connection



## Usage

1. Set up the Oracle client directory in the script or as environment variables.
2. Update the `ORACLE_DSN` and `CONNECTION` variables with your Oracle database credentials and DSN.
3. Run the Flask application:
python <script_name>.py

css
Copy code
4. Make a POST request to `http://<your_host>:5478/query` with a JSON body containing the SQL query:
```json
{
  "sql": "YOUR_SQL_QUERY_HERE"
}
```

Warning
The script contains sensitive information, such as database credentials. Never commit sensitive information like this to a public repository. Use environment variables or a secure vault to handle credentials and sensitive information.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.

vbnet
Copy code

**Notes:**
- Replace `<script_name>.py` with the actual name of your Python script.
- Replace `<your_host>` with the actual host name or IP address where your Flask application is running.
- Remember to remove or replace sensitive information like database credentials before
