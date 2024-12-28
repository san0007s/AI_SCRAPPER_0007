# AI Web Scraper  

## Overview  
The **AI Web Scraper** is a Streamlit-based application that leverages advanced AI and web scraping technologies to extract data from websites and allow users to ask insightful questions about the extracted data. The tool uses Streamlit for its user interface, Selenium for web scraping, and LangChain with Groq Cloud's API for AI-powered parsing and analysis.

---

## Features  
- **Web Scraping**: Scrapes the DOM content of any given URL using Selenium and BeautifulSoup.  
- **AI-Powered Parsing**: Utilizes Groq Cloud's API and LangChain to intelligently extract and process specific information from the webpage content.  
- **Streamlit UI**: Provides an intuitive interface for entering URLs, scraping content, and querying the data.  
- **Dynamic Parsing**: Allows users to define custom descriptions of the data they want to extract.  

---

## Prerequisites  
Ensure the following are installed:  
- Python 3.7 or higher  
- Chrome WebDriver  
- Groq Cloud API Key and Bright Light API Key (stored in a `.env` file)  

---

## Installation  

1. Clone this repository:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file to store API keys and configurations:  
   ```plaintext
   GROQ_API_KEY=your-groq-cloud-api-key
   SBR_WEBDRIVER=your-selenium-webdriver-url
   ```

---

## Usage  

1. Start the application:  
   ```bash
   streamlit run main.py
   ```

2. Enter the URL of the website you want to scrape in the Streamlit interface.  

3. Click on **Scrape Website** to extract and view the DOM content.  

4. Provide a description of what you want to parse (e.g., "Company size and ownership details") and click on **Parse Content** to get the desired data.  

---

## File Structure  
```plaintext
AI_Scraper/
├── main.py                  # Main Streamlit app & scrapping model
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
├── prase.py                 # Module for processing and parsing raw data
├── .env                     # Environment variables for API keys and configuration
```

---

## Explanation of Files  

- **`main.py`**: The main application file that integrates the Streamlit UI with the scraping and parsing models.  
- **`parse.py`**: Handles AI-based parsing of scraped content using Groq Cloud's API and LangChain.  
- **`.env`**: Stores sensitive configuration data such as API keys.  
- **`requirements.txt`**: Lists all the Python dependencies needed for the project.  

---

## Key Technologies  

- **Streamlit**: Builds the interactive user interface.  
- **Selenium**: Automates the web scraping process.  
- **BeautifulSoup**: Extracts and cleans HTML content.  
- **LangChain & Groq Cloud**: Processes and analyzes the extracted data using AI models.  

---

## Example `.env` File  
```plaintext
GROQ_API_KEY=your-groq-cloud-api-key
SBR_WEBDRIVER=your-selenium-webdriver-url
```

---

## Future Enhancements  
- Implementing support for additional web drivers.  
- Adding authentication mechanisms for scraping restricted websites.  
- Enhanceing AI parsing capabilities with custom-trained models.  

---

## Acknowledgments

- Groq Cloud for providing Llama API.
- Bright Light for the web scraping API.
- The Streamlit and LangChain communities for their awesome tools.

---

## Contributing  
Contributions are welcome! Feel free to submit a pull request or report issues.

---
