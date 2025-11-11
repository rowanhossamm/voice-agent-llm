import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyBPOWRXqbspBh_3ulMzi0l5m9DH1OZtvJ4"))

models = genai.list_models()
for m in models:
    print(m.name, "-", m.supported_generation_methods)
