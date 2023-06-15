from bs4 import BeautifulSoup
import requests
from lxml import etree
import time

unfamiliar_skill = input("please input unfamiiar skill:")
def find_jobs():
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchName=recentSearches&from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&gadLink=python').text
    Soup= BeautifulSoup(html_text, 'lxml')
    jobs = Soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').text.replace(' ','')
        if  "few" in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skill=job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skill:
                with open(f"POSTS/{index}.txt", "w") as f:
                    f.write(f"company name: {company_name.strip()}\n")
                    f.write(f"Required skills: {skill.strip()}\n")
                    f.write(f"more info: {more_info}\n")
                print(f"file Saved: {index}")

if __name__ == '__main__':
        while True:
            find_jobs()
            time_wait= 10
            print(f"waiting {time_wait} minutes...")
            time.sleep(time_wait*60)
        main()
        