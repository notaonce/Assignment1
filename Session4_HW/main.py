import requests
from bs4 import BeautifulSoup
from func import extract
import csv

result_list = []

url = f"https://comic.naver.com/webtoon/weekdayList?week=wed"

info_page = requests.get(url)

info_page_parsing = BeautifulSoup(info_page.text, "html.parser")

info_list_box = info_page_parsing.find("ul", {"class":"img_list"})
info_list = info_list_box.find_all("li")

result_list = extract(info_list)

file = open('./Session4_HW/웹툰리스트.csv', mode = "w", newline='')

writer = csv.writer(file)

writer.writerow(["제목", "작가", "별점"])

for result in result_list:
    row = []
    row.append(result["title"])
    row.append(result["author"])
    row.append(result["rating"])
    writer.writerow(row)



