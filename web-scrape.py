#The Below code would scrape all the links on a webpage that returns 200 Succes Code


import requests

from bs4 import BeautifulSoup

url = "https://example.com"  # Replace with the target URL
response = requests.get(url)

#If Condition to compare
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a', href=True)

        #For to runthrough all the HREF Code
        for link in links:
        print(f"Link: {link['href']}") #Print the HREF Link
else:
    print(f"Failed to retrieve {url} - Status code: {response.status_code}") #Print Error Code or Failure code (400 or 500)
