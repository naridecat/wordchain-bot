import psycopg2
import json

conn = psycopg2.connect(host='localhost', dbname='main', user='postgres', password='PASSWORD', port='5432') # db에 접속
cur = conn.cursor()
cur.execute("select _id from public.kkutu_ko;")
row = [item[0] for item in cur.fetchall()]

open('output.json', 'w', encoding='utf-8').write(json.dumps(row, ensure_ascii=False))

conn.commit()
cur.close()
conn.close()