from flask import Flask, request, jsonify
import cx_Oracle

app = Flask(__name__)



ORACLE_DSN = cx_Oracle.makedsn('165.22.180.189', '1521', 'ORCLCDB')
### ORACLE_DSN = cx_Oracle.makedsn('165.22.180.189', '1521', service_name='ORCL')

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
