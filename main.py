import streamlit as st
import langchain
import streamlit as st

def main():
    # Set the title and description of the app
    st.title("LearningStreamlit-Abdul Qadeer")
    st.subheader("Welcome to my app!")
    
    # Add a chatbot section
    st.markdown("## Chatbot Section")
    
    # Create a LangChain chatbot instance
    chatbot = langchain.Chatbot()
    
    # Add a text input for user input
    user_input = st.text_input("Enter your message", "")
    
    # Get the chatbot's response
    bot_response = chatbot.get_response(user_input)
    
    # Display the chatbot's response
    st.write("Chatbot:", bot_response)

if __name__ == "__main__":
    main()