#include<map>
#include<unordered_set>
#include<vector>
using namespace std;
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<pair<int, int>, unordered_set<char>> squares;
        map<int, unordered_set<char>> rows, cols;
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                pair<int, int> squareKey = {r / 3, c / 3};
                if (rows[r].count(board[r][c]) || 
                    cols[c].count(board[r][c]) || 
                    squares[squareKey].count(board[r][c])) return false;

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[squareKey].insert(board[r][c]);
            }
        }
        return true;
    }
};
