#include <iostream>
using namespace std;
int check(int n)
{
    int digit,sum =0;
    while(n!=0)
    {
        digit = n% 10;
        sum = sum + digit*digit*digit;
        n= n/10;
        
    }
    cout<<sum<<endl;
    return sum;
}
int main()
{
    int n;
    cout<<"Enter a number : ";
    cin>>n;
    int result = check(n);
    cout<<n<<endl;
    if(result == n)
    {
        cout<<"It's an armstrong number";
    }else
    {cout<<"It's not an armstrong number";}
    return 0;
}