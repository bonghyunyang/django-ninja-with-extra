from ninja import NinjaAPI

api = NinjaAPI(urls_namespace='pure_ninja', title='Pure Ninja API')


# function based definition
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


# pure ninja doesn't support class based definition
# in this case, you can use ninja_extra (refrence: api/views_for_ninja_extra.py)
