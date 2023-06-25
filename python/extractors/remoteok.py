from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


# 403 권한없음이 표시된다.
# selenium 실제로 웹브라우저를 실행 : 코드를 사용해서 브라우저를 자동화하고 제어 할 수 있는 방법
# google driver를 설치한다.
# https://stackoverflow.com/questions/76461596/unable-to-use-selenium-webdriver-getting-two-exceptions 참조해서 크롤링.


options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


browser = webdriver.Chrome(options=options)


def extract_remoteok_jobs(keyword):
    results = []

    base_url = f"https://remoteok.io/remote-dev+{keyword}-jobs"
    browser.get(base_url)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    div = soup.find_all("div", class_="container")

    for td in div:
        td_list = td.find_all("td", class_="company_and_position")

        for list in td_list:
            url = list.find_all("a", {"itemprop": "url"})
            for archor in url:
                link = f"https://remoteok.io{archor.get('href')}"

                # print(results)
                # print("/////////////////////////")
                # print("/////////////////////////")
                for h2_find in url:
                    title = h2_find.find("h2", {"itemprop": "title"}).string.replace(
                        "\n", ""
                    )

                    # print(results)

            company_name = list.find_all("span", {"itemprop": "hiringOrganization"})
            for name in company_name:
                company = name.find("h3", {"itemprop": "name"}).string.replace("\n", "")
                # print(results)
                location = "None"
                job_data = {
                    "link": link,
                    "company": company,
                    "location": location,
                    "position": title,
                }
                results.append(job_data)

    return results
