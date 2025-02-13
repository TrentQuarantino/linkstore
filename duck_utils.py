import duckdb
import streamlit as st

DBNAME = 'links.db'
def create_table():
  with duckdb.connect(DBNAME) as conn:
    conn.sql('''CREATE TABLE IF NOT EXISTS links(
      data VARCHAR,
      category VARCHAR,
      title VARCHAR,
      link VARCHAR, 
      )'''
    )

def save_links(data, category, title, url):
  with duckdb.connect(DBNAME) as conn:
    query1 = "INSERT INTO links VALUES (?,?,?,?)"
    conn.execute(query1, [data, category, title, url])

def show_all():
  with duckdb.connect(DBNAME) as conn:
    #li = pd.read_sql_query("SELECT * FROM links",conn)
    li = conn.sql("SELECT * FROM links")#.fetchall()
    #li.fetchall()
    print(li.fetchall())
    lidf = st.dataframe(li, use_container_width=True, hide_index=True)
    return lidf
  
# TODO Link Button in dataframe
# modify creation of db     