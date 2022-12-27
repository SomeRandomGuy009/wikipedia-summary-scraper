# import libraries
import requests
import os

def get_wikipedia_summaries(query):
  summaries = []

  # wikipedia api request to get search results
  url = "https://en.wikipedia.org/w/api.php"
  params = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": query,
    "utf8": 1,
    "formatversion": 2,
    "format": "json",
    "srlimit": 500
  }
  r = requests.get(url, params=params)
  data = r.json()

  # append search results to a list
  search_results = data['query']['search']

  # Get the summary for each search result
  for search_result in search_results:
    page_id = search_result['pageid']

    # wikipedia api request to get the summaries
    params = {
      "action": "query",
      "format": "json",
      "pageids": page_id,
      "utf8": 1,
      "formatversion": 2,
      "prop": "extracts",
      "exintro": 1,
      "explaintext": 1
    }
    r = requests.get(url, params=params)
    data = r.json()

    # Add the summary to the list
    summaries.append(data['query']['pages'][0]['extract'])

  return summaries

# Stuff
query = []
count = 0
print("Started.")
for queries in query:
   os.system(f"touch {queries}.txt")
   with open(f"{queries}.txt", "w") as output_file:
       summaries = get_wikipedia_summaries(queries)
       for summary in summaries:
         output_file.write(summary + "\n")
         count+=1
         print(count, "out of", (len(query)*500), "queries done")
