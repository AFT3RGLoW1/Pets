from html.parser import HTMLParser
import urllib.request

a = input("Your link: ")
url = urllib.request.urlopen(a)
html = url.read().decode()
url.close()


class Parse(HTMLParser):
	def __init__(self):
		super().__init__()
		self.reset()

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, link in attrs:
				if name == "href" and link.startswith("http"):
					print(link)

p = Parse()
p.feed(html)
