#include <stdio.h>
int main()
{
int array[4]={6,4,5,2};
int count=4,temp;
while(count){
for(int i=0;i<4;i++){
if(array[i]>array[i+1]){
temp=array[i];
array[i]=array[i+1];
array[i+1]=temp;
}
}
count=count-1;
}
for(int i=0;i<4;i++){
printf("%d",array[i]);
}
return 0;
}
