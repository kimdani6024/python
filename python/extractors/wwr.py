from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


browser = webdriver.Chrome(options=options)


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    browser.get(f"{base_url}{keyword}")
    results = []

    soup = BeautifulSoup(browser.page_source, "html.parser")
    jobs = soup.find_all("section", class_="jobs")

    for job_section in jobs:
        job_posts = job_section.find_all("li")
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all("a")
            anchor = anchors[1]
            link = anchor["href"]

            company, kind, region = anchor.find_all("span", class_="company")

            title = anchor.find("span", class_="title")
            # print(company.string, kind.string, region.string, title.string)
            # print("///////////////////")

            job_data = {
                "link": f"https://weworkremotely.com/{link}",
                "location": region.string.replace(",", " "),
                "company": company.string.replace(",", " "),
                "position": title.string.replace(",", " "),
            }
            results.append(job_data)

        # print(results)
        # for result in results:
        #   print(result)
        #   print("///////")
    return results
