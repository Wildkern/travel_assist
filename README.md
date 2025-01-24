# AI-Powered Travel Itinerary Planner with LangChain

This project is an AI-powered travel itinerary planner built with Streamlit and LangChain, utilizing DeepSeek model for text generation. The app takes user inputs for trip preferences and generates personalized travel itineraries.

## Features
- User inputs for trip preferences (destination, budget, duration, purpose, interests, etc.).
- AI-generated travel itinerary based on user preferences.
- Ability to refine the generated itinerary by adding or removing details.
- Conversation history to help with iterative refinements.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x (preferably Python 3.8 or higher)
- Git
- pip (Python package installer)

You will also need access to a **DeepSeek API key** for generating AI responses.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-travel-itinerary-planner.git
   cd ai-travel-itinerary-planner

    Set up a Virtual Environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`

Install Required Dependencies Install the required libraries using pip:

pip install -r requirements.txt

Set Your API Key Ensure you have the correct DeepSeek API key. You can set it as an environment variable or directly in the code:

export DEEPSEEK_API_KEY="your-deepseek-api-key"

Alternatively, you can modify the script where the API key is used.

Run the Application After setting up the environment, you can run the Streamlit app with the following command:

streamlit run app.py

This will start the app locally, and you can view it in your web browser at http://localhost:8501.
