import streamlit as st
import openai
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# DeepSeek API Key
api_key = "YOUR_DEEPSEEK_API_KEY"  # Replace with your DeepSeek API key

# Set the OpenAI API key for DeepSeek and custom base URL
openai.api_key = api_key
openai.api_base = "https://api.deepseek.com"  # Set the DeepSeek base URL

# Initialize memory to maintain conversation history
memory = ConversationBufferMemory()

# Define prompts
initial_prompt = PromptTemplate(
    input_variables=["destination", "duration", "budget", "purpose", "interests", "diet", "mobility"],
    template="""
    You are a travel planner. Plan a {duration}-day itinerary for a trip to {destination}.
    User preferences:
    - Budget: {budget}
    - Purpose: {purpose}
    - Interests: {interests}
    - Dietary Preferences: {diet}
    - Mobility Concerns: {mobility}
    Include top attractions, hidden gems, meal suggestions, and activity timings.
    """
)

refinement_prompt = PromptTemplate(
    input_variables=["itinerary", "refinement"],
    template="""
    Based on the following itinerary:
    {itinerary}

    The user has provided additional input: {refinement}.
    Please refine and improve the itinerary accordingly.
    """
)

# Function to call DeepSeek API using OpenAI SDK
def call_deepseek_api(prompt):
    response = openai.ChatCompletion.create(
        model="deepseek-chat",  # Specify the DeepSeek model
        messages=[
            {"role": "system", "content": "You are a travel planner."},
            {"role": "user", "content": prompt}
        ],
        stream=False  # Do not stream, get the full response at once
    )
    return response.choices[0].message["content"]

# Streamlit UI
st.title("AI-Powered Travel Itinerary Planner with DeepSeek")

# User inputs
st.sidebar.header("User Preferences")
destination = st.sidebar.text_input("Destination", "Paris")
budget = st.sidebar.selectbox("Budget", ["Luxury", "Moderate", "Budget-Friendly"])
duration = st.sidebar.number_input("Trip Duration (days)", min_value=1, max_value=30, value=3)
purpose = st.sidebar.text_area("Purpose of Trip", "Vacation")
interests = st.sidebar.text_area("Interests (e.g., museums, adventure, food)", "Art, Food")
diet = st.sidebar.text_input("Dietary Preferences", "Vegetarian")
mobility = st.sidebar.selectbox("Mobility Concerns", ["None", "Low Walking", "Moderate Walking", "High Walking"])

# Generate Initial Itinerary
if st.sidebar.button("Generate Initial Itinerary"):
    with st.spinner("Generating your itinerary..."):
        # Generate initial prompt
        prompt = initial_prompt.format(
            destination=destination,
            duration=duration,
            budget=budget,
            purpose=purpose,
            interests=interests,
            diet=diet,
            mobility=mobility,
        )
        
        # Call DeepSeek API using OpenAI SDK
        initial_response = call_deepseek_api(prompt)
        
        st.subheader("Initial Itinerary")
        st.write(initial_response)

        # Store the generated itinerary for further refinement
        st.session_state["itinerary"] = initial_response

# Refinement Section
if "itinerary" in st.session_state:
    st.subheader("Refine Your Itinerary")
    refinement = st.text_input("What would you like to add, remove, or clarify?")
    if st.button("Refine Itinerary"):
        with st.spinner("Refining your itinerary..."):
            refine_prompt = refinement_prompt.format(
                itinerary=st.session_state["itinerary"],
                refinement=refinement,
            )
            
            # Call DeepSeek API for refinement using OpenAI SDK
            refined_response = call_deepseek_api(refine_prompt)
            
            st.session_state["itinerary"] = refined_response
            st.subheader("Refined Itinerary")
            st.write(refined_response)

# Debugging or memory inspection (optional)
st.sidebar.subheader("Conversation Memory")
st.sidebar.write(memory.buffer)
