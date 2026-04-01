#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int main(){
	char key[] = "SECRET_BANK_TOKEN_888";
	int len, balance=500, quantity;
	cout << "Enter the length of your name: ";
	cin >> len;
	char name[len];
	string books[5] = {"The Alchemist by Paulo Coelho",
			 "1984 by George Orwell",
			 "The Hobbit by J.R.R. Tolkien",
			 "Harry Potter by J.K. Rowling",
			 "Atomic Habits by James Clear"};

	int price[5] = {300,250,400,500,350};
	scanf("%s",name);
	printf("\n----Welcome to the shop ");
	printf(name);
	printf("----\n");

	do{
		char ch;
		cout << "Do you want to buy a book? [y/n] : ";
		cin >> ch;
		if(ch=='n')	break;
		printf("Balance : Rs.%d\n ",balance);
		cout << "Which book would you like to buy?\n";
		for(int i=0; i<5; i++){
			cout << i << books[i] << "-> Rs." << price[i] << endl;
		}
		unsigned int book_choice;
		scanf("%u",&book_choice);
		cout << "How many books would you like to buy?" << endl ;
		cin >> quantity;
		unsigned int total = quantity*price[book_choice];
		printf("Total Cost: %u\n", total);
		if(total<=balance){
			balance -= total;
			cout << "Purchase sucessfull!"<<endl;
		}else{
			cout << "Insufficient Balance!" << endl;
		}
	}while(true);
}
