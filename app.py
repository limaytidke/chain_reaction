from brain import Game
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

game = Game()

class Coords(BaseModel):
    row: str
    col: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/board")
def board():
    gameBoard = [[ game.board[i][j].numberOfAtoms for j in range(game.width)] for i in range(game.height)]
    return { "board" : gameBoard }

@app.post("/sendCoord")
async def updateCell(coords: Coords):
    game.addAtom([coords.row,coords.col])
    gameBoard = [[ game.board[i][j].numberOfAtoms for j in range(game.width)] for i in range(game.height)]
    return { "updatedBoard" : gameBoard }
