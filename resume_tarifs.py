import requests
from bs4 import BeautifulSoup

def html_to_txt(url):
  """
  Genere une version condensee de la description des tarifs sur canada.ca 

  Args:
      url (str): The URL of the HTML page.
  """

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  tables = soup.find_all('table')
  if not tables:
    print("No tables found in the HTML page.")
    return


  unique_descs = set()

  for table in tables:
    rows = table.find_all('tr')

    for row in rows:
      cells = row.find_all(['th', 'td'])
      row_data = [cell.text.strip() for cell in cells]
      if row_data[1] not in unique_descs:
        unique_descs.add(row_data[1]) 
        print(row_data[0] + " " + row_data[1])



html_to_txt("https://www.canada.ca/fr/ministere-finances/nouvelles/2025/02/liste-des-produits-en-provenance-des-etats-unis-assujettis-a-des-tarifs-de-25--en-vigueur-des-le-4-fevrier-2025.html")


