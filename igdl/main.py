import requests
from bs4 import BeautifulSoup as bs

class Ingfo:
  def __init__(self, url):
    self.url = url
    self.home = "https://downloadgram.org"
    self.data = {
      "url": self.url
    }
    self.head = {
      "user-agent": "Chrome"
    }

  def Image(self):
    ses = requests.Session()
    req = ses.post(self.home, headers=self.head, data=self.data)
    soup = bs(req.text, "html.parser").find("div", {"id": "par-content"})
    img = []
    for i in soup.findAll("a"):
      img.append(i["href"])

    return img

  def Source(self):
    ses = requests.Session()
    req = ses.post(self.home, headers=self.head, data=self.data)
    soup = bs(req.text, "html.parser").find("div", {"id": "par-content"})
    sorc = []
    for i in soup.findAll("img"):
      sorc.append(i["src"])

    return sorc
