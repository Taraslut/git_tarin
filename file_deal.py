import requests
import bs4

response = requests.get("http://quotes.toscrape.com/")
print(response.text)

page_bs = bs4.BeautifulSoup(response.text, "html.parser")
file_for_html = open("parsed_page_2.txt", 'wt', encoding='utf-8')
elements = page_bs.find_all('span', {'class': 'text'})
for element in elements:
    file_for_html.write(element.text)
    file_for_html.write("\n")

# file_for_html.write(page_bs.text.encode("utf-8", 'ignore').decode('utf-8', 'ignore'))
print(file_for_html.tell())
print(f'file {file_for_html.name} is saved!!!')
file_for_html.close()
