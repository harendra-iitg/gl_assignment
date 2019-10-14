import asyncio
import concurrent.futures
from parallel_request import ParallelRequest
from queue_processor import QueueProcessor
import urllib
import xmltodict
from queue_processor import QueueProcessor


q = QueueProcessor()
sitemap_url = "https://www.greatlearning.in/website_sitemap.xml"
data = urllib.request.urlopen(sitemap_url)
xml_dist = xmltodict.parse(data.read()) # parsing the xml data
url_arr = xml_dist['urlset']['url']

count = 1
arr = []

# adding data in queue (each queue node contains array of 5 urls)
for url in url_arr:
    if count % 5 == 0:
        q.add_data(arr)
        arr = []
    arr.append(url['loc'])
    count += 1
q.add_data(arr)

# Getting data from queue and processing 5 urls at a time

while not q.is_empty():
    url_arr = q.get_data()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ParallelRequest(url_arr).parallel_call())
