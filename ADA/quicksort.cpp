#include <bits/stdc++.h>
using namespace std;

void swap(int *i,int* j){
    int temp = *i;
    *i=*j;
    *j=temp;
}
void quick_sort(int arr[],int n,int pivot,int i,int j){
    if((j-pivot)<=2 || (pivot-i)<=2){
        return ;
    }
    while(i<=(n-1) && arr[pivot]>arr[i]){
        i++;
    }
    while(j>=pivot && arr[pivot]<arr[j]){
        j--;
    }
    if(i<=j){
        swap(&arr[i],&arr[j]);
        quick_sort(arr,n,pivot,i,j);
    }else{
        swap(&arr[pivot],&arr[i]);
        quick_sort(arr,n,i,i+1,pivot);
        quick_sort(arr,n,pivot+1,pivot+2,j);
    }
}
int main()
{
    // Yaha se likho
    int arr[6] = {6,5,3,4,1,2};
    quick_sort(arr,6,0,1,5);
    for(int i:arr){
        cout<<i;
    }
    return 0;
}