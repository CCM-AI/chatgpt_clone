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
