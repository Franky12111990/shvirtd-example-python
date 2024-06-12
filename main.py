from flask import Flask
from flask import request
import os
import mysql.connector
from datetime import datetime

app = Flask(__name__)
db_host = os.getenv('DB_HOST', 'db')
db_user = os.getenv('DB_USER', 'app')
db_database = os.getenv("MYSQL_DATABASE")
db_password = os.getenv('DB_PASSWORD', 'QwErTy1234')
db_name = os.getenv('DB_NAME', 'virtd')

# Подключение к базе данных MySQL
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    autocommit=True
)
cursor = db.cursor()

# SQL-запрос для создания таблицы в БД
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {db_database}.requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_date DATETIME,
    request_ip VARCHAR(255)
)
"""
cursor.execute(create_table_query)

@app.route('/')
def index():
    # Получение IP-адреса пользователя
    ip_address = request.headers.get('X-Forwarded-For')

    # Запись в базу данных
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO requests (request_date, request_ip) VALUES (%s, %s)"
    values = (current_time, ip_address)
    cursor.execute(query, values)
    db.commit()

    return f'TIME: {current_time}, IP: {ip_address}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

