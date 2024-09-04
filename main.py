import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask


load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = Flask(__name__)


  
@app.route('/')
def index():
  f = open("template/index.html","r")
  page = f.read()
  f.close()
#   page = page.replace("{weather}",weather_codes[weather_code])
#   page = page.replace("{temp}",temp)
#   page = page.replace("{url}",url)
  return page


app.run(host='0.0.0.0', port=81)





# t = n = f":blue[Theme]"
# theme = st.selectbox(t,
#                      ['Horror', 'Adventurous','Fantasy','Fanfiction','Angst','Rags-to-Riches','Hardwork','Success'])



# g = f":blue[Enter the genre]"
# genre = st.text_input(g,value=None,placeholder="Happy/Tragic/Hopeful Ending, Plot-twist....")

# if theme== 'Fanfiction':
#     r = f":blue[Enter the name of the book/movie/drama on which you want it based on]"
#     reference = st.text_input(r)


# model=genai.GenerativeModel(
#   model_name="gemini-1.5-flash",
#   system_instruction="You're a world renowned author. You've this experience for over 20 years."
# )

# try:
#     if theme=='Fanfiction':
#         response = model.generate_content(f" Write a story in about {words} words on the theme of {theme}, also it should have the genre of {genre} and it must be based on {reference}."
#     )

#     else:
#         response = model.generate_content(f"You're a world renowned author. Write a story in about {words} words on the theme of {theme}, also it should have the genre of {genre}."
#         )



#     if st.button("Generate my story"):
        
#         story = response.text
#         title = model.generate_content(f"What is the the most appropriate title of the {response}?"
#         )
#         title = title.text.split('"')[1]
#         title = f":blue[{title}]"
#         st.header(title)
#         st.text_area(label ="",value=story,height=400)
        

#     response = model.generate_content(
#         "Tell me a story about a magic backpack.",
#         generation_config=genai.types.GenerationConfig(
            
#             candidate_count=1,
#             stop_sequences=["x"],
#             max_output_tokens=20,
#             temperature=1.0,
#         ),
#     )

#     print(response.text)
# except:
#     msg = '<h1 style="font-family:serif;color:#0047AB; font-size: 30px">Enter another genre.</h1>'
#     # st.markdown(title)
#     st.write(msg, unsafe_allow_html=True)
