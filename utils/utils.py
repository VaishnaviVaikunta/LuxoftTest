from playwright.sync_api import Playwright,  expect, Page


# method to open browser
def launchBroswer(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return page

#method to launch Website
def launchWebsite(page, testSite):
    page.goto(testSite)

#method to close browser
def closeBrowser(page):
    page.close()

#method to add items to the cart
def addItems(page,items):
    for each in items:
        page.get_by_placeholder("What needs to be done?").fill(each)
        page.keyboard.press("Enter")

#method to verify items in the cart
def verifyItems(page, items):
    for each in items:
        try:
            expect(page.locator("ng-view")).to_contain_text(each)
        except AssertionError:
            print(f'Item {each} not found!')
            return False
    return True

#method to take screenshot of the page
def takeScreenShot(page, path):
    page.screenshot(path=path, full_page=True)

#method to check the item in the dropdown
def checkItem(page:Page, item):
    try:
        if page.locator("div").filter(has_text=item).is_visible(timeout=10.000):
            page.locator("div").filter(has_text=item).get_by_role("checkbox").check()
            return True
        else:
            raise TimeoutError
    except TimeoutError:
        print(f'Item {item} not found!')
        return False


#method to verify if an item is checked in the dropdown
def verifyCheckedItem(page: Page,item):
    try:
        expect(page.locator("div").filter(has_text=item).get_by_role("checkbox")).to_be_checked(timeout=10.00)
        return True
    except AssertionError:
        print(f'Item {item} is not checked!')
        return False
    except TimeoutError:
        print(f'Item {item} not found!')
        return False

#method to change an item in the dropdown
def changeItem(page: Page, oldItem, newItem):
    try:
        if page.locator("li").filter(has_text=oldItem).is_visible(timeout=10.00):
            page.locator("li").filter(has_text=oldItem).dblclick()
            page.locator("li").filter(has_text=oldItem).get_by_role("textbox").fill(newItem)
            return True
        else:
            raise TimeoutError
    except TimeoutError:
        print(f'Item {oldItem} not found!')
        return False
