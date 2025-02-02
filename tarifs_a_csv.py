import csv
import requests
from bs4 import BeautifulSoup

def html_to_csv(url, output_file):
  """
  Charge la liste HTML des tarifs (habituellemnt de canada.ca), extrait la table et l'ecrit dans un fichier CSV

  Args:
      url (str): URL de la page HTML
      output_file (str): Fihier CSV destination
  """

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  tables = soup.find_all('table')
  if not tables:
    print("No tables found in the HTML page.")
    return

  with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    for table in tables:
      rows = table.find_all('tr')

      for row in rows:
        cells = row.find_all(['th', 'td'])
        row_data = [cell.text.strip() for cell in cells]
        csv_writer.writerow(row_data)

  print(f"Page HTML convertie a {output_file}")

# Exemple
html_to_csv("https://www.canada.ca/fr/ministere-finances/nouvelles/2025/02/liste-des-produits-en-provenance-des-etats-unis-assujettis-a-des-tarifs-de-25--en-vigueur-des-le-4-fevrier-2025.html", "tarifs_fr.csv")


