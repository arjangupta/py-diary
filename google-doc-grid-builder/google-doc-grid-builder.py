import requests
from bs4 import BeautifulSoup
from heapq import heappush, heappop

class MaxHeap:
    """
    A container that stores integers in descending sorted order using a max heap.
    Provides efficient insertion and iteration in descending order.
    """
    def __init__(self):
        self._heap = []
    
    def insert(self, item: tuple) -> None:
        """Insert a (number, Unicode_character) tuple into the container."""
        heappush(self._heap, (item[0] * -1, item[1]))
    
    def pop(self) -> tuple:
        """Remove and return the largest (number, Unicode_character) tuple. Raises IndexError if empty."""
        if not self._heap:
            raise IndexError("Pop from empty container")
        number, char = heappop(self._heap)
        return number * -1, char
    
    def peek(self) -> tuple:
        """View the largest (number, Unicode_character) tuple without removing it."""
        if not self._heap:
            raise IndexError("Container is empty")
        number, char = self._heap[0]
        return number * -1, char
    
    def __len__(self) -> int:
        """Return the number of elements in the container."""
        return len(self._heap)

def get_google_doc_contents(doc_url):
    # Fetch the document content
    response = requests.get(doc_url)
    # Check if the request was successful (i.e., response code 200)
    response.raise_for_status()

    # Parse the document content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract all text from the document, keep the newlines
    text = soup.get_text(separator='\n')
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
    # Split the data into lines
    data_lines = data.split('\n')

    # Declare a hash map of MaxHeaps to map x-coordinates to y-coordinate - Unicode character pairs
    # We can access x-coordinate keys to get the corresponding y-coordinates and print the characters
    x_to_y_char = {}

    # Iterate over the data lines in increments of 3
    largest_x = 0
    largest_y = 0
    for i in range(0, len(data_lines), 3):
        # Extract the x-coordinate, Unicode character, and y-coordinate
        x = int(data_lines[i])
        char = data_lines[i + 1]
        y = int(data_lines[i + 2])

        # Update the largest x-coordinate
        largest_x = max(largest_x, x)
        # Update the largest y-coordinate
        largest_y = max(largest_y, y)

        # If the x-coordinate is not in the hash map, create a new MaxHeap for it
        if x not in x_to_y_char:
            x_to_y_char[x] = MaxHeap()
        
        # Insert the y-coordinate - Unicode pair into the MaxHeap for the corresponding x-coordinate
        x_to_y_char[x].insert((y, char))
    
    # Iterate over the x-coordinates from 0 to the largest x-coordinate
    for x in range(largest_x + 1):
        # If the x-coordinate is in the hash map, print the Unicode characters in descending order of y-coordinate
        if x in x_to_y_char:
            while len(x_to_y_char[x]) > 0:
                _, char = x_to_y_char[x].pop()
                print(char, end='')
        # Print a newline character after each row
        print()



doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
decode_secret_message(doc_url)
