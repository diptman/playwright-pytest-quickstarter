class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.locator("user-name")
