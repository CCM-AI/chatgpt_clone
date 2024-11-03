import streamlit as st
import requests
import os

# Function to get response from OpenAI API
def get_ai_response(user_message):
    api_key = os.getenv("OPENAI_API_KEY")  # This will access the secret in your deployment
    if not api_key:
        st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
        return "Sorry, I couldn't fetch a response."

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': user_message}],
        'max_tokens': 150,
    }

    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
            return "Sorry, I couldn't fetch a response."
    except Exception as e:
        st.error(f"An exception occurred: {str(e)}")
        return "Sorry, I couldn't fetch a response."

# Streamlit app layout
st.set_page_config(page_title="ChatGPT Clone", layout="centered")

# Title of the app
st.title("ChatGPT Clone")

# Text input for user message
user_input = st.text_input("Type your question:")

# Button to send the message
if st.button("Send"):
    if user_input:
        st.write(f"**You:** {user_input}")
        ai_response = get_ai_response(user_input)
        st.write(f"**ChatGPT:** {ai_response}")
    else:
        st.warning("Please enter a message.")
