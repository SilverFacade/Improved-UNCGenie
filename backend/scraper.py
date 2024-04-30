import requests
from bs4 import BeautifulSoup
import psycopg2

urls = [
        'https://catalog.uncg.edu/courses/csc/',
        'https://catalog.uncg.edu/courses/mat/',
        'https://catalog.uncg.edu/courses/his/',
        'https://catalog.uncg.edu/courses/phi/',
        'https://catalog.uncg.edu/courses/bio/',
        'https://catalog.uncg.edu/courses/phy/'
]

conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)

for url in urls:
    # Make HTTP request
    response = requests.get(url) 

    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <div> elements with class "courseblock"
        course_blocks = soup.find_all('div', class_='courseblock')
        
        # Iterate over course blocks and extract class information
        for course_block in course_blocks:
            # Extract class title
            title_tag = course_block.find('p', class_='courseblocktitle')
            if title_tag:
                title = title_tag.text.strip()
            else:
                title = "No title available"
            
            # Split title into parts
            title_parts = title.split(' ')
            course_whole = title_parts[0]
            course_subject, course_number = title_parts[0].split()
            course_title = ' '.join(title_parts[2:-1])

            # Extract class description
            description_tag = course_block.find('p', class_='courseblockdesc')
            description = description_tag.text.strip() if description_tag else "No description available"

            # Find prerequisites element
            prerequisites_tag = course_block.find('p', class_='courseblockextra')
            if prerequisites_tag:
                # Extract prerequisites and remove from description
                prerequisites = prerequisites_tag.text.strip()
                description = description.replace(prerequisites, '').strip()
            else:
                prerequisites = "None"
            
            # Write to the database
            # try: 
                # cursor = conn.cursor()
                # cursor.execute("INSERT INTO classes (course_subject, course_number, course_title, description) VALUES (%s, %s, %s, %s, %s)",
                               # (course_subject, course_number, course_title, description))
            # finally:
                # if cursor is not None:
                    # cursor.close()

            # Print class information
            print("Course:", course_subject)
            print("Number:", course_number)
            print("Title:", course_title)
            print("Description:", description)
            print()
    else:
        print('Failed to retrieve the webpage:', response.status_code)