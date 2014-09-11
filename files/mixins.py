class Auth(object):
    name = "BaseAuth"
    logged_in = False
    def is_user_authenticated(self):
        return self.logged_in

class OAuth1(object):
    def three_legged_auth(self):
        return call_provider()

class OAuth2(object):
    def two_legged_auth(self):
        return call_provider()

class Google(Auth, OAuth2):
    name = "Google"
    def login(self):
        logged_in = self.two_legged_auth()

class Yahoo(Auth, OAuth1):
    name = "Yahoo"
    def login(self):
        logged_in = self.three_legged_auth()

g = Google()
y = Yahoo()

