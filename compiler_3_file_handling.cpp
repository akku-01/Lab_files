#include<iostream>
#include<fstream>
#include<string.h>
#include<cstdlib>
using namespace std;
int main()
{
     int noc=0,now=0,nol=0;
     FILE *fr;
     char fname[20],ch;

     cout<<"\n Enter Source File Name : ";
     gets(fname);
     fr=fopen(fname,"r");
     if(fr==NULL)
     {
          cout<<"\n Invalid File Name. \n No such File or Directory ";
          exit(0);
     }
     ch=fgetc(fr);
     while(ch!=EOF)
     {
          if(ch!=' ' && ch!='\n')
               noc++;
          if(ch==' ')
               now++;
          if(ch=='\n')
          {
               nol++;
               now++;
          }
          ch=fgetc(fr);
     }
     fclose(fr);
     cout<<endl;
     cout<<"Total No. of Characters  : "<<noc<<endl;
     cout<<"Total No. of Words       : "<<now<<endl;
     cout<<"Total No. of Lines       : "<<nol<<endl;

     return 0;
}