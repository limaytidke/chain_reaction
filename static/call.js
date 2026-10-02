let middle = document.querySelector(".game");

async function loadBoard() {
    const getBoard = await fetch("/board");
    const getBoardRes = await getBoard.json();
    const board = getBoardRes.board;

    board.forEach((row) => {
        row.forEach((col) => {
            middle.innerHTML += `${col} `;
        });
        middle.innerHTML += "<br>";
    });
    middle.innerHTML += "<br>";
    console.log("WORIN")
}

async function updateBoard() {
    const res = await fetch("/sendCoord" , {
        method : "POST",
        headers : {"Content-Type" : "application/json" },
        body : JSON.stringify({row : "5", col : "5"})
    });
    const data = await res.json();
    const board = data.updatedBoard;
    console.log(board);
    middle.innerHTML = "";

    board.forEach((row) => {
        row.forEach((col) => {
            middle.innerHTML += `${col} `;
        });
        middle.innerHTML += "<br>";
    });
    middle.innerHTML += "<br>";
    console.log("WORIN")
}

loadBoard();
