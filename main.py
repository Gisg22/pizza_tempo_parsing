from bs4 import BeautifulSoup
import requests
import csv

def get_data():
    headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    url = 'https://www.pizzatempo.by/menu/pizza.html'
    req = requests.get(url, headers=headers)
    scr = req.text
    with open('index.html', encoding='utf-8') as file:
        scr = file.read()
    soup = BeautifulSoup(scr, 'lxml')
    name_pizza = soup.find('div', class_='content').find_all('span')
    pizza = []

    for item in name_pizza:
        pizza.append(item.text)

    with open('names_of_pizza.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(pizza)




def main():
    get_data()

if __name__ == '__main__':
    main()
