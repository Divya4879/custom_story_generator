from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, render_template,redirect
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = Flask(__name__)


  
@app.route('/')
def index():
  f = open("template/index.html","r")
  page = f.read()
  f.close()

  page = page.replace("{title}","") 
  page = page.replace("{story}","") 
  return page

@app.route('/gen_story', methods=["POST","GET"])
def gen_story():
  f = open("template/index.html","r")
  page = f.read()
  f.close()
  model=genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You're a world renowned author. You've this experience for over 20 years.",
        generation_config=genai.types.GenerationConfig
        (
        candidate_count=1,
        stop_sequences=["x"],
        max_output_tokens=1000,
        temperature=0.2,
        ),
        
    )


  try:
      if request.form.get('theme')=='fanfiction':
              response = model.generate_content(f" Write a complete story with a meaningful ending in about {request.form.get('words')} words on the theme of {request.form.get('theme')}, also it should have the genre of {request.form.get('genre')} and it must be based on {request.form.get('ref')}."
          )

      else:
          response = model.generate_content(f"Write a complete story with a meaningful ending in about {request.form.get('words')} words on the theme of {request.form.get('theme')}, also it should have the genre of {request.form.get('genre')}."
          )

      
      story = response.text
      title = model.generate_content(f"What is the the most appropriate title of the {response} in 2-5 words (answer with only 1 title)?"
      )
      
      title = title.text
      
  except:
      title = "Enter another genre"
      story = ""
  
  
  page += """<div id="story">
            <h2>{title}</h2>
            <p>{story}</p>
      </div>"""
  page = page.replace("{title}",title)
  page = page.replace("{story}",story)
  return page
        


app.run(host='0.0.0.0', port=81)




