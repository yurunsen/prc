#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
    vector<int> v1{1,2,3,4};
    auto beg=v1.begin(),e=v1.end();
    for(auto &c : v1)
        c*=c;
    for(auto &c : v1)
    cout<<c<<" ";  
    
    cin.get();
   
    return 0; 
}
// int i=0;
    // string s;
    // //decltype(s.size()) index=0;
    // getline(cin,s);
    // for(auto &c:s)   
    //     c ='x';
    // // cin>>s;
    // // cout<<s<<i<<endl;
    // // while(getline(cin,s))
    // // if(s.size()>5)
    // cout<<s<<endl; //system("pause");