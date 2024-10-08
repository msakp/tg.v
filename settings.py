URL = "https://tgstat.ru" 
TEST_CHANNEL =  "/en/channel/@black_triangle_tg"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
HEADERS = {
        #"Host": "tgstat.com",
        "User-Agent": USER_AGENT,
        "DNT": "1",
        "Sec-GPC": "1",
        }

RESPONSE_CODE_TABLE = {
        2: "[OK]",
        3: "[OK]",
        4: "[Client Error]",
        5: "[Server Error]",
        }

