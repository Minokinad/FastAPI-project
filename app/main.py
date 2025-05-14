from datetime import date
from typing import Optional

from fastapi import FastAPI, Query, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

from app.bookings.router import router as bookings_router

app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(bookings_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

class SHotel(BaseModel):
    name: str
    address: str
    stars: int

class SearchHotelArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

@app.get("/hotels/")
def get_hotels(
    search_args: SearchHotelArgs = Depends(),
) :

    hotels = [
        {
            "name": "Five days",
            "address": f"{search_args.location}",
            "stars": search_args.stars,
        }
    ]
    return hotels

class BookingRequest(BaseModel):
    hotel_id: int
    date_from: date
    date_to: date
@app.post("/bookings/")
def book(booking: BookingRequest):
    pass
@app.get("/docs")
async def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )