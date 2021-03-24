# Python program to scrape website
# and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://docs.python.org/es/3/tutorial"
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html5lib")

indice = []  # a list to store quotes

table = soup.find("div", attrs={"class": "toctree-wrapper compound"})
for l_one in table.findAll("li", attrs={"class": "toctree-l1"}):
    # print(l_one.a.text, l_one.a["href"])
    l_one_dict = {}
    l_one_dict["Titulo"] = l_one.a.text
    l_one_dict["Link"] = URL + "/" + l_one.a["href"]
    indice_l_two = []
    for l_two in l_one.findAll("li", attrs={"class": "toctree-l2"}):
        # print(l_two.a.text, l_two.a["href"])
        l_two_dict = {}
        l_two_dict["Titulo"] = l_two.a.text
        l_two_dict["Link"] = URL + "/" + l_two.a["href"]
        indice_l_three = []
        for l_three in l_two.findAll("li", attrs={"class": "toctree-l3"}):
            # print(l_three.a.text, l_three.a["href"])
            l_three_dict = {}
            l_three_dict["Titulo"] = l_three.a.text
            l_three_dict["Link"] = URL + "/" + l_three.a["href"]
            indice_l_four = []
            for l_four in l_three.findAll("li", attrs={"class": "toctree-l4"}):
                # print(l_four.a.text, l_four.a["href"])
                l_four_dict = {}
                l_four_dict["Titulo"] = l_four.a.text
                l_four_dict["Link"] = URL + "/" + l_four.a["href"]
                indice_l_four.append(l_four_dict)
            l_three_dict["subindice"] = indice_l_four
            indice_l_three.append(l_three_dict)
        l_two_dict["subindice"] = indice_l_three
        indice_l_two.append(l_two_dict)
    l_one_dict["subindice"] = indice_l_two
    indice.append(l_one_dict)

for dicty_l_one in indice:
    for key_l_one in dicty_l_one:
        if not key_l_one == "subindice":
            print(key_l_one, "->", dicty_l_one[key_l_one])
        else:
            for dicty_l_two in dicty_l_one[key_l_one]:
                for key_l_two in dicty_l_two:
                    if not key_l_two == "subindice":
                        print("\t" + key_l_two, "->", dicty_l_two[key_l_two])
                    else:
                        for dicty_l_three in dicty_l_two[key_l_two]:
                            for key_l_three in dicty_l_three:
                                if not key_l_three == "subindice":
                                    print(
                                        "\t\t" + key_l_three,
                                        "->",
                                        dicty_l_three[key_l_three],
                                    )
                                else:
                                    for dicty_l_four in dicty_l_three[key_l_three]:
                                        for key_l_four in dicty_l_four:
                                            if not key_l_four == "subindice":
                                                print(
                                                    "\t\t\t" + key_l_four,
                                                    "->",
                                                    dicty_l_three[key_l_four],
                                                )
