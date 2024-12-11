from browserPackage.OpenBrowser import start_browser
from browserPackage.StopBrowser import stop_Browser


def test_Case():
    start_browser()
    print("Hello Running TC")
    stop_Browser()


test_Case()
