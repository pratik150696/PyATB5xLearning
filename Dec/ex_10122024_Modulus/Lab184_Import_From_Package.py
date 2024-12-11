from browserPackage.OpenBrowser import start_browser
from browserPackage.StopBrowser import stop_Browser

class TestCase:

    def test_Case(self):
        start_browser()
        print("Hello Running TC")
        stop_Browser()

object_TestCase = TestCase()
object_TestCase.test_Case()