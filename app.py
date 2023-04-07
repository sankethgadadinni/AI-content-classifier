import os
import streamlit as st
from utils import GPT2PPL

def main():
    
    st.title("AI Content Classifier")
    
    text = st.text_input('enter the text')
    
    if text:
        
        length = len(text)
        
        if length < 250:
            st.write("Please enter some more text (> 250 characters)!!!")
            
        else:
            st.header("Input text")
            st.write(text)
            
            model = GPT2PPL()
            
            results, label = model(text)
            
            st.header("Result")
            st.write(label)            
    
    

if __name__ == '__main__':

    main()