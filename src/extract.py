import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

headers = {'user-agent': 'Mozilla/5.0'}

def extract(i):
    url = f"https://www.npmjs.com/search?q=keywords%3Aweb&ranking=popularity&page={i}&perPage=20"
    print(f'Coletando página {i}')
    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    sections = page.find_all('section', attrs={'class': 'ef4d7c63 flex-l pl1-ns pt3 pb2 ph1 bb b--black-10'})

    data = []

    for section in sections:
        info = section.find('a')
        package_name = info.text.strip()
        link = info.get('href')
        gh, wk_d = extract_pkg_info(f"https://www.npmjs.com{link}")

        pkg_data = {
            "nome": package_name,
            "link": f"https://www.npmjs.com{link}",
            "github": gh,
            "weekly_downloads": wk_d
            }

        data.append(pkg_data)
        print(f'Pacote {package_name} coletado com sucesso.')

    return data

def extract_pkg_info(url: str):
    repo_res = None
    wk_res = None

    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    gh_repo = page.find('a', attrs={'class': 'b2812e30 f2874b88 fw6 mb3 mt2 truncate black-80 f4 link'})
    if gh_repo:
        repo_res = gh_repo.get('href')

    wk_downloads = page.find('p', attrs={'class': '_9ba9a726 f4 tl flex-auto fw6 black-80 ma0 pr2 pb1'})
    if wk_downloads:
        wk_res = int(wk_downloads.text.replace(',', '').strip())

    return repo_res, wk_res

def init_extract():
    start = datetime.now()

    all_data = []

    for i in range(10):
        data = extract(i)
        all_data.extend(data)


    df = pd.DataFrame(all_data)

    df.to_excel('npm_packages.xlsx', index=False)

    end_time = datetime.now()
    total_time = end_time - start

    print('----------------------------------')
    print(f"Início da execução: {start}")
    print(f"Fim da execução: {end_time}")
    print(f"Tempo total de execução: {total_time}")
