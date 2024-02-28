from flask import Flask, request, jsonify
import cx_Oracle
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set Oracle client directory relative to the script file
oracle_client_dir = os.getenv('ORACLE_CLIENT_DIR', os.path.join(os.path.dirname(__file__), 'instantclient_21_11'))
os.environ["LD_LIBRARY_PATH"] = oracle_client_dir
os.environ["ORACLE_HOME"] = oracle_client_dir

# Use environment variables for sensitive information
ORACLE_DSN = cx_Oracle.makedsn(*os.getenv('ORACLE_DSN').split('/'))
CONNECTION = cx_Oracle.connect(os.getenv('ORACLE_USER'), os.getenv('ORACLE_PASSWORD'), ORACLE_DSN)

@app.route('/query', methods=['POST'])
def query_oracle():
    sql = request.json.get('sql')
    cursor = CONNECTION.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in result])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5478, debug=True)
