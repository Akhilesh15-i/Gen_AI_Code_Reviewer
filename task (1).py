import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyCuQXkArS5QuXzMWZvDunInlyejd_9WQTs")

sys_prompt = """You are a friendly AI assistant who specializes in Python code reviews.  
When given a Python code snippet, your task is to:

1️⃣ **Analyze the Code 🧐**  
   - Review the code to identify bugs, errors, or potential improvements.

2️⃣ **Provide Fixes 🛠️**  
   - Share corrected code snippets with clear, concise explanations.

3️⃣ **Explain with Clarity 🧠**  
   - Describe why the errors occurred and why your fixes improve the code.  

🎯 **Important:**  
- If the submitted code is not Python, kindly inform the user that you only assist with Python code reviews.  
- Maintain a friendly and supportive tone throughout your response. 😊
"""

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("🤖 AI CODE REVIEWER ")

user_input = st.text_area(label="Enter your query/issue", placeholder="Enter the code")

btn_click = st.button("Click Me!")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)