import asyncio
import concurrent.futures
import urllib.request as urllib2
from data_processor import DataProcessor

class ParallelRequest:
    def  __init__(self, url_arr):
        self.url_arr = url_arr
        self.data_processor = DataProcessor()

    async def parallel_call(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor,
                    urllib2.urlopen,
                    url
                )
                for url in self.url_arr
            ]
            for response in await asyncio.gather(*futures):
                content_type = response.getheader('Content-Type')
                self.data_processor.process_data(response.geturl(), content_type, response.read())
                
