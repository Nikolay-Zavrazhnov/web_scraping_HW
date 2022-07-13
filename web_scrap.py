import bs4

import requests

KEYWORDS = ['Pi', 'HoughCircles', 'MLAG', 'body']
base_url = 'https://habr.com'
url = '/ru/all'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2)'
           ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

response = requests.get(base_url+url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    titles = article.find_all(class_='tm-article-snippet__title tm-article-snippet__title_h2')
    titles = article.find('h2').find('span').text
    link = article.find(class_="tm-article-snippet__title-link").attrs['href']
    date = article.find('time').attrs['title']
    texts_preview_article = article.find_all(
        class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    texts_preview_article_div = article.find_all('div')

    compl_list = []

    for words in list(texts_preview_article_div):
        compl_list += words.text.split(' ')
    crossing_word = set(KEYWORDS) & set(compl_list)
    if len(crossing_word) > 0:
        print(f"<{date}>-<{titles}>-<{base_url + link}>")
