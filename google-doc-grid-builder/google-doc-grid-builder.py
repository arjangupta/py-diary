import requests
from bs4 import BeautifulSoup

def get_google_doc_contents(doc_url):
    # Fetch the document content
    response = requests.get(doc_url)
    # Check if the request was successful (i.e., response code 200)
    response.raise_for_status()

    # Parse the document content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract all text from the document
    text = soup.get_text()
    # Return the extracted text
    return text

def decode_secret_message(doc_url):
    # Get the extracted text from the Google document
    extracted_text = get_google_doc_contents(doc_url)

    # Find the header row of the table
    header_string = 'x-coordinateCharactery-coordinate'
    start_index = extracted_text.find(header_string)

    # Find the beginning of the data
    data = extracted_text[ (start_index + len(header_string)) : ]


doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
decode_secret_message(doc_url)
