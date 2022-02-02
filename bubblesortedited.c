#include <stdio.h>
int main()
{
int array[5]={9,7,8,5,6};
int count=5,temp;
while(count){
int irr=0;
for(int i=0;i<count;i++){
if(array[i]>array[i+1]){
temp=array[i];
array[i]=array[i+1];
array[i+1]=temp;
}
irr++;
for(int i=0;i<5;i++){
printf("%d",array[i]);
}
printf("  ");
}
printf("%d\n",irr);
count=count-1;
}

return 0;
}
