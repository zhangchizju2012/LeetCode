//
//  main.c
//  lab8
//
//  Created by ZHANG CHI on 2017/11/9.
//  Copyright © 2017年 ZHANG CHI. All rights reserved.
//

#include <stdio.h>

int main() {
    char ch;
    char a[100];
    int length=0;
    printf("enter a message:");
    ch=getchar();
    while (ch != '\n'){
        if( ch >= 48 && ch <= 57){//数字
            a[length]=ch;
        }else if(ch >= 65 && ch <= 90){//把A-Z转化为a-z进行比较
            ch+=32;
            a[length]=ch;
        }else if(ch >= 97 && ch <= 122){//字母
            a[length]=ch;
        }
        ch=getchar();
        length++;
    }
    int palindrome=1;
    char *index;
    index = a;
    
    for (int i=0;i<length;i++){
        printf("%c",index[i]);
        printf("%c",index[length-1-i]);
        printf("\n");
        if (index[i]!=index[length-1-i]){
            palindrome=0;
            break;
        }else{
        }
    }

//    for (int i=0;i<length;i++){
//        printf("%c",*(index+i));
//        printf("%c",*(index+length-1-i));
//        printf("\n");
//        if (*(index+i)!=*(index+length-1-i)){
//            palindrome=0;
//            break;
//        }else{
//        }
//    }
    if (palindrome==1){
        printf("palindrome\n");
    }
    else{
        printf("No a palindrome\n");
    }
    return 0;
}

//#include <stdio.h>
//
//int main() {
//    char ch;
//    char a[100];
//    int length=0;
//    printf("enter a message:");
//    ch=getchar();
//    while (ch != '\n'){
//        if( ch >= 48 && ch <= 57){//数字
//            a[length]=ch;
//        }else if(ch >= 65 && ch <= 90){//把A-Z转化为a-z进行比较
//            ch+=32;
//            a[length]=ch;
//        }else if(ch >= 97 && ch <= 122){//字母
//            a[length]=ch;
//        }
//        ch=getchar();
//        length++;
//    }
//    int palindrome=1;
//    char *index;
//    index = &a[0];
//
////    for (index = &a[0];index < &a[length];index++){
////        if (*(index) != *(length-1-index)){
////            palindrome=0;
////            break;
////        }else{
////        }
////    }
//    for (int i=0;i<length;i++){
//        printf("%c",*(index+i));
//        printf("%c",*(index+length-1-i));
//        printf("\n");
//        if (*(index+i)!=*(index+length-1-i)){
//            palindrome=0;
//            break;
//        }else{
//        }
//    }
//    if (palindrome==1){
//        printf("palindrome\n");
//    }
//    else{
//        printf("No a palindrome\n");
//    }
//    return 0;
//}

//#include <stdio.h>
//
//int main() {
//    char ch;
//    char a[100];
//    int length=0;
//    printf("enter a message:");
//    ch=getchar();
//    while (ch != '\n'){
//        if( ch >= 48 && ch <= 57){//数字
//            a[length]=ch;
//        }else if(ch >= 65 && ch <= 90){//把A-Z转化为a-z进行比较
//            ch+=32;
//            a[length]=ch;
//        }else if(ch >= 97 && ch <= 122){//字母
//            a[length]=ch;
//        }
//        ch=getchar();
//        length++;
//    }
//    int palindrome=1,index;
//    for (index=0;index<length;index++){
//        if (a[index]!=a[length-1]){
//            length--;
//            palindrome=0;
//            break;
//        }else{
//            length--;
//        }
//        
//    }
//    if (palindrome==1){
//        printf("palindrome\n");
//    }
//    else{
//        printf("No a palindrome\n");
//    }
//    return 0;
//}
