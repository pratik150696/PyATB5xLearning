
class OldBrowser:

    def start_browser(self):
        print("IE Browser is Starting")

    def stop_browser(self):
        print("IE Browser is Closing")

class Chrome(OldBrowser):

    def start_browser(self):
        super().start_browser()          # Parent Start Browser Also
        print("Better Chrome Browser is Starting!!!")

    def stop_browser(self):
        print("Better Chrome Browser is Closing!!!")

object_ref = Chrome()
object_ref.start_browser()
object_ref.stop_browser()