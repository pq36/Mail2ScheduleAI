import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyA6RKrChXc9iXQW0o-nl4otpNiMDfVrRM8")

for model in genai.list_models():
    print(model.name)
model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hello")

print(response.text)