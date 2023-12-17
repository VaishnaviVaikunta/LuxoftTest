# from playwright.sync_api import Playwright
from utils.utils import *
import pytest

#fixture to be executed before every test case
@pytest.fixture
def browserPage(playwright: Playwright):
    return launchBroswer(playwright)

#test case 1: Add items to the cart and verify all the items are added to the cart
def test_addItems(browserPage):
    #Test data
    testSite = "https://todomvc.com/examples/angularjs/#/"
    items = ["Apple", "Orange", "Beef"]
    #Test steps
    launchWebsite(browserPage, testSite)
    addItems(browserPage, items)
    if not verifyItems(browserPage, items):
        pytest.fail("Specified item not found")
    takeScreenShot(browserPage, "Tests/screenshots/addItems.jpg")
    closeBrowser(browserPage)

#test case 2: Check the checkbox of an item, verify and modify the cart and verify  the modified item
def test_modifyItems(browserPage):
    #Test data
    testSite = "https://todomvc.com/examples/angularjs/#/"
    items = ["Apple", "Orange", "Beef"]
    itemToChange = "Beef"
    newItem = "Chicken"
    itemToCheck = "Apple"
    #Test steps
    launchWebsite(browserPage, testSite)
    addItems(browserPage, items)
    if not checkItem(browserPage, itemToCheck):
        pytest.fail("Specified item cannot be checked")
    if not verifyCheckedItem(browserPage, itemToCheck):
        pytest.fail("Specified item is not checked as it is not found")
    if not changeItem(browserPage, itemToChange, newItem):
        pytest.fail("Item cannot be changed")
    verifyItems(browserPage,[newItem])
    takeScreenShot(browserPage, "Tests/screenshots/modifiedItems.jpg")
    closeBrowser(browserPage)











