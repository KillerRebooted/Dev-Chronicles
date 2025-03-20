import requests, os
from bs4 import BeautifulSoup as bs

clear = lambda: os.system('cls')

clear()

headers = { 'Authority': 'api.dex.guru', 'Method': 'GET', 'Path': '/v1/tokens/0x8076C74C5e3F5852037F31Ff0093Eeb8c8ADd8D3-bsc', 'Scheme': 'https', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'Sec-Ch-Ua': 'Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54' }

response = requests.get("https://steamunlocked.net/all-games-2/", headers=headers)

soup = bs(response.text, "html.parser")

games = [i.get_text() for i in soup.find_all("a") if not i.has_attr("class") and "Download" in i.get_text()]

with open(f"{__file__.removesuffix(os.path.basename(__file__))}\\Games.txt", "w+", encoding="utf-8") as f:
    for i in games: f.write(f"{i}\n")

total_games = len(games)
print(f"There are {total_games} on Steamunlocked\n")

while True:

    search = input("Enter the Search Term (0 to exit): ")

    clear()

    if search == "0":
        break

    else:

        results = 0

        for i in games:

            match = True

            for j in search.split():

                if j.lower() in i.lower(): pass
                else: match = False

            if match:
                print(i)
                results += 1

        print(f"\n{results} Results out of {total_games} Games")
