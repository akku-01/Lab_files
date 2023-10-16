#include <iostream>
#include <stack>
using namespace std;

int priority (char ch){
    if(ch == '+' || ch =='-')
        return 1;
 
    if(ch == '*' || ch =='/')
        return 2;
 
    return 0;
}
void convert(string infix)
{
    int i = 0;
    string postfix = "";
    stack <int>s;

    while(infix[i]!='\0')
    {
        if(infix[i]>='a' && infix[i]<='z'|| infix[i]>='A'&& infix[i]<='Z')          
        {
            postfix += infix[i];
            i++;
        }
        else if(infix[i]=='(')
        {
            s.push(infix[i]);
            i++;
        }
        else if(infix[i]==')')
        {
            while(s.top()!='('){
                postfix += s.top();
                s.pop();
            }
            s.pop();
            i++;
        }
        else            
        {
            while (!s.empty() && priority(infix[i]) <= priority(s.top())){
                postfix += s.top();
                s.pop();
            }
            s.push(infix[i]);
            i++;
        }
    }
    while(!s.empty()){
        postfix += s.top();
        s.pop();
    }


    cout << "Postfix is : " << postfix;
}

int main()
{
    string infix = "((a+(b*c))-d)"; 
    //string postfix;
    convert(infix);
    
    return 0;
}