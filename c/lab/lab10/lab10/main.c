//
//  main.c
//  lab10
//
//  Created by ZHANG CHI on 2017/11/30.
//  Copyright © 2017年 ZHANG CHI. All rights reserved.
//

//
//  q5p456.c
//  lab10
//
//  Created by 王明月 on 2017/11/29.
//  Copyright © 2017年 王明月. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WORD_LEN 20
int read_line(char str[], int n);
void quicksort(char**word,int low,int high);
int split(char**word,int low, int high);
int main(){
    
    char *str[WORD_LEN+1];
    int i,n;
    for (i=0; ;i++){
        printf("enter word:");
        str[i] = malloc(sizeof(char)*20);
        if (read_line(str[i], WORD_LEN)==0)
            break;
        
    }
//    for (n=0; n<i;n++){
//        printf("%s ",str[n]);
//        
//    }printf("\n");
    quicksort(str,0,i-1);
    printf("In sorted order:");
    for (n=0; n<i;n++){
        printf("%s ",str[n]);
        
    }printf("\n");
}
int read_line(char str[], int n){
    int ch,i=0;
    while ((ch=getchar()) != '\n'){
        
        if(i<n)
            str[i++]=ch;
    }
    str[i]='\0';
    return i;
}

void quicksort(char**word, int low, int high)
{
    int middle;
    
    if (low >= high) return;
    middle = split(word, low, high);
    quicksort(word, low, middle - 1);
    quicksort(word, middle + 1, high);
}

int split(char**word, int first, int last)
{
    char *part_element = word[first];
    int low = first + 1;
    int high = last;
    
    for (;;) {
        while (low <= high && word[low] <= part_element)
            low++;
        while (low <= high && word[high] >= part_element)
            high--;
        if (low > high)
            break;
        else{
            char *temp_1 = word[low];
            word[low] = word[high];
            word[high] = temp_1;
        }
        
    }
    char *temp_2 = word[first];
    word[first] = word[high];
    word[high] = temp_2;
    return high;
}

//int split(char**word, int low, int high)
//{
//    char *part_element = word[low];
//    
//    for (;;) {
//        while (low < high && part_element<= word[high])
//            high--;
//        if (low >= high) break;
//        word[low++] = word[high];
//        
//        while (low < high && word[low] <= part_element)
//            low++;
//        if (low >= high) break;
//        word[high--] = word[low];
//    }
//    word[high] = part_element;
//    return high;
//}
