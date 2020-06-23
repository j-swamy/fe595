import requests
from bs4 import BeautifulSoup

def scrape(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	getName = soup.find_all("li", string = lambda text: "name:" in text.lower())
	getPurpose = soup.find_all("li", string = lambda text: "purpose:" in text.lower())
	companyPurpose = getPurpose[0].text[9:]
	companyName = getName[0].text[6:]
	return companyName + ", " + companyPurpose + "\n"

if __name__ == "__main__":
	url = "http://18.207.112.240:8000/random_company"
	f = open("results.txt", "w")
	f.write("Name, Purpose\n")
	for i in range(50):
		myString = scrape(url)
		f.write(myString)
	f.close()
