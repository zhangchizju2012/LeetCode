//
//  midterm.c
//  lab5
//
//  Created by ZHANG CHI on 2017/10/23.
//  Copyright © 2017年 ZHANG CHI. All rights reserved.
//

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int  main(){
    int a,b,i,j;
    printf("Enter two integer:");
    scanf("%d%d",&a,&b);
    srand((unsigned) time(NULL));
    
    while(a+b>0){
        i=rand()%(a+b);
        int temp = a+b-1;
        j=rand()%temp;
        printf("%d",i);
        printf("%d",j);
        if(i<a){
            j++;
        }
        if(i<a && j<a){
            a-=2;
            b+=1;
        }
        else{
            b-=1;
        }
    }
    printf("%d%d",a,b);
}
