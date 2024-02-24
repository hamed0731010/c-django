#include <stdio.h>
/* this is a Hello World script in C */
long long claculate(int limit){
     long long total = 0;
     for(int i = 1 ;i<= limit ;++i){
        total += i;
     }
     return total;
}
int main(void)
{
    int limit = 100000000;
    
    long long result = claculate(limit);
  printf("sum %lld",result);
  return 0;
}