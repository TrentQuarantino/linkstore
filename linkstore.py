import streamlit as st
import datetime
import duck_utils as du
import re

du.create_table()
uro = []
cat_opt = ["Database", "Streamlit", "Python", "Fluter", "English", "Music"]
st.set_page_config(layout="wide")
colu1, colu2 = st.columns(2)
with colu1:
  st.title(":mag: Link Store")
with colu2:
  st.header("Store your link in DuckDb database")
col1, col2 = st.columns([3,3], border=False)
with col1:
  with st.expander("About this app"):
    st.write('This app store, retry and show your link')
  with st.form("entry_form", clear_on_submit=True):
    oggi = datetime.datetime.now()
    st.write("Today's Links &nbsp;&nbsp; ", oggi.strftime("%c"))
    tod_date = oggi.strftime("%c")

    cat = st.selectbox("Choose a Category", cat_opt,  key='category')
    tit = st.text_input("Paste the article's Title")
    url = st.text_input('Paste link URL', 'https://youtu.be/JwSS70SZdyM', key='url')
    uro = url.split("=")

    submitted = st.form_submit_button("Save Data")
    if submitted:
      st.write(f"Data: {tod_date}")
      st.write(f"Category: {cat}")
      st.write(f"Title: {tit}")
      st.write(f"URL: {url}")
      #x = re.sub("watch\?v\=", "embed/", url)
      #print(x)
      #st.success("Data Saved!")
      du.save_links(tod_date, cat, tit, url)
      st.success(f"Data Saved")

  
    #li = du.show_all()
    #st.dataframe(li,use_container_width=True, hide_index=True, column_config={1:'data', 2:'category', 3:'title', 4:'link'})
    #st.table(li)
  with col2:
   # VIDEO_URL = "https://www.youtube.com/watch?v=k3DBmAlUh1A"
    #st.video(VIDEO_URL)
    
    col2.markdown(
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

st.header("Show Links stored")
sub = st.button("Show")
if sub:
  du.show_all()

#  streamlit run linkstore.py --theme.base dark
# streamlit config set [theme]
# https://stackoverflow.com/questions/71722979/how-to-use-a-python-variable-inside-streamlit-markdown
# import re

#Replace all white-space characters with the digit "9":

#txt = "https://www.youtube.com/watch?v=VEHnHID4vyA"
#x = re.sub("watch\?v\=", "embed/", txt)
#print(x)