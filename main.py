import requests
from bs4 import BeautifulSoup

PAGE_MAX = 1 # 501 페이지까지 있는듯?
page_num = 1

while page_num <= PAGE_MAX:
    page = requests.get(f"https://cafe.naver.com/ArticleList.nhn?search.clubid=20486145&search.menuid=214&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.cafeId=20486145&search.page={page_num}")
    page_parsed = BeautifulSoup(page.text, "html.parser")

    trs = page_parsed.find_all("tr")
    del trs[0:95]

    for tr in trs: 
        title_td = tr.find("td",{"class": "td_article"})
        if title_td:
            print("----------------------------------------------------------------------------")
            print(title_td.find("div", {"class": "board-list"}).text.strip())    
        date_td = tr.find("td",{"class": "td_date"})
        if date_td:
            print(date_td.text)
        view_td = tr.find("td",{"class": "td_view"})
        if view_td:
            print(view_td.text)
        like_td = tr.find("td",{"class": "td_likes"})
        if like_td:
            print(like_td.text)
    page_num = page_num + 1