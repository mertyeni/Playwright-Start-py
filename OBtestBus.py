from playwright.sync_api import sync_playwright

def test_Bus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://obilet.com")

        page.click("#accept")
        page.wait_for_timeout(1000)

        page.click("button#search-button")
        page.wait_for_load_state('load')

        # Pop-up'ın geldiğinden emin ol, 5 saniye bekle
        page.wait_for_selector("#close-button-1454703513200", timeout=10000)
        page.click("#close-button-1454703513200")

        page.wait_for_timeout(1000)
        page.click("xpath=//*[@id='journey-1026679807']/div[1]/div[5]")
        page.wait_for_timeout(1000)

if __name__ == "__main__":
    test_Bus()
