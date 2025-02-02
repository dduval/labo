import csv
import requests
from bs4 import BeautifulSoup

def html_to_csv(url, output_file):
  """
  Fetches an HTML page, extracts table data, and writes it to a CSV file.

  Args:
      url (str): The URL of the HTML page.
      output_file (str): The name of the output CSV file.
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
#        print(row_data[1])

  print(f"HTML page converted to CSV and saved as {output_file}")

# Example usage
html_to_csv("https://www.canada.ca/en/department-finance/news/2025/02/list-of-products-from-the-united-states-subject-to-25-per-cent-tariffs-effective-february-4-2025.html", "full-tariffs.csv")

#html_to_csv("https://www.canada.ca/fr/ministere-finances/nouvelles/2025/02/liste-des-produits-en-provenance-des-etats-unis-assujettis-a-des-tarifs-de-25--en-vigueur-des-le-4-fevrier-2025.html", "output.csv")


