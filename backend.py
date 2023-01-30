from flask import Flask,  render_template
from psycopg2 import connect

app = Flask(__name__)
      
conn = connect(
    host='172.17.0.2', 
    port=5432,
    user="webappdev",
    password="1234",
    dbname="webappdev"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usernames', methods=['GET'])
def get_usernames():
    cur = conn.cursor()
    cur.execute("SELECT * from users;")
    usernames = cur.fetchall()
    return usernames
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
