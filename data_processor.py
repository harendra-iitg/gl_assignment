from html.parser import HTMLParser

class DataProcessor:
    def __init__(self):
        self.parser = TitleParser()

    def process_data(self, url, content_type, data):
        print("\n url: ", url)
        self.parser.feed(str(data))
        print("\n Title:", self.parser.title)
        print("\n Content-Type:", content_type)
        #print("\n RawContent:", data) # Uncomment this line to display raw data

class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.match = False
        self.title = ''

    def handle_starttag(self, tag, attributes):
        self.match = True if tag == 'title' else False

    def handle_data(self, data):
        if self.match:
            self.title = data
            self.match = False
