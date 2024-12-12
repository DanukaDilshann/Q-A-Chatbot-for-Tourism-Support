import streamlit as st
from Hugginface_config import llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


#Streamlit
st.title("Q&A Chatbot for Tourism Support in Sri Lanaka ")
st.write("You can ask any questions about tourism in Sri Lanka")

# User input section
user_question = st.text_input("Enter your question:" )


placeholder=st.empty()
placeholder.text("we are here to help!")
if user_question:
    placeholder.text(f"You asked: {user_question}")
else:
    placeholder.text(' ')


with open("prompt.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

template = """System Prompt: {system_prompt}
User Question: {user_question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["system_prompt", "user_question"])

# Initialize an LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Generate a response when the user submits a question
if user_question:
    with st.spinner("Please wait..."):
        response = llm_chain.run({"system_prompt": system_prompt, "user_question": user_question})
    st.write("### Here the details:")
    st.write(response)


#-------------------------------------------------------------------------------------
# Testing the chatbot 

st.write("________________________________________________________________________________________")
st.write("Feel free to test different questions and explore recommendations!")

# Example
if st.button("Test Example Question"):
    test_question = "What are the best beaches in Sri Lanka?"
    with st.spinner("Generating response for test question..."):
        test_response = llm_chain.run({"system_prompt": system_prompt, "user_question": test_question})
    st.write("### Test Response:")
    st.write(test_response)
