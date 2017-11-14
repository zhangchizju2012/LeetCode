//
//  main.c
//  test
//
//  Created by ZHANG CHI on 2017/11/10.
//  Copyright © 2017年 ZHANG CHI. All rights reserved.
//

#include <stdio.h>
#include <string.h>

// * 代表地址
// 就像初始化地址时一样 char * a;
void test(char *c){
    printf("%c\n",*c);
    puts(c);
}

int main(int argc, const char * argv[]) {
    // insert code here...
    //printf("Hello, World!\n");
    char c[10] = "123456";
    //char *c = "123456";
    c[2] = '\0';
    test(c);
    
    struct student	{
        char name[10];
        int marks;
        int grade;
    };
    
    struct student s1 = {"chi",1,1};
    puts(s1.name);
    struct student s2 = s1;
    s2.name[3] = '3';
    puts(s2.name);
    char * temp = strcpy(s2.name,"zhang");
    puts(s2.name);
    puts(temp);
    puts(s1.name);

    
    return 0;
}
