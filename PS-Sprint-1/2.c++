#include <iostream>
using namespace std;
int check(int n)
{
    int count=0;
    for(int i=2;i<=n/2;i++)
    {
        if(n%i==0)
        {
            count++;
        }
        
    }
    if(count>0)
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
    cout<<"Enter a number to check : ";
    cin>>n;
    if(check(n))
    {
        cout<<"non-prime";
    }else
    {
        cout<<"prime";
    }
}
