class MyService:

    def __init__(self, sso_registry):
        self.sso_registry = sso_registry

    def handle_request_correctly(self, request, token):
        if self.sso_registry.is_valid(token):
            return "hello world"
        return "please enter your login details"

    def handle_request_wrong_token(self, request, token):
        if self.sso_registry.is_valid(None):
            return "hello world"
        return "please enter your login details"

    def handle_request_no_call_to_is_valid(self, request, token):
        if token:
            return "hello world"
        return "please enter your login details"

    # test switcher fake/mock/spy
    handle_request = handle_request_correctly
    # handle_request = handle_request_wrong_token  # mock/spy tests fail
    # handle_request = handle_request_no_call_to_is_valid  # all tests fail
