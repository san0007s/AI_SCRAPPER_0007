import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Check for missing environment variables
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file.")

# Initialize ChatGroq
llm_groq = ChatGroq(api_key=groq_api_key, temperature=0, model_name="mixtral-8x7b-32768")

# Define the prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string (' ')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)


# Parsing function using ChatGroq
def parse_with_chatgroq(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        # Format the prompt with the current chunk
        formatted_prompt = prompt.format(
            dom_content=chunk, parse_description=parse_description
        )
        # Invoke ChatGroq with the formatted prompt
        response = llm_groq.invoke(formatted_prompt)

        # Extract text content from the response
        if hasattr(response, 'content'):  # Assuming response has a `content` attribute
            parsed_results.append(response.content)
        else:
            parsed_results.append(str(response))  # Fallback to string conversion

        print(f"Parsed batch: {i} of {len(dom_chunks)}")

    return "\n".join(parsed_results)


# Example usage

