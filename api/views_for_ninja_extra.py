from ninja_extra import NinjaExtraAPI, api_controller, http_get

api = NinjaExtraAPI(urls_namespace='ninja_extra', title='Ninja Extra API')


# function based definition
@api.get("/add", tags=['Math'])
def add(request, a: int, b: int):
    return {"result": a + b}


# class based definition
@api_controller
class MathAPI:

    @http_get('/subtract', )
    def subtract(self, a: int, b: int):
        """Subtracts a from b"""
        return {"result": a - b}

    @http_get('/divide', )
    def divide(self, a: int, b: int):
        """Divides a by b"""
        return {"result": a / b}

    @http_get('/multiple', )
    def multiple(self, a: int, b: int):
        """Multiples a with b"""
        return {"result": a * b}


api.register_controllers(
    MathAPI
)
