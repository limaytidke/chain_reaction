let middle = document.querySelector(".game");
let boardSize = 10;
let cellColor = {
    1 : "red",
    2 : "green",
};
let Color = {
    "red" : 1,
    "green" : 2,
};
let playerColor = "red";

async function loadBoard() {
    const getBoard = await fetch("/board");
    const getBoardRes = await getBoard.json();
    const board = getBoardRes.board;

    for (let row = 0; row < boardSize; row++) {
        for (let col = 0; col < boardSize; col++) {
            const button = document.createElement("button");
            button.innerText = board[row][col];
            button.addEventListener("click", () => {
                updateBoard(row+1,col+1);
            });
            middle.appendChild(button);
        }
    }
}

async function updateBoard(row,col) {
    let playerCellColor = Color[playerColor];
    console.log(playerCellColor);
    const targetDiv = document.querySelector(".game");
    const buttons = targetDiv.querySelectorAll("button");
    const buttonAccess = buttons[row * boardSize + col];

    const res = await fetch("/sendCoord" , {
        method : "POST",
        headers : {"Content-Type" : "application/json" },
        body : JSON.stringify({row : row, col : col, color: playerCellColor })
    });
    const data = await res.json();
    const board = data.updatedBoard;
    if (board == "error") {
        console.log("cell is not yours");
    }
    else {
        console.log(board);
        playerColor = cellColor[(playerCellColor%2)+1];


        for (let row = 0; row < boardSize; row++) {
            for (let col = 0; col < boardSize; col++) {
                buttons[row * boardSize + col].innerText = board[row][col][0];
                if (board[row][col][1] == "red") { buttons[row * boardSize + col].style.backgroundImage = "url('assets/red.png')"; }
                else if (board[row][col][1] == "green") { buttons[row * boardSize + col].style.backgroundImage = "url('assets/green.png')"; }
            }
        }
    }
}

loadBoard();
