import streamlit as st
import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()


background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTA4L3N0YXJ0dXBpbWFnZXNfYmx1ZV9wdXJwbGVfc2t5X3doaXRlX2Nsb3Vkc19iYWNrZ3JvdW5kX2ltYWdlX2dyYV9jZDNlMTI5My03MjBkLTQ5ZTgtOTZkYy0yMTAyY2RhN2I2MzlfMS5qcGc.jpg");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
    opacity:0.9
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


title = '<h1 style="font-family:serif;color:#52327a; font-size: 48px">Your customized story generator</h1>'
st.markdown(title, unsafe_allow_html=True)

subheading1 = '<h2 style="color:#52327a; font-size: 40px;font-style:italic">Generate a customized story</h1>'
st.markdown(subheading1, unsafe_allow_html=True)


text = f":blue[Enter the approx no. of words in the story]"
words = st.number_input(text, 400, 1500, "min", 400)


t = n = f":blue[Theme]"
theme = st.selectbox(t,
                     ['Romance', 'Horror', 'Adventurous','Fantasy','Fanfiction','Angst'])



g = f":blue[Enter the genre]"
genre = st.text_input(g,value=None,placeholder="Happy/Tragic/Hopeful Ending, Plot-twist....")

if theme== 'Fanfiction':
    r = f":blue[Enter the name of the book/movie/drama on which you want it based on]"
    reference = st.text_input(r)


api_key = os.environ.get("MISTRAL_API_KEY")
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

if theme=='Fanfiction':
    chat_response = client.chat.complete(
    model=model,
    messages=[{"role":"system", "content":f"You're a world renowned author. Write a story in about {words} words on the theme of {theme}, also it should have the genre of {genre} and it must be based on {reference}."}]
)

else:
    chat_response = client.chat.complete(
        model=model,
        messages=[{"role":"system", "content":f"You're a world renowned author. Write a story in about {words} words on the theme of {theme}, also it should have the genre of {genre}."}]
    )



if st.button("Generate my story"):
    
    story = chat_response.choices[0].message.content
    title = client.chat.complete(
        model=model,
        messages=[{"role":"user", "content":f"What is the the most appropriate title of the {chat_response}?"}]
    )
    title = title.choices[0].message.content.split(".")[0].split('**"')[1].strip('"**')
    title = f":blue[{title}]"
    st.header(title)
    st.text_area(label ="",value=story,height=400)
    
