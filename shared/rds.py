import pymysql
from shared.config import RDS_HOST, RDS_USER_NAME, RDS_USER_PW, RDS_DB

def write_db(sellings):
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS sellings")
    cursor.execute("CREATE TABLE sellings (\
        id int,\
        title text,\
        views text,\
        date text,\
        comments text,\
        likes text\
    )")
    for selling in sellings:
        cursor.execute(f"INSERT INTO sellings VALUES({selling['id']},\"{selling['title']}\",\"{selling['views']}\",\"{selling['date']}\",\"{selling['comments']}\",\"{selling['likes']}\")")
    conn.commit()

def read_db():
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sellings")
    conn.commit()