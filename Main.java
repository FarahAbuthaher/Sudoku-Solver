package com.company;
class Sudoku{
    static void printBoard(int[][] bo)
    {
        for (int i=0; i< bo.length; i= i+1) {
            if (i%3 ==0) {
                System.out.println("-------------------------");
            }
            for (int j=0; j< bo[0].length; j= j+1){
                if (j %3==0){
                    System.out.print( "| ");
                }
                if (j == 8){
                    System.out.println(bo[i][j]+" |");

                }else {
                    System.out.print(bo[i][j] +" ");
                }
            }
        }
        System.out.println("-------------------------");
    }
    int[] findEmpty (int[][] bo){
        for (int i=0; i< bo.length; i++){
            for (int j=0; j< bo[0].length; j++){
                if (bo[i][j]==0){
                    int[] pos = {i,j};
                    return pos;
                }
            }
        }
        return null;
    }
    boolean checkPos (int[][] bo, int num, int[] pos){
        // check for column
        for (int i=0; i< bo.length; i= i+1){
            if (num == bo[i][pos[1]] && i != pos[0]){
                return false;
            }
        }
        // check for rows
        for (int i=0; i< bo[0].length; i= i+1){
            if (num == bo[pos[0]][i] && i != pos[1]){
                return false;
            }
        }
        // check box
        int x = pos[1] / 3;
        int y = pos[0] / 3;
        for (int i = y*3; i < y*3+3; i++){
            for (int j = x*3; j < x*3+3; j++){
                if (bo[i][j] == num && (pos[0] !=i && pos[1] != j)){
                    return false;
                }
            }
        }
        return true;
    }
    boolean solveSudoku (int[][] bo){
        int[] find = findEmpty(bo);
        if (find == null){
            return true;
        }
        for(int i = 1; i < 10; i++){
            if (checkPos(bo,i, find)){
                bo[find[0]][find[1]] = i;
                if(solveSudoku(bo)){
                    return true;
                }
                bo[find[0]][find[1]] = 0; // return it to zero and try a different number
            }
        }
        return false;
    }

}

public class Main {

    public static void main(String[] args) {
        Sudoku test = new Sudoku();
        int[][] board = {
                {9,3,4,0,0,0,6,0,0},
                {2,0,0,0,6,0,0,9,4},
                {0,0,0,4,2,0,5,0,0},
                {0,7,3,2,0,5,4,0,0},
                {8,0,0,1,0,0,0,0,0},
                {5,0,2,0,0,8,0,7,0},
                {0,0,1,0,0,6,0,0,0},
                {6,0,0,7,5,2,1,0,0},
                {0,0,7,0,1,0,0,0,0}
        };
        test.printBoard(board);
        System.out.println("<><><><><><><><><><><><><><><><><><><><><>");
        test.solveSudoku(board);
        test.printBoard(board);
        System.out.println("<><><><><><><><><><><><><><><><><><><><><>");
    }
}
