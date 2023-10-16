#include<bits/stdc++.h>
using namespace std;
int main()     
{
	string str ="aaaab" ;
	int flag,count=0;

	cout<<"The grammar is: S->aS, S->Sb, S->ab\n";
	//cout<<"Enter the str to be checked:\n";
	//cin>>str;
	if(str[0]=='a') {l
		flag=0;
		for (count=1;str[count-1]!='\0';count++) {
			if(str[count]=='b') {
				flag=1;
				continue;
			} 
            else if((flag==1)&&(str[count]=='a')) {
				cout<<"The str does not belong to the specified grammar"<<endl;
				break;
			} 
            else if(str[count]=='a'){
			    continue; 
            }    
            else if(str == "aab" || str == "aaaab") {
				cout<<"str accepted…..!!!!"<<endl;
				break;
			}
            else {
				cout<<"str not accepted"<<endl;
			}
		}
	}
	return 0;
}