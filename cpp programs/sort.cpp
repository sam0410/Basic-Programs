#include<iostream>
#include<fstream>
#include<queue>
using namespace std;

int main()
{
ofstream out;
ifstream in;

out.open("output.txt");
in.open("input.txt");

int temp,n=0;
priority_queue<int, vector<int>, greater <int> >h;
while(in>>temp)
{
n++;
h.push(temp);
}
cout<<n;
for(int i=0;i<n;i++)
{
temp=h.top();
h.pop();	
out<<temp<<endl;
}

}
