import bs4
import requests

KEYWORDS_2 = ['Pi', 'HoughCircles', 'MLAG', 'body', 'HTML']
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
    link = article.find(class_='tm-article-snippet__title-link').attrs['href']
    date = article.find('time').attrs['title']
    texts_preview_article = article.find_all(
        class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    texts_preview_article = article.find_all('div')

    link_full_text = article.find(class_='tm-article-snippet__readmore').attrs['href']
    full_url = base_url+link_full_text

    response_2 = requests.get(full_url, headers=HEADERS)
    text_2 = response_2.text

    soup_2 = bs4.BeautifulSoup(text_2, features='html.parser')
    article_2 = soup_2.find('article')
    all_text = article_2.find_all('div')
    sub_title = article_2.find('h3')
    # print(type(sub_title))

    compl_list_2 = []

    for words in list(all_text):
        compl_list_2 += words.text.split(' ')
    crossing_word_2 = set(KEYWORDS_2) & set(compl_list_2)
    if len(crossing_word_2) != 0:
        print(f"<{date}>-<{titles}>-<{full_url}>")
