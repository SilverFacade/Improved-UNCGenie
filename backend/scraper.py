import requests
from bs4 import BeautifulSoup


url = 'https://catalog.uncg.edu/courses/csc/'
response = requests.get(url)

if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <div> elements with class "courseblock"
    course_blocks = soup.find_all('div', class_='courseblock')
    
    # Iterate over course blocks and extract class information
    for course_block in course_blocks:
        # Extract class title
        title = course_block.find('p', class_='courseblocktitle').text.strip()
        
        # Extract class description
        description = course_block.find('p', class_='courseblockdesc').text.strip()
        
        # Print class information
        print("Title:", title)
        print("Description:", description)
        print()
else:
    print('Failed to retrieve the webpage:', response.status_code)