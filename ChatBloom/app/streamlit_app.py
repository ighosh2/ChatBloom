import streamlit as st
from sidebar import display_sidebar
from chat_interface import display_chat_interface


# Custom CSS for centering title and background color
st.markdown(
    """
    <style>
     .stApp {
            background-color: #8f86f6;
        }
      .stSidebar {
            background-color: #11057e;
        }
          /* Top-Right Corner Text */
        .top-right {
            position: absolute;
            top: 10px;
            right: 20px;
            font-size: 12px;
            font-weight: bold;
            color: white;
        }

        .main {
            background-color: #f0f2f6; /* background color */
        }
        h1 {
            text-align: center;
            color: #4B6EAF; /* Optional: Title color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Top-right developer credit and header
st.markdown("<div class='top-right'>-Developed by Indrajit Ghosh</div>", unsafe_allow_html=True)
st.title("ChatBloom")
st.markdown("<h4 style='text-align: center;'>Your Personal RAG Chatbot</h4>", unsafe_allow_html=True)


# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

# Display the sidebar
display_sidebar()

# Display the chat interface
display_chat_interface()
