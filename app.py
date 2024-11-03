import streamlit as st
import requests

# Function to get response from OpenAI API
def get_ai_response(user_message):
    api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-3.5-turbo',  # You can use a different model if you prefer
        'messages': [{'role': 'user', 'content': user_message}],
        'max_tokens': 150,
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    response_data = response.json()

    if response.status_code == 200:
        return response_data['choices'][0]['message']['content'].strip()
    else:
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
        # Show user input in the chat
        st.write(f"**You:** {user_input}")
        
        # Get AI response
        ai_response = get_ai_response(user_input)
        
        # Show AI response in the chat
        st.write(f"**ChatGPT:** {ai_response}")
    else:
        st.warning("Please enter a message.")
