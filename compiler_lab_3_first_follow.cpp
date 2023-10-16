#include <bits/stdc++.h>
using namespace std;

struct production
{
            char l;
            char r[10];
            int rear;
};
struct production prod[20],pr_new[20];        

int p=0,b=0,d,f,q,n,flag=0;
char terminal[20],nonterm[20],alpha[10];
char x,epsilon='^';

int main()
{
    // Yaha se likho
    cout<<"Enter the value of all productions"<<endl;
    cout<<"Enter the number of terminals: ";
    cin>>d;
    cout<<"Enter the terminal symbols for your production: ";
    int k=0;
    for(k=0;k<d;k++)
    {
      cin>>terminal[k];
    }

  
    cout<<"\nEnter the number of non-terminals: ";
    cin>>f;
    cout<<"Enter the non-terminal symbols for your production: ";
    for(k=0;k<f;k++)
    {
      cin>>nonterm[k];
    }

 
    cout<<"\nEnter the number of Special characters(except non-terminals): ";
    cin>>q;
    cout<<"Enter the special characters for your production: ";
    for(k=0;k<q;k++)
    {
      cin>>alpha[k];
    }

  
    cout<<"\nEnter the number of productions: ";
    cin>>n;
    for(k=0;k<=n-1;k++)
    {
      cout<<"Enter the "<< k+1<<" production: ";
      cin>>prod[k].l;
      cout<<"->";
      cin>>prod[k].r;
      prod[k].rear=strlen(prod[k].r);
    }
    return 0;
}
