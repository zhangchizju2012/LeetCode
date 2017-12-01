//
//  main.c
//  lab7
//
//  Created by 王明月 on 2017/10/29.
//  Copyright © 2017年 王明月. All rights reserved.
//

#include <stdio.h>
int check(int puzzle[9][9], int row,int col,int number);
int solvesudoku(int puzzle[9][9], int n);

int main(void) {
    int row,col;
    int puzzle[9][9]={
        0, 0, 2, 0, 0, 0, 5, 0, 0,
        0, 1, 0, 7, 0, 5, 0, 2, 0,
        4, 0, 0, 0, 9, 0, 0, 0, 7,
        0 ,4 ,9 ,0 ,0 ,0 ,7 ,3 ,0,
        8 ,0, 1, 0, 3, 0, 4, 0, 9,
        0, 3, 6, 0, 0, 0, 2, 1, 0,
        2, 0, 0, 0, 8, 0, 0, 0, 4,
        0, 8, 0, 9 ,0 ,2, 0, 6, 0,
        0, 0, 7, 0, 0, 0, 8, 0, 0
    };
//    int puzzle[9][9]={
//        0, 0, 0, 0, 0, 0, 0, 0, 0,
//        0, 7, 9, 0, 5, 0, 1, 8, 0,
//        8, 0, 0, 0, 0, 0, 0, 0, 7,
//        0, 0, 7, 3, 0, 6, 8, 0, 0,
//        4, 5, 0, 7, 0, 8, 0, 9, 6,
//        0, 0, 3, 5, 0, 2 ,7 ,0, 0,
//        7, 0, 0, 0, 0, 0, 0, 0, 5,
//        0, 1, 6, 0, 3, 0, 4, 2, 0,
//        0, 0, 0, 0, 0, 0, 0, 0, 0
//    };
//    int puzzle[9][9]={
//        0,0,0,0,0,3,0,1,7,
//        0,1,5,0,0,9,0,0,8,
//        0,6,0,0,0,0,0,0,0,
//        1,0,0,0,0,7,0,0,0,
//        0,0,9,0,0,0,2,0,0,
//        0,0,0,5,0,0,0,0,4,
//        0,0,0,0,0,0,0,2,0,
//        5,0,0,6,0,0,3,4,0,
//        3,4,0,2,0,0,0,0,0
//    };
//    int puzzle[9][9]={
//        7,0,3,1,0,8,4,5,9,
//        9,0,0,0,6,0,8,0,0,
//        0,0,0,0,0,0,0,0,0,
//        0,1,0,2,9,0,3,6,7,
//        0,7,5,0,0,3,0,0,8,
//        0,0,0,7,0,1,0,0,0,
//        0,0,2,0,7,0,0,1,5,
//        0,8,6,3,5,0,0,2,0,
//        0,0,0,0,1,0,0,0,0};
//    int puzzle[9][9]={
//        0,0,0,0,6,0,0,0,5,
//        6,2,4,0,0,0,0,1,0,
//        0,0,1,0,0,0,3,0,0,
//        0,0,8,0,0,4,0,3,7,
//        0,0,9,1,0,0,5,0,0,
//        0,0,7,5,0,0,0,9,0,
//        0,8,2,4,7,0,0,0,0,
//        0,9,0,3,1,0,0,0,0,
//        0,0,0,0,2,9,0,5,3
//    };
    
    solvesudoku(puzzle,0);
    
    for (row=0;row<9;row++){
        for (col=0;col<9; col++){
            printf("%2d",puzzle[row][col]);
        }
        printf("\n");
    }
    return 0;
}
//检查有没有这个数字，如果有return 0，
int check(int puzzle[9][9], int row,int col,int number){
    int x,y;
    int m,n;
    int t1=(row/3)*3,t2=(col/3)*3;
    //检查col
    for (m=0;m<9;m++){
        if (puzzle[row][m]==number){
            return 0;}
    }
    //检查row
    for (n=0;n<9;n++){
        if (puzzle[n][col]==number){
            return 0;}
    }
    //检查3*3
    for(x=t1;x<t1+3;x++){
        for(y=t2;y<t2+3;y++){
            if(puzzle[x][y] == number){
                return 0 ;}
        }
        
    }
    return 1;
}
int solvesudoku(int puzzle[9][9], int n) {
    int a[9][9];
    int row;
    int col;
    int number;
    row = n / 9;
    col = n % 9;

    if (puzzle[row][col] != 0){
        if (n==80){
            return 1;
        }
        else{
            return solvesudoku(puzzle,n+1);
        }
    }
    else{
        for (number=1;number<=9;number++){
            int find=check(puzzle,row,col,number);
            if (find==1){
                //复制这个数组 用于之后的检查是否成功
                for(int m = 0;m<9;m++){
                    for(int n=0;n<9;n++){
                        a[m][n] = puzzle[m][n];
                    }
                }
                puzzle[row][col]=number;
                if (n==80){
                    return 1;
                }
                else{
                    if(solvesudoku(puzzle,n+1)==1){
                        return 1;
                    }else{
                        //不成功的话还原回来
                        for(int m = 0;m<9;m++){
                            for(int n=0;n<9;n++){
                                puzzle[m][n] = a[m][n];
                            }
                        }
                    }
                }
            }
        }
        return 0;
    }
}
