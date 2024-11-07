#include <iostream>
using namespace std;
int check(int n)
{
   if(n%4==0&& n%100!=0||n%400==0)
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
    cout<<"Enter a year to check : ";
    cin>>n;
    if(check(n))
    {
        cout<<"Leap Year";
    }else
    {
        cout<<"Not a leap year";
    }
}
