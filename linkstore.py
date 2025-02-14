import requests
import datetime
import streamlit as st
import duck_utils as du

def get_data():
  response = requests.get('http://localhost:8888/to_app').json()  
  return response['title'], response['url']

du.create_table()

uro = []
cat_opt = ["Database", "Streamlit", "Python", "Fluter", "Angular", "English", "Music"]
st.set_page_config(layout="wide")
# headert
colu1, colu2 = st.columns(2)
with colu1:
  st.title(":mag: Link Store")
  st.button('get data')
with colu2:
  st.header("Store your link in DuckDb database")

col1, col2 = st.columns([3,3], border=False)
# insertion form
with col1:
  with st.form("entry_form", enter_to_submit=False, clear_on_submit=True):
    oggi = datetime.datetime.now()
    tod_date = oggi.strftime("%c")
    st.write("Today's Links &nbsp;&nbsp; ", tod_date)
    
    cat = st.selectbox("Choose a Category", cat_opt,  key='category')
    # get the data from browser 
    title, url = get_data()

    url = st.text_input("",url)
    mod_title = st.text_input('Edit if the title is not correct or imprecise', title)
    if mod_title != title:
      title =  mod_title

    subm = st.form_submit_button('Save Data')
    if subm:
      du.save_links(tod_date, cat, title, url)
      st.success("You succesfully saves this data: ")
      st.write(f"Data: {tod_date}")
      st.write(f"Category: {cat}")
      st.write(f"Titolo: {title}")
      st.write(f"URL: {url}")

  with col2:
    if url.find("youtube") > 0:
      print(True)
      uro = url.split("=")
      ur = uro[-1]
    else:
      print(False)
      uro = "oMHLkcc9I9c"
    
    st.markdown(
      """
      <div style="width: 600px; height: 400px; background-color: #ccc; border: 1px solid black; 
                  transform: perspective(500px) rotatey(-15deg);">
                  <iframe width="600" height="400" 
                    src="https://www.youtube.com/embed/{ur}">
                  </iframe>
      </div>
      """.format(ur = uro[-1]),
      unsafe_allow_html=True,
    )
st.container(height=100, border=False)
tab1, tab2, tab3= st.tabs(["Show All", "Search", "Update"])
with tab1:  
  st.header("Show Links stored")
  sub = st.button("Show")
  if sub:
    du.show_all()
with tab2:
  st.header("Search from Links stored by keywords")
  keywords = st.text_input("Keyword to search")
  sub = st.button("Search")
  if sub:
    du.search_by_keywords(keywords)
with tab3:
  st.header("Update Links stored")
  new_name = st.text_input("Insert new title")
  link = st.text_input("Insert old title")
  sub = st.button("Update")
  if sub:
    print(new_name, link)
    du.update_title(new_name, link)
    
