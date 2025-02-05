import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the webpage
url = "https://www.linkedin.com/in/gower-campbell-16940115b/"  # Replace with your desired URL
response = requests.get(url)

# Step 2: Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract the data (Example: Post titles and content)
posts = soup.find_all('div', class_='post')  # Modify the class or tag according to the website structure

# Extract and print each post's title and content
for post in posts:
    title = post.find('h2').text  # Example: extracting post title inside an <h2> tag
    content = post.find('p').text  # Example: extracting post content inside a <p> tag
    print(f"Title: {title}")
    print(f"Content: {content}\n")
