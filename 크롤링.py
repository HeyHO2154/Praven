from playwright.sync_api import sync_playwright

def scrape_page_text(url):
    with sync_playwright() as p:
        # 브라우저 열기
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 페이지 열기
        page.goto(url)

        # 텍스트가 로드될 때까지 대기
        page.wait_for_selector("body", timeout=10000)  # 페이지가 로드되었는지 확인

        # 전체 텍스트 가져오기
        text_content = page.evaluate("document.body.innerText")

        print(text_content)

        # 브라우저 닫기
        browser.close()

url = "https://glaw.scourt.go.kr/wsjo/panre/sjo050.do#1735630086803"
scrape_page_text(url)
