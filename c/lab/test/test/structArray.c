//
//  structArray.c
//  test
//
//  Created by ZHANG CHI on 2017/11/14.
//  Copyright © 2017年 ZHANG CHI. All rights reserved.
//

#include <stdio.h>
#include<string.h>
#include<ctype.h>
#define NAME_LEN 15
//
struct student{
    char name[NAME_LEN + 1];
    int marks;
    int grade;
};
// Function declarations
struct student create_student(const char *name, int marks, int grade);
void print_list(struct student list[], int n);
void get_list(struct student list[], int n);
int read_name(char* name, int n);
//
int main(void) {
    struct student cmput201_student[4] = {[0].name[0] = '\0', [0].marks = 0, [0].grade = 0};
    *cmput201_student = create_student("Zack", 82, 3);
    *(cmput201_student+1) = create_student("michael", 60, 2);
    cmput201_student[2] = create_student("jerry", 100, 4);
    cmput201_student[3] = create_student("john", 40, 0);
    print_list(cmput201_student,4);
    get_list(cmput201_student,4);
    print_list(cmput201_student,4);
    return 0;
}
// Function definition
struct student create_student(const char *name, int marks, int grade) {
    struct student s;
    strcpy(s.name, name);
    s.marks = marks;
    s.grade = grade;
    return s;
}
//
void print_list(struct student list[],int n)
{
    printf("\n================================================================");
    printf("\n%-15s%-10s%-10s","Name","Mark","Grade");
    printf("\n================================================================");
    for(int i=0; i<n ; i++)
        printf("\n%-15s%-10d%d",list[i].name,list[i].marks,list[i].grade);
    printf("\n\n");
}
//
void get_list(struct student list[], int n)
{
    for(int i = 0 ; i<n; i++)
    {
        printf("Enter student %d name:",i+1);
        read_name(list[i].name, NAME_LEN);
        printf("Enter the student %d mark:",i+1);
        scanf("%d",&list[i].marks);
        printf("Enter the student %d grade:",i+1);
        scanf("%d",&list[i].grade);
    }
}
//
int read_name(char* name, int n)
{
    int c, i=0;
    while(isspace(c=getchar())) ;
    while(c != '\n')
    {
        if(i<n)
            name[i++] = c;
        
        c=getchar();
    }
    name[i] = '\0';
    return i;
}
