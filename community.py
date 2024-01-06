import streamlit as st
import requests

# Function to send message to the backend
def send_message(message):
    url = 'http://localhost:5000/messages'
    data = {"message": message}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        st.success("Message sent!")

# Streamlit app layout
def chat():
    st.title("Mood-O-Meter with Community Chat")

    st.subheader("Community Chat")

    # Display chat interface
    user_message = st.text_area("Type your message here:")
    if st.button("Send"):
        if user_message:
            send_message(user_message)

    # Display chat history
    st.subheader("Chat History")
    response = requests.get('http://localhost:5000/messages')
    if response.status_code == 200:
        messages = response.json()
        for message in messages:
            st.write(f"- {message['message']}")

# Run the Streamlit app
if __name__ == "__main__":
    chat()
