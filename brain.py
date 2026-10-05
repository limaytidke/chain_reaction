import sys
from time import sleep
import numpy as np
from collections import deque

cellColor = {
    1: "red",
    2: "green",
}

Color = {
    "red": 1,
    "green": 2,
}


class Cell:
    numberOfAtoms: int = 0
    atomLimit: int = 3
    color: str = ""


class Game:
    def __init__(self, height: int = 10, width: int = 10) -> None:
        self.height: int = height
        self.width: int = width

        board: list[list[Cell]] = [
            [Cell() for i in range(self.width)] for i in range(self.height)
        ]
        self.board = np.array(board, dtype=object)

    def renderBoard(self) -> None:
        sys.stdout.write("\033[H\n    ")
        for i in range(self.width):
            sys.stdout.write(f"  {i + 1}  ")
        sys.stdout.write("\n")
        for i in range(self.height):
            sys.stdout.write(f" {i + 1} ")
            for j in range(self.width):
                sys.stdout.write(f"   {self.board[i][j].numberOfAtoms} ")
            sys.stdout.write("\n")

    def updateCell(self, cell, atom, color):
        if (cell.color == "" or cell.color == cellColor[color]):
            cell.numberOfAtoms = atom
            cell.color = cellColor[color]
            return 1
        else:
            return 0

    def checkCellReaction(self, cell, y, x):
        frontCell: Cell = cell
        noAtom, limit = frontCell.numberOfAtoms, frontCell.atomLimit
        color = Color[frontCell.color]

        if noAtom >= limit:
            noAtom = 0
            neighbors = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
            for ny, nx in neighbors:
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    ncell: Cell = self.board[ny][nx]
                    ncell.numberOfAtoms += 1
                    ncell.color = cellColor[color]
                    self.updateCell(frontCell, noAtom, color)
                    self.checkCellReaction(ncell, ny, nx)

            # sleep(0.5)
            # self.renderBoard();

    def addAtom(self, coord: list[int]):
        y, x, color = coord[0], coord[1], coord[2]
        cell = self.board[y - 1][x - 1]
        self.updateCell(cell=cell, atom=cell.numberOfAtoms + 1, color=color)
        self.checkCellReaction(cell, y - 1, x - 1)

    def start(self):
        while True:
            self.renderBoard()
            coord = input("\nEnter cell: ").split(",")
            self.addAtom(coord)


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
