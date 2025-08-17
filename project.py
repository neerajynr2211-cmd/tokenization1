import nltk
from nltk.tokenize import word_tokenize
import streamlit as st
import pandas as pd
import emoji

with st.sidebar.chat_message("ai",avatar="🎨"):
     st.write("Themes")
with st.chat_message("ai"):
    st.write("Hey There!")

st.set_page_config(
    page_title="Word Tokenization App",
    page_icon="✂️",
    layout="wide"
) 
#st.subheader("✂️Word tokenization App")

st.markdown("<h1 style='text-align: center;'>✂️ Word Tokenization App</h1>", unsafe_allow_html=True)

text = st.text_area("Enter your text here:",)

if st.button("Tokenize",):
    if text.strip():  # Check if not empty
        tokens = word_tokenize(text)
        st.subheader("📊 Tokens")
        st.write("**Tokens:**", tokens)
        st.write(f"**Number of tokens:** {len(tokens)}")
        freq = pd.Series(tokens).value_counts().reset_index()
        freq.columns = ["Tokens","Frequency"]
        st.table(freq)
        st.balloons()

    else:
        st.warning("Please enter some text before tokenizing.")

# themes
mode =st.sidebar.selectbox("Choose Theme",["Midnight ocean","Purple Galaxy","Light","Dark"])
if mode == "Purple Galaxy":
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #201e30, #2c2c54);

        }
        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }
        .stButton > button {
       background: linear-gradient(135deg, #e056fd, #7d5fff);

        border-radius: 20px;
        padding: 10px 24px;
        font-size: 30px;
        </style>
        """,
        unsafe_allow_html=True
    )

elif mode=="Midnight ocean":
    st.markdown(
        """
        <style>
        .stApp {
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: white ;
        }
    .stButton > button {
        background: linear-gradient(135deg, #9c88ff, #00cec9);

        color: black;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 30px;
    }
        </style>
        """,
        unsafe_allow_html=True
    )
elif mode=="Dark":
     st.markdown(
        """
        <style>
        .stApp {
           background-color:#000000;
        }
        h1 { 
         background-color: linear-gradient(180deg, #f5f5f5, #dcdcdc);
        }
        .stButton > button {
        background-color: #00bcd4;
        color: black;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 30px;
        
        </style>
        """,
        unsafe_allow_html=True
    )
elif mode =="Light":
    st.markdown(
        """
         <style>
        .stApp {
            background: #d9f4ef; background-image: linear-gradient(135deg, #d9f4ef 0%, #9be7d6 45%, #2aa39a 100%);

         }
        h1, h2, h3, h4, h5, h6,{
            color: black;
            color: #1a1a1a ; 
        }
        .stTextInput, .stButton, .stTextArea {
            color: #000 ;
          }

        .stButton > button {
        background-color: #00bcd4;
        color: ;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 30px;
        
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.sidebar.write(f"Current theme: **{mode.capitalize()} Mode**")

#about
about = st.sidebar.button("ℹ️About") 

if about:
    
    st.sidebar.write(" 1. Word tokenization is the process of splitting text into individual units called tokens (usually words).")
    col1,col2 =st.sidebar.columns(2)
    with col1:
     st.sidebar.write("""2. Why Tokenization Matters
     Explain real-world use cases:

     Search engines
             
     Chatbots
                         
     sentiment analysis
                         
     Text summarization""")

st.subheader("Made by Nk")