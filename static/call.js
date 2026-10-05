let middle = document.querySelector(".game");
let boardSize = 10;

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
    const res = await fetch("/sendCoord" , {
        method : "POST",
        headers : {"Content-Type" : "application/json" },
        body : JSON.stringify({row : row, col : col})
    });
    const data = await res.json();
    const board = data.updatedBoard;
    console.log(board);

    const targetDiv = document.querySelector(".game");
    const buttons = targetDiv.querySelectorAll("button");

    for (let row = 0; row < boardSize; row++) {
        for (let col = 0; col < boardSize; col++) {
            buttons[row * boardSize + col].innerText = board[row][col];
            buttons[row * boardSize + col].style.backgroundImage = "url('./assets/green.png')";
        }
    }
}

loadBoard();
