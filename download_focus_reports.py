from utils.get_focus_pdf_links import GetFocusPdfLinks
import requests

pdfLinks = GetFocusPdfLinks()
pdfLinks = pdfLinks.get_data()

for pdfLink in pdfLinks:
    url = pdfLink['url']
    releaseDate = pdfLink['releaseDate']
    response = requests.get(url)

    if response.status_code == 200:
        fileName = url.split('/')[-1]
        fileName = fileName.split('.')[0]
        fileName = f"{fileName}.{releaseDate}.pdf"
        
        with open(f'./data/reports/{fileName}', 'wb') as file:
            file.write(response.content)
            print(f"Downloaded {fileName}")
