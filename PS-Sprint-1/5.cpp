#include <iostream>
using namespace std;
void series(int n)
{
    int t1=0,t2=1,prev=0,current=0;

    for(int i=1;i<=n;i++)
    {
        if(i==1)
        {
            cout<<t1<<" ";
        }
        if(i==2)
        {
            cout<<t2<<" ";
        }
        current = t1 +t2;
        t1=t2;
        t2 =current;
        
        cout<<current<<" ";
    }
    
    
}
int main()
{
    int n;
    cout<<"Enter limit";
    cin>>n;
    series(n);
    return 0;
}