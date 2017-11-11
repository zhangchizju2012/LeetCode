//
//  main.c
//  lab5
//
//  Created by ZHANG CHI on 2017/10/18.
//  Copyright © 2017年 ZHANG CHI. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int i = 1;
    int j = 100;
    int k = +(+(+i)+(+j));//(++i)+(++j);//(i++)+(j++);
    printf("%d\n",i);
    printf("%d\n",j);
    printf("%d\n",k);
    return 0;
}

//void pb(int n){
//    if(n != 0){
//        pb(n / 2);
//        putchar('0' + n % 2);
//    }
//}
//
//int main(int argc, const char * argv[]) {
//    pb(17);
//    printf("\n");
//    return 0;
//}

//void create_magic_square(int size, int magic_square[size][size]){
//    int i = 0;
//    int j = (size - 1) / 2;
//    for(int count = 1; count <= size * size; count++){
//        magic_square[i][j] = count;
//        if(count % size != 0){
//            i = i - 1;
//            j = j + 1;
//        }else{
//            i = i + 1;
//        }
//        if(i < 0){
//            i = i + size;
//        }
//        if(i > size - 1){
//            i = i - size;
//        }
//        if(j > size - 1){
//            j = j - size;
//        }
//    }
//}
//
//void print_magic_square(int size, int magic_square[size][size]){
//    for(int i=0;i<size;i++){
//        for(int j=0;j<size;j++){
//            printf("%5d ",magic_square[i][j]);
//        }
//        printf("\n");
//    }
//}
//
//int main(int argc, const char * argv[]) {
//    
//    int size;
//    
//    printf("What the size do you want? ");
//    scanf("%d",&size);
//    
//    int temp[size][size];
//    create_magic_square(size, temp);
//    print_magic_square(size, temp);
//
//    return 0;
//}

//int main(int argc, const char * argv[]) {
//    
//    int size;
//    
//    printf("What the size do you want? ");
//    scanf("%d",&size);
//    
//    int temp[size][size];
//    int i = 0;
//    int j = (size - 1) / 2;
//    for(int count = 1; count <= size * size; count++){
//        temp[i][j] = count;
//        if(count % size != 0){
//            i = i - 1;
//            j = j + 1;
//        }else{
//            i = i + 1;
//        }
//        if(i < 0){
//            i = i + size;
//        }
//        if(i > size - 1){
//            i = i - size;
//        }
//        if(j > size - 1){
//            j = j - size;
//        }
//    }
//    for(int i=0;i<size;i++){
//        for(int j=0;j<size;j++){
//            printf("%5d ",temp[i][j]);
//        }
//        printf("\n");
//    }
//    return 0;
//}

//int main(int argc, const char * argv[]) {
//    // insert code here...
//    // printf("Hello, World!\n");
//    
//    int temp[5][5];
//    int i = 0;
//    int j = 2;
//    for(int count = 1; count <= 25; count++){
//        temp[i][j] = count;
//        if(count % 5 != 0){
//            i = i - 1;
//            j = j + 1;
//        }else{
//            i = i + 1;
//        }
//        if(i < 0){
//            i = i + 5;
//        }
//        if(i > 4){
//            i = i - 5;
//        }
//        if(j > 4){
//            j = j - 5;
//        }
//    }
//    for(int i=0;i<5;i++){
//        for(int j=0;j<5;j++){
//            printf("%d ",temp[i][j]);
//        }
//        printf("\n");
//    }
//    
//    return 0;
//}
