from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "GMAN DID THIS"}

# Added OPTIONS method to handle CORS preflight requests
@app.options("/")
def options_root():
    # Return an empty response with a JSON media type
    return JSONResponse(content={}, media_type="application/json")

@app.get("/bbc-news")
async def get_bbc_news():
    response = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=12d7902e5d394fbaafbc43ba299fa50f")
    return response.json() 

# Added OPTIONS method to handle CORS preflight requests
@app.options("/bbc-news")
def options_bbc_news():
    # Return an empty response with a JSON media type
    return Response(content="", media_type="application/json")

@app.get("/techcrunch-news")
async def get_techcrunch_news():
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines?",
        params={
            "apiKey": "12d7902e5d394fbaafbc43ba299fa50f",
            "sources": "techcrunch",
            "language": "en"
        }
    )
    return response.json()


@app.get("/zim-news")
async def get_news():
    url = "https://newsdata.io/api/1/news?apikey=pub_4560054a110f686b5a82c65856438ab007856&q=zimbabwe&country=zw&category=top"
    response = requests.get(url)
    return Response(content=response.text, media_type="application/json")

@app.get("/tech-sources")
async def get_tech_sources():
    url = "https://newsapi.org/v2/top-headlines/sources"
    params = {
        "category": "technology",
        "apiKey": "12d7902e5d394fbaafbc43ba299fa50f"
    }
    response = requests.get(url, params=params)
    return Response(content=response.text, media_type="application/json")

