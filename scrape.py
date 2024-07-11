import requests
from bs4 import BeautifulSoup

def check_links(readme_path, base_url):
    """
        Checks the validity of links in the LeetCode README file.

        Args:
            readme_path (str): The path to the README file.
            base_url (str): The base URL to prepend to relative links.

        Returns:
            None
        """
    with open(readme_path, 'r', encoding='utf-8') as file:
        readme_content = file.read()

    # Extract all URLs using BeautifulSoup
    soup = BeautifulSoup(readme_content, 'html.parser')
    links = soup.find_all('a', href=True)
    invalid_links = []

    for link in links:
        url = link['href']

        # Prepend the base URL
        if not url.startswith('http'):
            url = base_url + url

        try:
            # Checks for a valid response
            response = requests.head(url)
            if response.status_code == 200:
                print(f"Valid link: {url}")
            else:
                # Link was successfully reached but server responded with an issue (represented by the status code)
                print(f"Invalid link: {url} - Status code: {response.status_code}")
                invalid_links.append(url)

        # Programme error, probably network issue or server issue
        except requests.exceptions.RequestException as e:
            print(f"Error checking link: {url} - Error: {e}")

    print("========================================================================================")
    if invalid_links:
        print(f"Found {len(invalid_links)} Invalid links: " + " \n".join(invalid_links))

    else:
        print("No Invalid Links :)")


if __name__ == "__main__":
    readme_path = 'README.md'
    base_url = 'https://github.com/jyztintan/Leetcode/blob/main/'
    check_links(readme_path, base_url)
