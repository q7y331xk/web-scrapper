from scrapping import scrapper
from rds import write_db
from config import PAGE_MAX, PAGE_START

sellings = scrapper(PAGE_START, PAGE_MAX)
write_db(sellings)
