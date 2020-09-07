from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for k, v  in attrs:
            print(f"-> {k} > {v}")
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for k, v  in attrs:
            print(f"-> {k} > {v}")
    def handle_comment(self, data):
        return None

parser = MyHTMLParser()

for n in range(int(input())):
        parser.feed(input())
