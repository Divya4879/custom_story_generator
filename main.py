import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai



genai.configure(api_key=os.environ["GEMINI_API_KEY"])
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
                     ['Horror', 'Adventurous','Fantasy','Fanfiction','Angst','Rags-to-Riches','Hardwork','Success'])



g = f":blue[Enter the genre]"
genre = st.text_input(g,value=None,placeholder="Happy/Tragic/Hopeful Ending, Plot-twist....")

if theme== 'Fanfiction':
    r = f":blue[Enter the name of the book/movie/drama on which you want it based on]"
    reference = st.text_input(r)


model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction="You're a world renowned author. You've this experience for over 20 years."
)

try:
    if theme=='Fanfiction':
        response = model.generate_content(f" Write a story in about {words} words on the theme of {theme}, also it should have the genre of {genre} and it must be based on {reference}."
    )

    else:
        response = model.generate_content(f"You're a world renowned author. Write a story in about {words} words on the theme of {theme}, also it should have the genre of {genre}."
        )



    if st.button("Generate my story"):
        
        story = response.text
        title = model.generate_content(f"What is the the most appropriate title of the {response}?"
        )
        title = title.text.split('"')[1]
        title = f":blue[{title}]"
        st.header(title)
        st.text_area(label ="",value=story,height=400)
        

    response = model.generate_content(
        "Tell me a story about a magic backpack.",
        generation_config=genai.types.GenerationConfig(
            
            candidate_count=1,
            stop_sequences=["x"],
            max_output_tokens=20,
            temperature=1.0,
        ),
    )

    print(response.text)
except:
    msg = '<h1 style="font-family:serif;color:#0047AB; font-size: 30px">Enter another genre.</h1>'
    # st.markdown(title)
    st.write(msg, unsafe_allow_html=True)
