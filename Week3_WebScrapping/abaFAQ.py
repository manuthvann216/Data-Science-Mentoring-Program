import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
url='https://www.ababank.com/en/aba-mobile-app/aba-mobile-overview/f-a-q/'
html=requests.get(url)

s=BeautifulSoup(html.content, 'html.parser')
results=s.find(id='left_content')
faq_Q=results.find_all('a', class_='accordion-toggle')
faq_A=results.find_all('div', class_='accordion-inner')

for question, answer in zip(faq_Q, faq_A):  
    print(question.text + " \n " + "->" + answer.text);
