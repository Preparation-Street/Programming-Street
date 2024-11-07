#include <iostream>
using namespace std;
int check(int n)
{
    if(n%2==0)
    {
        return true;
    }else
    {
        return false;
    }
}
int main()
{
    int n;
    cout<<"Enter a number to check";
    cin>>n;
    if(!check(n))
    {
        cout<<"odd";
    }else
    {
        cout<<"even";
    }
}
