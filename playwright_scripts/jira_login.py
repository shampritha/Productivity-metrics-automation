from playwright.sync_api import sync_playwright


def jira_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto("https://your-jira-url.com")

        print("Jira page opened")

        browser.close()


if __name__ == "__main__":

    jira_login()