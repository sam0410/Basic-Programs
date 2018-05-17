#include<bits/stdc++.h>
using namespace std;


long fast_gcd(long a,long b)
{
	if(a==0)return b;
	if(b==0)return a;
	if(a<0)a=-a;
	if(b<0)b=-b;
	int shift= _builtin_ctz(a|b);
	a= a>>(_builtin_ctz(b));
	do
	{
		b= a>>(_builtin_ctz(b));
		if(a>b)
			{
				long t;
				t=a;
				a=b;
				b=t;
			}
		b=b-a;
	}while(b!=0);

return (a<<shift);

}

int main()
{
long a,b;
cin>>a>>b;
long gcd= fast_gcd(a,b);
cout<<gcd;

}
