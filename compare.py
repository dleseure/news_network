''' compare.py

    Compares text of each pair of articles extracted from
    article data returned from Newscatcher
'''
from pysimilar import compare
# import pysimilar
from datetime import datetime
#   import os

#   Define work folder
#   os.chdir("E:\\Work1\\Network_project\\test_data")

#   Create empty lists
articles = []
scores = []
top_scores = []

#   Load articles
with open('articles.csv', 'r',encoding='windows-1252') as articles_file:
    articles = articles_file.readlines()

#   Compare each article to every other article
k = 0
m = 0
nbr50 = 0
nbr60 = 0
nbr70 = 0
nbr80 = 0
nbr90 = 0
while k <= 204:
    j = k + 1
    while j <= 205:
#       Get first article & date/time       
        one_art = articles[k]
        title_begin = one_art.find('","') + 3
        author_begin = one_art.find('","',title_begin) + 3
        art_begin = one_art.find('","',author_begin) + 3
        art_end = one_art.find('","',art_begin)
        art1 = one_art[art_begin:art_end]
        date_begin = art_end + 3
        date_end = date_begin + 10
        date1 = one_art[date_begin:date_end]
        date1 = date1.replace("-","/",2)        
        time_begin = date_end + 3
        time_end = time_begin + 8
        time1 = one_art[time_begin:time_end]
        time1 = time1.replace(':','/',2)
        source_begin = time_end + 3
        source_end = len(articles[k]) - 2
        source1 = one_art[source_begin:source_end]
        
#       Get second article & date/time
        one_art = articles[j]
        title_begin = one_art.find(',"') + 2
        author_begin = one_art.find('","',title_begin) + 3
        art_begin = one_art.find('","',author_begin) + 3
        art_end = one_art.find('","',art_begin)
        art2 = one_art[art_begin:art_end]
        date_begin = art_end + 3
        date_end = date_begin + 10
        date2 = one_art[date_begin:date_end]
        date2 = date2.replace("-","/",2)
        time_begin = date_end + 3
        time_end = time_begin + 8
        time2 = one_art[time_begin:time_end]
        time2 = time2.replace(':','/',2)
        source_begin = time_end + 3
        source_end = len(articles[j]) - 2
        source2 = one_art[source_begin:source_end]

        score = compare(art1, art2)
        
#       Tally current score
        if score >= 0.5:
            nbr50 = nbr50 + 1
            if score >= 0.6:
                nbr60 = nbr60 + 1
                if score >= 0.7:
                    nbr70 = nbr70 + 1
                    if score >= 0.8:
                        nbr80 = nbr80 + 1
                        if score >= 0.9:
                            nbr90 = nbr90 + 1
                            
#       Calculate direction (ie, which article was published second)
        format = "%Y/%m/%d/%H/%M/%S"
        dt1 = date1 + "/" + time1
        dt1 = datetime.strptime(dt1,format)
        dt2 = date2 + "/" + time2
        dt2 = datetime.strptime(dt2,format)        
        if dt1 < dt2:
            direction = str(j)
        else:
            direction = str(k)

#       Save the result of one comparison        
        one_result = '"'+str(k)+'","'+source1 +'","'+str(j)+'","'+source2+'","'+str(score)+'","'+ direction +'"\n'
        scores.append(one_result)
        if score >= 0.9:
            top_scores.append(one_result)
        m = m + 1
        j = j + 1
    k = k + 1

#   with open('articles.csv', 'r') as articles_file:
#    articles = articles_file.readlines()

#   Save scores
with open('scores.csv', 'w') as scores_file:
    scores_file.writelines(scores)

with open('top_scores.csv', 'w') as top_scores_file:
    top_scores_file.writelines(top_scores)

print("total number of scores:",m)
print("scores >= 0.5 ",nbr50)
print("scores >= 0.6 ",nbr60)
print("scores >= 0.7 ",nbr70)
print("scores >= 0.8 ",nbr80)
print("scores >= 0.9 ",nbr90)
