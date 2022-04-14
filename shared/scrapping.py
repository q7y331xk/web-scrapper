import requests
from bs4 import BeautifulSoup

def scrapper(page_num=1, page_max=1):
    new_sellings = []
    id = 1
    while page_num <= page_max:
        page = requests.get(f"https://cafe.naver.com/ArticleList.nhn?search.clubid=20486145&search.menuid=214&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.cafeId=20486145&search.page={page_num}")
        page_parsed = BeautifulSoup(page.text, "html.parser")

        trs = page_parsed.find_all("tr")
        del trs[0:95]

        for tr in trs:
            title = ""
            comments = "0"
            date = ""
            views = ""
            likes = ""
            title_td = tr.find("td",{"class": "td_article"})
            if title_td:
                title_div = title_td.find("div", {"class": "board-list"})
                title = title_div.find("a",{"class": "article"}).text.strip()
                cmt = title_div.find("a",{"class": "cmt"})
                if cmt:
                    comments = cmt.text.strip().strip("[""]")
                date_td = tr.find("td",{"class": "td_date"})
                if date_td:
                    date = date_td.text.strip()
                view_td = tr.find("td",{"class": "td_view"})
                if view_td:
                    views = view_td.text.strip()
                like_td = tr.find("td",{"class": "td_likes"})
                if like_td:
                    likes = like_td.text.strip()
                new_sellings.append({'id': id,'title': title, 'comments': comments, 'date': date, 'views': views, 'likes': likes})
                id = id + 1
        print(f"page {page_num}/{page_max} done")
        page_num = page_num + 1
    return new_sellings