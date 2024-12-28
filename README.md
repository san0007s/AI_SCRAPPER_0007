
# AI Scraper

AI Scraper is an intelligent web scraping application developed using **Streamlit**, **Llama** from **Groq Cloud**, **Selenium**, and **LangChain**. It provides a user-friendly interface for extracting data from websites and querying the extracted data with natural language questions.

## Features

- **Web Scraping**: Extracts data from provided website links using the **Bright Light API**.
- **AI-Powered Q&A**: Answers questions like "Who owns this company?" or "What is the size of the company?" about the scraped data.
- **Interactive Interface**: Built with **Streamlit** for a seamless user experience.
- **Cloud Integration**: Utilizes **Groq Cloud's Llama API** for data processing and uploading.
- **Customizable Workflow**: Designed to be extendable and adaptable for various scraping and analysis tasks.

---

## Installation

### Prerequisites

1. **Python 3.8+**: Ensure Python is installed on your machine.
2. **Pip**: Package manager for installing dependencies.

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```



## Usage

1. Open the application in your browser (Streamlit will provide the link after starting).
2. Enter the website link you want to scrape.
3. Use the question input to ask questions about the scraped data.

Examples:
- *"Who owns this company?"*
- *"What is the size of the company?"*

---

## Project Structure

```
AI_Scraper/
├── main.py                  # Main Streamlit app & scrapping model 
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
├── prase.py                 # Module for processing and parsing raw data
├── .env                     # Environment variables for API keys and configuration
```

---

## APIs Used

1. **Bright Light API**: For web scraping.
2. **Groq Cloud Llama API**: For advanced data processing and uploading.

---

## Libraries and Tools

- **Streamlit**: For building the user interface.
- **LangChain**: For chaining AI tasks and managing workflows.
- **Selenium**: For interacting with dynamic web pages.

---

## Notes

1. Make sure the dependencies are installed before running the app:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure you have access to the required APIs (Bright Light and Groq Cloud Llama).

3. Run the app using:
   ```bash
   streamlit run main.py
   ```

---

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

---

## Acknowledgments

- **Groq Cloud** for providing Llama API.
- **Bright Light** for the web scraping API.
- The **Streamlit** and **LangChain** communities for their awesome tools.
```

You can copy-paste this into your `README.md` file. Be sure to replace `<repository-url>` and `<repository-folder>` with the actual URL of your repository and folder name.
