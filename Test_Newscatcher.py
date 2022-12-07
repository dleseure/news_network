''' Test_Newscatcher.py

    Uses Newscatcher API to fetch the begining of news articles
    about Donald Trump for a specified set of dates.
'''
import time
import csv
import os
import json
import jsonlines
import requests
import pandas

#   Define work folder
os.chdir("E:\\Work1\\Network_project\\test_data")

#   Newscatcher URL
base_url = "https://api.newscatcherapi.com/v2/search"

#   Put API key in headers
headers = {"x-api-key": "9P8V7lNe97wrKE6Z_SaA0wpui3xBCH7CjoFZdxKEWC8"}

#   Define parameters
params = {
    "q": "Donald AND Trump",
    "lang": "en",
    "countries": "US",
    "topic": "politics",
    "to_rank": 1000,
    "page_size": 10,
    "page": 1,
    "from": "2022/11/18"
    }

#   Make a call with both headers and params
response = requests.get(base_url, headers=headers, params=params)

#   Encode received results
results = json.loads(response.text.encode())
if response.status_code == 200:
    print("Done")
else:
    print(results)
    print("ERROR: API call failed.")

#   Variable to store all found news articles
all_news_articles = []

#   Ensure that we start from page 1
params["page"] = 1

#   Infinite loop which ends when all articles are extracted
while True:
    #   Wait for 1 second between each call
    time.sleep(1)

    # GET Call from previous section enriched with some logs
    response = requests.get(base_url, headers=headers, params=params)
    results = json.loads(response.text.encode())
    if response.status_code == 200:
        print(f"Done for page number => {params['page']}")
        
        #   Add parameters to each result to be able to explore afterwards
        for i in results["articles"]:
            i["used_params"] = str(params)

        #   Storing all found articles
        all_news_articles.extend(results["articles"])

        #   Ensuring to cover all pages by incrementing "page" value at each iteration
        params["page"] += 1
        if params["page"] > results["total_pages"]:
            print("All articles have been extracted")
            break
        else:
            print(f"Proceed extracting page number => {params['page']}")
    else:
        print(results)
        print(f"ERROR: API call failed for page number => {params['page']}")
        break

print(f"Number of extracted articles => {str(len(all_news_articles))}")

field_names = list(all_news_articles[0].keys())

#   Create list of article titles
nbr_articles = len(all_news_articles)
print(nbr_articles)
i = 0
for i in range(nbr_articles):
    all_titles[i] = all_news_articles[i]['title']
    i = i + 1

#   Create list of article summaries
i = 0
for i in range(nbr_articles):
    all_summaries[i] = all_news_articles[i]['summary']
    i = i + 1

#   Generate JSONL file from dict
with jsonlines.open('extracted_news_articles.jsonl', mode = "w") as writer:
    writer.write(all_news_articles)
    writer.close()

with open('extracted_news_titles.csv', 'w', encoding="utf-8", newline='') as csvfile:
    filewriter = csv.writer(csvfile, fieldnames="summary", delimiter=",")
    filewriter.writeheader()
    filewriter.writerows(all_titles)
