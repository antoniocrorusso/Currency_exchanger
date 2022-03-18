import requests
from bs4 import BeautifulSoup


def get_current_rate(tag):
    user_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/99.0.4844.51 Safari/537.36'}

    url = requests.get(f"https://br.investing.com/currencies/{tag}", headers=user_header)
    soup = BeautifulSoup(url.content, 'html.parser')

    answer = soup.find_all('span', class_="text-2xl")[0]
    cur_value = float(answer.text.replace(',', '.'))
    return cur_value


def exit_program():
    print("Thanks for using the program!")
    quit()

def run_again():
    print("""Do you wish to Run again:
1 - Yes
2 - No""")
    inp = int(input("Choice> "))
    if inp == 1:
        return True
    else:
        return False