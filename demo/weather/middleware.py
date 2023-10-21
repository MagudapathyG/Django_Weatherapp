class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('before middlw ware')

        response = self.get_response(request)
        print('After Middleware')

        # Code to be executed for each request/response after
        # the view is called.

        return response