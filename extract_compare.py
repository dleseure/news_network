''' Extract.py and Compare.py
    Test_extract.py
    Takes the articles from Newscatcher, cleans them, and saves
    necessary data for later use.
'''
# import os                                            # comment out in github
from pysimilar import compare

#   Define work folder
# os.chdir("E:\\Work1\\Network_project\\test_data")   #comment out in github

#   Create empty lists to hold specfic data
content = {}
articles = {}
article_IDs = []
titles = []
authors = []
summaries = []
pub_dt = []
sources = []
links = []
publishers = []
k = 0

#   Load jsonl file
with open('news_articles.jsonl', 'r', encoding='utf-8') as jsonl_f:
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
while k < 205:
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

    begin_dt = one_article.find('published_date') + 18
    end_dt = begin_dt + 19
    one_dt = one_article[begin_dt:end_dt]
    pub_dt.append(one_dt)

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
article_file = open('articles.csv','w', encoding='utf-8')
k = 0
while k < 205:
    one_line = '"' + article_IDs[k] + '","' + titles[k] + '","' + authors[k]   \
               + '","' + summaries[k] + '","' + pub_dt[k]   \
               + '","' + sources[k]+ '","' + links[k]+ '"\n'
    article_file.write(one_line)
    k = k + 1
article_file.close()

#   Save titles and summaries as txt files
title_file = open('titles.txt','w', encoding='utf-8')
k = 0
while k < 205:
    one_line = titles[k] + "\n"
    title_file.write(one_line)
    k = k + 1
title_file.close()

title_file = open('summaries.txt','w', encoding='utf-8')
k = 0
while k < 205:
    one_line = summaries[k] + "\n\n"
    title_file.write(one_line)
    k = k + 1
title_file.close()

#   compare.py
#   Compares text of each pair of articles extracted from
#   article data returned from Newscatcher

#   Create empty lists
articles = []
scores = []
top_scores = []
header =  'source' +  ',' + 'target' + ',' + 'weight' + '\n'
top_scores.append(header)

#   Load articles
with open('articles.csv', 'r',encoding='windows-1252') as articles_file:
    articles = articles_file.readlines()

#   Compare each article to every other article
k = 0
m = 0
nbr_50 = 0
nbr_60 = 0
nbr_70 = 0
nbr_80 = 0
nbr_90 = 0
while k < 205:
    j = k + 1
    while j < 205:
#       Get first article & date/time
        one_art = articles[k]
        title_begin = one_art.find('","') + 3
        author_begin = one_art.find('","',title_begin) + 3
        art_begin = one_art.find('","',author_begin) + 3
        art_end = one_art.find('","',art_begin)
        art1 = one_art[art_begin:art_end]
        dt1_begin = art_end + 3
        dt1_end = dt1_begin + 19
        dt1 = one_art[dt1_begin:dt1_end]
        source_begin = dt1_end + 3
        source_end = one_art.find('","',source_begin)
        source1 = one_art[source_begin:source_end]

#       Get second article & date/time
        one_art = articles[j]
        title_begin = one_art.find(',"') + 2
        author_begin = one_art.find('","',title_begin) + 3
        art_begin = one_art.find('","',author_begin) + 3
        art_end = one_art.find('","',art_begin)
        art2 = one_art[art_begin:art_end]
        dt2_begin = art_end + 3
        dt2_end = dt2_begin + 19
        dt2 = one_art[dt2_begin:dt2_end]
        source_begin = dt2_end + 3
        source_end = one_art.find('","',source_begin)
        source2 = one_art[source_begin:source_end]

        score = compare(art1, art2)

#       Tally current score
        if score >= 0.5:
            nbr_50 = nbr_50 + 1
            if score >= 0.6:
                nbr_60 = nbr_60 + 1
                if score >= 0.7:
                    nbr_70 = nbr_70 + 1
                    if score >= 0.8:
                        nbr_80 = nbr_80 + 1
                        if score >= 0.9:
                            nbr_90 = nbr_90 + 1

#       Calculate direction (ie, which article was published second)
        if dt1 < dt2:
            direction = str(j)
            one_result = '"'+str(k)+'","'+source1+'","'+str(j)+'","'+source2+'","'+str(score) +'"\n'
            short_result =  source1 + "," + source2 + ","+ str(score) +"\n"
        else:
            direction = str(k)
            one_result = '"'+str(j)+'","'+source2+'","'+str(k)+'","'+source1+'","'+str(score)+'"\n'
            short_result =  source2 + "," + source1 + ","+ str(score) +"\n"

#       Save the result of one comparison
        scores.append(one_result)
        if score >= 0.9:
            top_scores.append(short_result)
        m = m + 1
        j = j + 1
    k = k + 1

#   Save scores
with open('scores.csv', 'w', encoding='utf-8') as scores_file:
    scores_file.writelines(scores)
with open('top_scores.csv', 'w', encoding='utf-8') as top_scores_file:
    top_scores_file.writelines(top_scores)

print("total number of scores:",m)
print("scores >= 0.5 ",nbr_50)
print("scores >= 0.6 ",nbr_60)
print("scores >= 0.7 ",nbr_70)
print("scores >= 0.8 ",nbr_80)
print("scores >= 0.9 ",nbr_90)
