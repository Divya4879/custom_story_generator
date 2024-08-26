from mistralai import Mistral
import streamlit as st


background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM7b3QnJ8IX1do_6GkwIO2lXMOjHA2Rxns7frOkEBajW7F6Lnf5wpEJ6j-D07V0637k7U&usqp=CAU");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


api_key = "4J5FV9NMfls7auEarUq9WYuVfEp1KDB1"
model = "mistral-large-latest"

title = '<h1 style="font-family:serif;color:#f2ecfa; font-size: 48px;">Your customized story generator</h1>'
st.markdown(title, unsafe_allow_html=True)

subheading1 = '<h2 style="color:#f5f2f6; font-size: 36px;">Generate a customized story</h1>'
st.markdown(subheading1, unsafe_allow_html=True)


words = st.number_input("Enter the approx no. of words in the story", 100, 800, "min", 100)

theme = st.selectbox("Theme: ",
                     ['Romance', 'Horror', 'Adventurous','Fantasy','Fanfiction'])


genre = st.text_input("Enter the genre",value=None,placeholder="Happy/Tragic/Hopeful Ending, Plot-twist....")

if theme== 'Fanfiction':
    reference = st.text_input("Enter the name of the book/movie/drama on which you want it based on: ",)

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
    story=chat_response.choices[0].message.content
    
    title = client.chat.complete(
        model=model,
        messages=[{"role":"user", "content":f"What is the the most appropriate title of the {chat_response}?"}]
    )
    st.header(title.choices[0].message.content.split(".")[0].split('**"')[1].strip('**"'))
    st.text_area(label ="",value=story,height=400)
    