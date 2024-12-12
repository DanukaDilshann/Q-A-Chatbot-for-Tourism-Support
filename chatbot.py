import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set the Hugging Face API token
sec_key = "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"
os.environ['HUGGINGFACEHUB_API_TOKEN'] = sec_key

# Define the repository ID and explicitly set parameters
repo_id = "microsoft/Phi-3-mini-4k-instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.7, 
    max_length=128    
)


#Streamlit
# Define a Streamlit app
st.title("Tourism Q&A Chatbot for Tourism Support ")
st.write("You can ask any questions about tourism in Sri Lanka")

# User input section
placeholder=st.empty()
placeholder.text("we are here to help!")

user_question = st.text_input("Enter your question:" )

if user_question:
    placeholder.text(f"You asked: {user_question}")
else:
    placeholder.text('We are here to help!')

# Create a system prompt for the chatbot
# system_prompt = """You are a knowledgeable tourism assistant specializing in Sri Lanka. 
# direclty give the answers.
# Answer questions about the best places to visit, popular attractions, and travel tips in Sri Lanka."""

system_prompt="""You are a tourism assistant specializing in Sri Lanka. When asked a question, directly provide a short and clear answer in one sentence. Follow this with a detailed explanation about the location, its significance, and why it is worth visiting. Highlight key attractions, activities, and travel tips.

Example Question and Response:
Q: What is the most famous landmark in Sri Lanka?
A: Sigiriya Rock Fortress is the most famous landmark in Sri Lanka.

Tourism Details:
Sigiriya, also known as the Lion Rock, is a UNESCO World Heritage Site. 
It is an ancient rock fortress featuring remarkable frescoes, water gardens, and stunning panoramic views from the summit. 
Built in the 5th century by King Kashyapa, it stands as a symbol of Sri Lanka's architectural ingenuity and rich history.
Visitors can explore the archaeological ruins, marvel at the giant lion paws at the entrance, and enjoy the lush surroundings.
Ideal for history buffs and adventure seekers alike."""

template = """System Prompt: {system_prompt}
User Question: {user_question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["system_prompt", "user_question"])

# Initialize an LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Generate a response when the user submits a question
if user_question:
    with st.spinner("Generating response..."):
        response = llm_chain.run({"system_prompt": system_prompt, "user_question": user_question})
    st.write("### here the details:")
    st.write(response)

# # Testing the chatbot functionality
# st.write("---")
# st.write("Feel free to test different questions and explore recommendations!")

# # Example Testing Button
# if st.button("Test Example Question"):
#     test_question = "What are the best beaches in Sri Lanka?"
#     with st.spinner("Generating response for test question..."):
#         test_response = llm_chain.run({"system_prompt": system_prompt, "user_question": test_question})
#     st.write("### Test Response:")
#     st.write(test_response)
