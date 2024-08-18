#include <iostream>
#include <vector>

using namespace std;

bool isSafe(vector<vector<int>>& board, int row, int col) {
    int i, j;
    int n = board.size();

    // Check this row on left side
    for (i = 0; i < col; i++)
        if (board[row][i])
            return false;

    // Check upper diagonal on left side
    //
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    // Check lower diagonal on left side
    for (i = row, j = col; j >= 0 && i < n; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

bool solveNQUtil(vector<vector<int>>& board, int col) {
    int n = board.size();
    cout << "col: " << col << endl;
    // If all queens are placed
    if (col >= n)
        return true;

    // Consider this column and try placing this queen in all rows one by one
    for (int i = 0; i < n; i++) {
        // Check if the queen can be placed on board[i][col]
        if (isSafe(board, i, col)) {
            // Place this queen in board[i][col]
            board[i][col] = 1;

            // Recur to place rest of the queens
            if (solveNQUtil(board, col + 1))
                return true;

            // If placing queen in board[i][col] doesn't lead to a solution,
            // then remove queen from board[i][col]
            board[i][col] = 0; // BACKTRACK
        }
    }

    //print board

    // If the queen can not be placed in any row in this column col then return false
    return false;
}

void printBoard(const vector<vector<int>>& board) {
    for (const auto& row : board) {
        for (int cell : row) {
            cout << (cell ? "Q " : "_ ");
        }
        cout << endl;
    }
}

void queen(vector<vector<int>>& board) {
    if (!solveNQUtil(board, 0)) {
        cout << "Solution does not exist" << endl;
        printBoard(board);
        return;
    }
    printBoard(board);
}

int main() {
    int board_size = 2;
    vector<vector<int>> board(board_size, vector<int>(board_size, 0));
    queen(board);
    return 0;
}











































































