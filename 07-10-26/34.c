 #include <stdio.h>
void foo(int *p, int x){
 *p=x;
}
int main(){
 int *z;
 int a = 20, b = 25;
 z = &a;
 foo(z,b);
 printf("%d",a);
 return 0;
}
