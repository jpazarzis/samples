#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


template <int N> class Matrix{
        int _element [N] [N];       
    public:
    
};

int symetrikos(int **, int);
int anwtrigwnikos(int **, int);
int katwtrigwnikos(int **, int);
int araios(int **, int);
int**dimiourgeiapinaka(int);


int main()
{

        int **a;
        int **b;
        int n;
        printf("Dwse tis diastaseis tou pinaka");
        scanf("%d",&n);

        printf("dwse n*n stoixeia gia na gemisei o pinakas %d",**dimiourgeiapinaka(int));


         if ( anwtrigwnikos(a,n) == 1){
            printf("O pinakas einai anw trigwnikos\n");
         }
         else {
            printf("O pinakas den einai anw trigwnikos\n");
         }

         if ( katwtrigwnikos(a,n) == 1){
            printf("O pinakas einai katw trigwnikos\n");
         }
         else{
            printf("O pinakas den einai katw trigwnikos\n");
         }

         if ( symetrikos(a,n) == 1){
            printf("O pinakas einai symetrikos\n");
         }
         else{
            printf("O pinakas den einai symetrikos\n");}

            if ( araios(a,n) == 1){
            printf("O pinakas einai araios\n");}
            else{
            printf("O pinakas den einai araios\n");
        }
        return 0;
}

int anwtrigwnikos(int **b, int n)
{
    int i,j;
    for (i = 1;i < n;i++){
        for (j = 0;j < i;j++){
            if ( (*(*(b+i) + j) ) != 0){
                 return 0;
            }

        }
    }
return 1;
}
int katwtrigwnikos(int **b, int n)
{
    int i,j;
    for (j = 1;j < n;j++){
        for (i = 0;i < j;i++){
            if ( (*(*(b+i) + j) ) != 0){
                return 0;
            }
        }
    }
return 1;
}
int symetrikos(int **b, int n)
{
    int i,j;
    for (i=0;i<n;i++){
        for (j=0;j<n;j++){
            if ( (*(*(b+i) + j) ) != (*(*(b+j) + i) )){
            return 0;}
            }
    }
return 1;
}
int araios(int **b, int n)
{
    int i,j,count=0;
    for (i=0;i<n;i++){
     for (j=0;j<n;j++){
      if ( (*(*(b+i) + j) ) == 0){
       count++;
            }
        }
    }
    if (count >= n*n*80/100){
              return 1;
    }
    else{
         return 0;
        }
}
int ** dimiourgeiapinaka(int n)
{
        int i, j, number1,number2;
        int **B;

        B=(int **)malloc(n*sizeof(int *));

        for(i=0; i<n; i++){
                B[i]=(int *)malloc(n*sizeof(int));
        }


         for(i=0; i<n; i++){
                printf("dwse mou enan arithmo");
                scanf("%d",&number1);
                B[i][j]=number1;
            for(j=0; j<n; j++){
                printf("dwse mou enan arithmo");
                scanf("%d", &number2);
                B[i][j]=number2;
             }
             return B;
        }
}
