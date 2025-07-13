from bs4 import BeautifulSoup
import requests
from consts import stores

for i in stores:
    match i:
        case 'Target':
            url = f"https://www.target.com/s?searchTerm={}"
        case 'Walmart':
            url = f"https://www.walmart.com/search?q=Little+Bites+Frosted+Mini+Wheats"
        case 'Publix':
            url = f"https://www.publix.com/search?searchTerm=Little%20Bites%20Frosted%20Mini%20Wheats&srt=products"
        case 'Costco':
            url = f"https://www.costco.com/s?keyword=little%20bite%20frosted%20mini%20wheats"
        case 'Wegmans':
            url = f"https://www.wegmans.com/shop/search?query=little%20bites%20frosted%20mini%20wheats"

response = requests.get(url)

if response.status_code == 200:
    html_doc = response.text

    soup = BeautifulSoup(html_doc, 'html.parser')