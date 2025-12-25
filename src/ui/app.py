import streamlit as st
from src.chatbot.engine import ChatbotEngine
from config.settings import settings

def run_app():
    st.set_page_config(page_title="Ask Me Anything 😉", layout="centered")
    
    st.title("Ask Me Anything 😉")

    with st.sidebar:
        st.title("Settings")
        st.info("Configure your OpenAI API details below.")
        
        # Override API Key from UI if provided, otherwise use config
        api_key = st.text_input(
            "OpenAI API Key", 
            type="password", 
            value=settings.OPENAI_API_KEY if settings.OPENAI_API_KEY else ""
        )
        
        model_name = st.selectbox(
            "Select Model",
            options=["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
            index=0
        )

    if not api_key:
        st.warning("Please provide an OpenAI API Key to proceed.")
        st.stop()

    # Initialize Chatbot Engine
    chatbot = ChatbotEngine(api_key=api_key, model=model_name)

    question = st.text_input("Enter your question here:")

    if question:
        if st.button("Get Answer") or question:
            with st.spinner("Thinking..."):
                response = chatbot.get_response(question)
                st.markdown("### Response:")
                st.write(response)

if __name__ == "__main__":
    run_app()
