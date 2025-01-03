import streamlit as st
from selenium.webdriver import Remote, ChromeOptions
from prase import parse_with_chatgroq
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

# Web scraping functions
def scrape_website(website):
    """Scrapes the website using Selenium and Chrome WebDriver"""
    st.write("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        st.write("Waiting for CAPTCHA to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        st.write("Captcha solve status:", solve_res["value"]["status"])
        st.write("Navigated! Scraping page content...")
        html = driver.page_source
        return html

def extract_body_content(html_content):
    """Extracts the body content of the webpage"""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    """Cleans the body content by removing unwanted elements"""
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    """Splits the DOM content into smaller chunks if it exceeds the max length"""
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Scrape the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        # Display the DOM content in an expandable text box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Split the content into smaller chunks if it's too large
            dom_chunks = split_dom_content(st.session_state.dom_content)

            # Here, you can add your own parsing logic using Ollama or another API
            # For example:
            parsed_result = parse_with_chatgroq(dom_chunks, parse_description)  # Placeholder for actual parsing logic
            st.write(parsed_result)