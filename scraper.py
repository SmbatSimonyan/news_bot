import asyncio
import re
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://www.aravot.am"

CATEGORIES = {
    "sport": "/category/news/sport/",
    "politics": "/category/news/politics/"
}

TARGET_COUNT = 2500

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


async def fetch(session, url):
    try:
        async with session.get(url, timeout=20) as response:
            return await response.text()
    except:
        return ""


def get_article_links(html):
    soup = BeautifulSoup(html, "lxml")

    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if re.match(
            r"https://www\.aravot\.am/\d{4}/\d{2}/\d{2}/\d+/?",
            href
        ):
            links.add(href)

    return list(links)


def extract_text(html):
    soup = BeautifulSoup(html, "lxml")

    article = soup.find(id="fullstory")

    if article:
        return article.get_text(" ", strip=True)

    return None


async def scrape_category(session, label, path):
    data = []

    page = 1

    while len(data) < TARGET_COUNT:

        url = f"{BASE_URL}{path}page/{page}/"

        print("PAGE:", page)

        html = await fetch(session, url)

        links = get_article_links(html)

        tasks = [
            fetch(session, link)
            for link in links
        ]

        pages = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        for page_html in pages:

            if not isinstance(page_html, str):
                continue

            text = extract_text(page_html)

            if text and len(text) > 300:

                data.append({
                    "text": text,
                    "label": label
                })

            if len(data) >= TARGET_COUNT:
                break

        page += 1

    return data[:TARGET_COUNT]


async def main():

    async with aiohttp.ClientSession(
        headers=HEADERS
    ) as session:

        sport = await scrape_category(
            session,
            "sport",
            CATEGORIES["sport"]
        )

        politics = await scrape_category(
            session,
            "politics",
            CATEGORIES["politics"]
        )

    df = pd.DataFrame(
        sport + politics
    )

    df.to_csv(
        "news_dataset.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("DONE:", len(df))


if __name__ == "__main__":
    asyncio.run(main())