import sys
from time import sleep
import numpy as np

class Cell:
    numberOfAtoms:int = 0
    atomLimit:int = 3

class Game:
    def __init__(self,height:int = 10,width:int = 10) -> None:
        self.height:int = height
        self.width:int = width

        board:list[list[Cell]] = [[Cell() for i in range(self.width)] for i in range(self.height)]
        self.board = np.array(board,dtype = object)

    def renderBoard(self) -> None:
        sys.stdout.write("\033[H\n    ")
        for i in range(self.width): sys.stdout.write(f"  {i + 1}  ")
        sys.stdout.write("\n")
        for i in range (self.height):
            sys.stdout.write(f" {i + 1} ")
            for j in range(self.width): sys.stdout.write(f"   {self.board[i][j].numberOfAtoms} ")
            sys.stdout.write("\n")

    def updateCell(self,cell,atom):
        cell.numberOfAtoms = atom;

    def checkCellReaction(self,cell):
        queue = [cell]
        while len(queue) > 0:
            frontCell = queue[0]
            queue.remove(frontCell)
            noAtom,limit = frontCell.numberOfAtoms,frontCell.atomLimit

            if noAtom >= limit:
                noAtom = noAtom % limit
                coords = np.where(self.board == frontCell)
                y,x = int(coords[0][0]),int(coords[1][0])
                if x - 1 >= 0:
                    cell = self.board[y][x-1]
                    cell.numberOfAtoms += 1
                    queue.append(cell)
                if x + 1 < self.width:
                    cell = self.board[y][x+1]
                    cell.numberOfAtoms += 1
                    queue.append(cell)
                if y - 1 >= 0:
                    cell = self.board[y-1][x]
                    cell.numberOfAtoms += 1
                    queue.append(cell)
                if y + 1 < self.height:
                    cell = self.board[y+1][x]
                    cell.numberOfAtoms += 1
                    queue.append(cell)
            
            self.updateCell(frontCell,noAtom)
            #sleep(0.5)
            #self.renderBoard();


    def addAtom(self,coord:list[str]):
        x,y = int(coord[0]),int(coord[1])
        cell = self.board[y - 1][x - 1]
        self.updateCell(cell=cell,atom=cell.numberOfAtoms + 1)
        self.checkCellReaction(cell)

    def start(self):
        while True:
            self.renderBoard()
            coord = input("\nEnter cell: ").split(',')
            self.addAtom(coord)

def main():
    game = Game()
    game.start()

if __name__ == '__main__':
    main()
