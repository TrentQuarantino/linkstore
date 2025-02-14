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
    lidf = st.dataframe(li, use_container_width=True, hide_index=True, column_config={"link":st.column_config.LinkColumn()})
    return lidf
  
def search_by_keywords(keywords):
  with duckdb.connect(DBNAME) as conn:
    query = "SELECT * FROM links WHERE title LIKE '%{s}%'".format(s=keywords)
    sear = conn.sql(query)
    search_res = st.dataframe(sear, use_container_width=True,hide_index=False, column_config={"link":st.column_config.LinkColumn()})
    return search_res
  
def update_title(new_name, link):
  with duckdb.connect(DBNAME) as conn:
    queryUp = "UPDATE links SET title = '{n}' WHERE link = '{l}'".format(n=new_name, l=link)
    conn.execute(queryUp)
