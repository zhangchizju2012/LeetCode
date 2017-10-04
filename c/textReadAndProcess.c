//
//  main.c
//  assignment1
//
//  Created by ZHANG CHI on 2017/10/3.
//  Copyright © 2017年 ZHANG CHI. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
int main(int argc, char *argv[]) {
    FILE *fp;

    int max_x, max_y, num_pt;
    int *x_coordinate, *y_coordinate;
    int inputfile = 0, outputfile = 0;
    int i;
    if (argc == 1) {
        /* to generate random instances, accepting parameters from stdin */
        return 1;
    }
    for (i = 1; i < argc; i++) {
        if (strcmp (argv[i], "-i") == 0)
            inputfile = i+1;
        else if (strcmp (argv[i], "-o") == 0)
            outputfile = i+1;
    }
    if (inputfile == 0) {
        /* invalid command line options */
        return -1; }
    if ((fp = fopen(argv[inputfile], "r")) == NULL) {
        /* open file error */
        return -2;
    }
    while (fscanf(fp, "%d", &max_x) != 1) {
        if (ferror(fp)) {
            /* read error */
            fclose(fp);
            return -3; }
        if (feof(fp)) {
            /* no integer to read */
            fclose(fp);
            return -4;
        }
        fscanf(fp, "%*[^\n]"); /* skip the rest of line */
    }
    if (fscanf(fp, "%d", &max_y) != 1) {
        /* max_y not following max_x */
        fclose(fp);
        return -5;
    }
    while (fscanf(fp, "%d", &num_pt) != 1) {
        if (ferror(fp)) {
            /* read error */
            fclose(fp);
            return -6; }
        if (feof(fp)) {
            /* no integer to read */
            fclose(fp);
            return -7;
        }
        fscanf(fp, "%*[^\n]"); /* skip the rest of line */
    }
    x_coordinate = (int *)malloc(num_pt * sizeof(int));
    y_coordinate = (int *)malloc(num_pt * sizeof(int));
    for (i = 0; i < num_pt; i++) {
        while (fscanf(fp, "%d", &x_coordinate[i]) != 1) {
            if (ferror(fp)) {
                /* read error */
                fclose(fp);
                return -8; }
            if (feof(fp)) {
                /* no integer to read */
                fclose(fp);
                return -9;
            }
            fscanf(fp, "%*[^\n]"); /* skip the rest of line */
        }
        if (fscanf(fp, "%d", &y_coordinate[i]) != 1) {
            /* y_coordinate not following x_coordinate */
            fclose(fp);
            return -10;
        } }
    fclose(fp);
    if (outputfile > 0) {
        if ((fp = fopen(argv[outputfile], "w")) == NULL) {
            /* open file error */
            return -2; }
    }
    else {
        fp = stdout; }
    fprintf(fp, "##################################################\n");
    fprintf(fp, "#%s\n", argv[inputfile]);
    fprintf(fp, "#area [0, MAX_X] x [0, MAX_Y]\n");
    fprintf(fp, "%d\t%d\n", max_x, max_y);
    fprintf(fp, "#number of points NUM_PT\n");
    fprintf(fp, "%d\n", num_pt);
    fprintf(fp, "#coordinates\n");
    for (i = 0; i < num_pt; i++) {
        fprintf(fp, "%d\t%d\n", x_coordinate[i], y_coordinate[i]);
    }
    fprintf(fp, "#end of instance\n");
    if (fp != stdout) {
        fclose(fp);
    }
    free(x_coordinate);
    free(y_coordinate);
    return 0;
}
