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
