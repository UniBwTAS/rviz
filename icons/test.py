
import os
import requests
from bs4 import BeautifulSoup

def download_google_font_icon(icon_name, save_directory="icons"):
    base_url = "https://fonts.google.com/icons?query=home"

    # Construct the search URL
    search_url = f"{base_url}&icon.query={icon_name}"

    # Send a GET request to fetch the search page
    response = requests.get(search_url)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first result for the icon name
    icon_link = soup.find('a', class_="VfPpkd-YVzG2b YtXJdc-tJHJj-LgbsSe")
    
    if icon_link:
        icon_href = icon_link.get('href')
        icon_page_url = f"https://fonts.google.com{icon_href}"

        # Visit the icon's page to fetch the SVG URL
        icon_page_response = requests.get(icon_page_url)
        icon_page_response.raise_for_status()

        icon_page_soup = BeautifulSoup(icon_page_response.content, 'html.parser')
        svg_element = icon_page_soup.find('svg')

        if svg_element:
            svg_code = str(svg_element)
            icon_filename = f"{formatted_icon_name}.svg"

            # Ensure the save directory exists
            os.makedirs(save_directory, exist_ok=True)
            file_path = os.path.join(save_directory, icon_filename)

            # Save the SVG content to a file
            with open(file_path, 'w') as file:
                file.write(svg_code)
            print(f"Icon '{icon_name}' downloaded successfully as '{file_path}'")
        else:
            print(f"SVG for '{icon_name}' not found.")
    else:
        print(f"Icon '{icon_name}' not found on Google Fonts.")

# Example usage:
download_google_font_icon("home", save_directory="downloaded_icons")
