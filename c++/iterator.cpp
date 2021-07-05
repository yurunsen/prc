//gitt
#include<iostream>
//make
using namespace std;
int main()
{
    int a[3][4] ={{1,2},{3},{5,6}};
    for(auto p=begin(a);p!=end(a);++p)
    {
        for(auto q=begin(*p);q!=end(*p);q++)
            cout<<*q<<" ";
        cout<<endl;
    }
    cin.get();
}