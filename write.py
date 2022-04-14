from shared.scrapping import scrapper
from shared.rds import write_db
from shared.config import PAGE_MAX, PAGE_START

sellings = scrapper(PAGE_START, PAGE_MAX)
write_db(sellings)
