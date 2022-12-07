''' Test_extract.py
    Takes the articles from Newscatcher, cleans them, and saves
    necessary data for later use.
'''
import time
import csv
import os
import json
import jsonlines

#   Define work folder
os.chdir("E:\\Work1\\Network_project\\test_data")

#   Create empty lists to hold specfic data
content = {}
articles = {}
article_IDs = []
titles = []
authors = []
summaries = []
pub_dates = []
pub_times = []
sources = []
links = []
publishers[]
k = 0

#   Load jsonl file
with open('news_articles.jsonl', 'r') as jsonl_f:
    content = jsonl_f.read()
    
#   Load file of articles
start_article = 1
while len(content) > 1501:
    end_article = content.find('"},')
    one_article = content[start_article:end_article]
    articles[k] = one_article
    content = content[(end_article+4):len(content)]
    start_article = 0
    k = k + 1

k = 0
while k <= 205:
    article_IDs.append(str(k))
    
    one_article = articles[k]
    end_title = one_article.find(',')
    one_title = one_article[9:(end_title)]
    one_title = one_title.replace('"','')
    one_title = one_title.replace('\\','')    
    titles.append(one_title)

    begin_author = one_article.find('author') + 10
    end_author = one_article.find('",',begin_author)
    if (begin_author)==end_author:
        one_author = '  '
    else:
        one_author = one_article[begin_author:end_author]
#    print(begin_author,end_author,one_author)
#    if k>15:
#        stop
    one_author = one_author.replace('Â','')
    one_author = one_author.replace('© ','')    
    authors.append(one_author)
    
    begin_summary = one_article.find('summary')
    begin_summary = begin_summary + 10
    end_summary = one_article.find('rights', begin_summary)
    end_summary = end_summary - 3
    one_summary = one_article[begin_summary:end_summary]
    one_summary = one_summary.replace('"','')
    one_summary = one_summary.replace(',','')    
    one_summary = one_summary.replace('\\n',' ')
    one_summary = one_summary.replace('\\','')
    one_summary = one_summary.replace('Â© ','')
    one_summary = one_summary.replace('Â','')
    one_summary = one_summary.replace('â€','')
    one_summary = one_summary.replace('â€˜ ','')
    one_summary = one_summary.replace('© ','')
    one_summary = one_summary.replace('˜ ',' ')

    summaries.append(one_summary)

    begin_pub_date = one_article.find('published_date') + 18
    end_pub_date = begin_pub_date + 10
    one_pub_date = one_article[begin_pub_date:end_pub_date]
    begin_pub_time = end_pub_date + 1
    end_pub_time = begin_pub_time + 8
    one_pub_time = one_article[begin_pub_time:end_pub_time]
    pub_dates.append(one_pub_date)
    pub_times.append(one_pub_time)
    
    begin_source_site = one_article.find('clean_url') + 13
    end_source_site = one_article.find(',',begin_source_site) - 1
    one_source_site = one_article[begin_source_site:end_source_site]
    sources.append(one_source_site)

    begin_link = one_article.find('link') + 8
    end_link = one_article.find(',',begin_link) - 1
    one_link = one_article[begin_link:end_link]
    links.append(one_link)
    
    k = k + 1

#   Save title, text, date, time, source
article_file = open('articles.csv','w')
k = 0
while k <= 205:
    one_line = '"' + article_IDs[k] + '","' + titles[k] + '","' + authors[k] + '","' + summaries[k] + '","' + pub_dates[k] + '","' + pub_times[k] + '","' + sources[k]+ '","' + links[k] + '"\n'
    article_file.write(one_line)
    k = k + 1
article_file.close()

#   Save titles and summaries as txt files
title_file = open('titles.txt','w')
k = 0
while k <= 205:
    one_line = titles[k] + "\n"
    title_file.write(one_line)
    k = k + 1
title_file.close()

title_file = open('summaries.txt','w')
k = 0
while k <= 205:
    one_line = summaries[k] + "\n\n"
    title_file.write(one_line)
    k = k + 1
title_file.close()

