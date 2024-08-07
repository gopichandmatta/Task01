
# import requests
# from bs4 import BeautifulSoup
# import mysql.connector
# import json

# # Define the URLs of the pages containing links to JSON files
# urls = [
#     "https://www.circl.lu/doc/misp/feed-osint/",
#     "https://www.circl.lu/data/feed-osint/"
# ]

# # MySQL database connection details
# db_config = {
#     'user': 'gopichand',            # Replace with your MySQL username
#     'password': 'Gopi@6666',    # Replace with your MySQL password
#     'host': 'localhost',
#     'database': 'json_data_db',
#     'port': 3306

# }

# # try:
# #     connection = mysql.connector.connect(
# #         host='host.docker.internal',
# #         port=3306,
# #         user='gopichand',
# #         password='Gopi@6666',
# #         database='your_database'
# #     )
# #     cursor = connection.cursor()
# #     # Your data processing and insertion logic here
# # except mysql.connector.Error as err:
# #     print(f"Error: {err}")
# # finally:
# #     if connection.is_connected():
# #         cursor.close()
# #         connection.close()


# def fetch_page(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         return response.text
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred while fetching the page: {e}")
#         return None

# def extract_json_links(page_content):
#     soup = BeautifulSoup(page_content, 'html.parser')
#     links = soup.find_all('a', href=True)
#     json_links = [link['href'] for link in links if link['href'].endswith('.json')]
#     return json_links

# def fetch_json_data(json_url):
#     try:
#         response = requests.get(json_url)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred while fetching JSON data: {e}")
#         return None

# def flatten_json(y):
#     """
#     Flatten a nested JSON object.
#     """
#     out = {}

#     def flatten(x, name=''):
#         if isinstance(x, dict):
#             for a in x:
#                 flatten(x[a], name + a + '_')
#         elif isinstance(x, list):
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + '_')
#                 i += 1
#         else:
#             out[name[:-1]] = x

#     flatten(y)
#     return out

# def insert_data_to_db(data):
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()

#         # Define columns and their corresponding values
#         columns = [
#             'Event_analysis', 'Event_date', 'Event_extends_uuid', 'Event_info',
#             'Event_publish_timestamp', 'Event_published', 'Event_threat_level_id',
#             'Event_timestamp', 'Event_uuid', 'Event_Orgc_name', 'Event_Orgc_uuid',
#             'Event_Tag_0_colour', 'Event_Tag_0_local', 'Event_Tag_0_name',
#             'Event_Tag_0_relationship_type', 'Event_Tag_1_colour', 'Event_Tag_1_local',
#             'Event_Tag_1_name', 'Event_Tag_1_relationship_type', 'Event_Tag_2_colour',
#             'Event_Tag_2_local', 'Event_Tag_2_name', 'Event_Tag_2_relationship_type',
#             'Event_Tag_3_colour', 'Event_Tag_3_local', 'Event_Tag_3_name',
#             'Event_Tag_3_relationship_type', 'Event_Tag_4_colour', 'Event_Tag_4_local',
#             'Event_Tag_4_name', 'Event_Attribute_0_category', 'Event_Attribute_0_comment',
#             'Event_Attribute_0_deleted'
#         ]
        
#         placeholders = ', '.join(['%s'] * len(columns))
#         columns_str = ', '.join(columns)
        
#         # Prepare query
#         insert_query = f"INSERT INTO flattened_data ({columns_str}) VALUES ({placeholders})"
        
#         # Prepare data for insertion
#         row_data = [data.get(col, None) for col in columns]
        
#         # Print debug information
#         print(f"Insert Query: {insert_query}")
#         print(f"Row Data: {row_data}")

#         cursor.execute(insert_query, tuple(row_data))

#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Data inserted successfully.")
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")

# def process_url(url):
#     print(f"Processing URL: {url}")
    
#     # Fetch the main page content
#     page_content = fetch_page(url)
    
#     if page_content:
#         # Extract JSON links from the page
#         json_links = extract_json_links(page_content)
        
#         if not json_links:
#             print("No JSON links found.")
#             return
        
#         count = 0
#         for json_link in json_links:
#             if count >= 100:
#                 break
            
#             # Create full URL for the JSON files
#             full_url = requests.compat.urljoin(url, json_link)
            
#             # Fetch JSON data
#             json_data = fetch_json_data(full_url)
            
#             if json_data is not None:
#                 # Flatten the fetched JSON data
#                 flat_data = flatten_json(json_data)
                
#                 # Insert the data into the database
#                 insert_data_to_db(flat_data)
                
#                 count += 1

# def main():
#     for url in urls:
#         process_url(url)

# if __name__ == "__main__":
#     main()



# ##########################################################################



import requests
from bs4 import BeautifulSoup
import mysql.connector
import json

# Define the URLs of the pages containing links to JSON files
urls = [
    "https://www.circl.lu/doc/misp/feed-osint/",
    "https://www.botvrij.eu/data/feed-osint/",


]

# MySQL database connection details
db_config = {
    'user': 'gopichand',            # Replace with your MySQL username
    'password': 'Gopi@6666',        # Replace with your MySQL password
    'host': 'host.docker.internal', # Updated to connect to the host's MySQL server
    'database': 'json_data_db',
    'port': 3306
}

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
        return None

def extract_json_links(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    links = soup.find_all('a', href=True)
    json_links = [link['href'] for link in links if link['href'].endswith('.json')]
    return json_links

def fetch_json_data(json_url):
    try:
        response = requests.get(json_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching JSON data: {e}")
        return None

def flatten_json(y):
    """
    Flatten a nested JSON object.
    """
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x, list):
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def insert_data_to_db(data):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Define columns and their corresponding values
        columns = [
            'Event_analysis', 'Event_date', 'Event_extends_uuid', 'Event_info',
            'Event_publish_timestamp', 'Event_published', 'Event_threat_level_id',
            'Event_timestamp', 'Event_uuid', 'Event_Orgc_name', 'Event_Orgc_uuid',
            'Event_Tag_0_colour', 'Event_Tag_0_local', 'Event_Tag_0_name',
            'Event_Tag_0_relationship_type', 'Event_Tag_1_colour', 'Event_Tag_1_local',
            'Event_Tag_1_name', 'Event_Tag_1_relationship_type', 'Event_Tag_2_colour',
            'Event_Tag_2_local', 'Event_Tag_2_name', 'Event_Tag_2_relationship_type',
            'Event_Tag_3_colour', 'Event_Tag_3_local', 'Event_Tag_3_name',
            'Event_Tag_3_relationship_type', 'Event_Tag_4_colour', 'Event_Tag_4_local',
            'Event_Tag_4_name', 'Event_Attribute_0_category', 'Event_Attribute_0_comment',
            'Event_Attribute_0_deleted'
        ]
        
        placeholders = ', '.join(['%s'] * len(columns))
        columns_str = ', '.join(columns)
        
        # Prepare query
        insert_query = f"INSERT INTO flattened_data ({columns_str}) VALUES ({placeholders})"
        
        # Prepare data for insertion
        row_data = [data.get(col, None) for col in columns]
        
        # Print debug information
        print(f"Insert Query: {insert_query}")
        print(f"Row Data: {row_data}")

        cursor.execute(insert_query, tuple(row_data))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def process_url(url):
    print(f"Processing URL: {url}")
    
    # Fetch the main page content
    page_content = fetch_page(url)
    
    if page_content:
        # Extract JSON links from the page
        json_links = extract_json_links(page_content)
        
        if not json_links:
            print("No JSON links found.")
            return
        
        count = 0
        for json_link in json_links:
            if count >= 100:
                break
            
            # Create full URL for the JSON files
            full_url = requests.compat.urljoin(url, json_link)
            
            # Fetch JSON data
            json_data = fetch_json_data(full_url)
            
            if json_data is not None:
                # Flatten the fetched JSON data
                flat_data = flatten_json(json_data)
                
                # Insert the data into the database
                insert_data_to_db(flat_data)
                
                count += 1

def main():
    for url in urls:
        process_url(url)

if __name__ == "__main__":
    main()
