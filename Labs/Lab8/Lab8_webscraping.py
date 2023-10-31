import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
html = requests.get(url)

a = BeautifulSoup(html.content, 'html.parser')

results = a.find(id='ResultsContainer')
job_title = results.find_all('h2',class_='title is-5')

print("List of All Jobs")
print("\n")
for job in job_title:
    print(job.text)