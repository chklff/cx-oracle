from flask import Flask, request, jsonify
import cx_Oracle
import os

app = Flask(__name__)

# Set Oracle client directory relative to the script file
oracle_client_dir = os.path.join(os.path.dirname(__file__), 'instantclient_21_11')
os.environ["LD_LIBRARY_PATH"] = oracle_client_dir
os.environ["ORACLE_HOME"] = oracle_client_dir

# You might need to reconfigure environment variables for Python to recognize them.
# This can depend on your operating system and setup.

ORACLE_DSN = cx_Oracle.makedsn('165.22.180.189', '1521', 'ORCLCDB')
CONNECTION = cx_Oracle.connect('system', 'iDx16reA2R9#i', ORACLE_DSN)

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
