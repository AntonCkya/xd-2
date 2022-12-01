from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from routers import comments, countries, genres, movies, users

from models.db_engine import metadata, engine
metadata.create_all(engine)


app = FastAPI()

app.include_router(comments.router)
app.include_router(countries.router)
app.include_router(genres.router)
app.include_router(movies.router)
app.include_router(users.router)

origins = [
    "http://localhost"
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# root
@app.get('/', tags=["root"])
async def test():
	return {"xd": "api"}


def custom_openapi():
	if app.openapi_schema:
		return app.openapi_schema
	openapi_schema = get_openapi(
    	title="[ xd ]",
		version="0.0.2",
		description="API к онлайн-кинотеатру [ xd ]",
		routes=app.routes,
	)
	app.openapi_schema = openapi_schema
	return app.openapi_schema

app.openapi = custom_openapi
