from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://obilet.com")

        print("İlk Sayfa Başlığı:", page.title())

        page.click("xpath=//*[@id='header']/div[1]/div/div[2]/ul/li[5]/a")
        page.wait_for_timeout(1500)

        page.fill("input[name='username']", "example@gmail.com")
        page.wait_for_timeout(1500)

        page.fill("input[name='password']", "testpass1234+")
        page.wait_for_timeout(1000)

        page.click("xpath=//*[@id='login-form']/div[5]/button[1]")
        page.wait_for_selector("xpath=//*[@id='header']/div[1]/div/div[2]/ul/li[4]")

        page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        page.click("button#search-button")
        page.wait_for_load_state('load')

        print("İkinci sayfa başlığı:", page.title())

        assert "İstanbul" in page.title()

if __name__ == "__main__":
    test_login()
