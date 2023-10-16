#include <bits/stdc++.h>
using namespace std;

bool solve(string s){
    int size = s.size();
    if(s[size-1]=='1'){
        cout<<false;
    }
    int count =0;
    for(auto i:s){
        if(i=='1'){
            count ++;
        }
    }
    if(count == 1){
        cout<<true;
    }
    cout<<false;
}
int main()
{
    // Yaha se likho
    string s = "000000010";
    cout<<solve(s);
}