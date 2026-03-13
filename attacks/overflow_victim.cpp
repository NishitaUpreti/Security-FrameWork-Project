#include<iostream>
using namespace std;

void secretAccess(){
cout <<  "!!!BUFFER OVERFLOW!!!" << endl;
}

void username(){
char bufferArr[10];
int n = sizeof(bufferArr)/sizeof(char);
cout <<  "Enter username:" << endl;
cin >> bufferArr;
cout << "Welcome" << bufferArr << "!" << endl;
}

int main(){
username();
return 0;
}
