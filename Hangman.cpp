//	Computer Project
// 11th standard
// Hangman
#include<iostream>
#include<cstdlib>
#include<ctime>
#include<string>
#define clrscr() system("CLS")
using namespace std;

char a[100][100];
const int MAX_TRIES = 5;
int i,j;
int letterFill(char, string, string&);
int main()
{
	string name;
	char letter;
	int num_of_wrong_guesses=0;
	string word;
	//25 countries declariation.
	string words[]=
	{
		"america","austria",
		"peru","alaska",
		"ukeaine","japan",
		"argentina","brazil",
		"india",
		"nepal","malaysia",
		"philippines","pakistan",
		"australia","iran",
		"ethopia","oman",
		"mexico","china",
		"russia","algeria",
		"egypt","germany",
		"madagascar",
		"indonesia",
	};
	//choose and copy a word from array of words randomly.
	srand (time(NULL));
	int n=rand()%25;
	word=words[n];
	//intialize the secret word with the * character.
	string unknown(word.length(),'*');
	//Initiialising the hang 
	{
		for(i=1;i<=6;i++)
		{
			for(j=0;j<=7;j++)
			{
				a[i][j]=' ';
        	}
        } 
        a[0][0]=a[0][1]=a[0][9]=' ';
        for(i=1;i<=5;i++)
        	a[i][8]=' ';
        for(i=0;i<=5;i++)
        	a[i][10]=' ';
		for(i=2;i<=8;i++)
        	a[0][i]='_';
		for(i=1;i<=6;i++)
        	a[i][9]='|';
        a[6][8]=a[6][10]='_';
    }
    //	bell to start the game
    cout<<"\a\a";
    //	Loop until the guesses are used up
    while(num_of_wrong_guesses < MAX_TRIES)
    {
    	//	Welcome the user and tell the user how many guesses are there
    	
    	cout<<"\t\t\t\t\"HANGMAN\"";
    	cout<<"\n\nWelcome to Hangman...Guess a country name";
    	cout<<"\n\n*Each letter is represented by a star \' * \'";
    	cout<<"\n\n*You have to type only one letter in one try";
		cout<<"\n\n*You will hear a beep for every wrong entry";
		cout<<"\n____________________________________________________________________________________________________";
		cout<<"\n\n-->You have "<<" "<<MAX_TRIES-num_of_wrong_guesses;
		if(MAX_TRIES - num_of_wrong_guesses == 1)
			cout<<"try";
		else
			cout<<"tries";
		cout<<" "<<"to guess the word and save yourself from getting HANGED";
		
		//	loop for hanging the man step by step
		for(i=0;i<=6;i++)
		{
			cout<<endl<<"\t";
			for(j=0;j<=10;j++)
			{
				cout<<a[i][j];
			}
		}
		cout<<"\n\n"<<unknown;
		cout<<"\n\nGuess a letter: ";
		cin>>letter;
		
		//to convert input to lower case letters
		letter=tolower(letter);
		
		//	Fill secret word with letter if the guess is correct
		//	otherwise increment the number of wrong guesses
		
		if(letterFill(letter, word, unknown)==0)
		{
			num_of_wrong_guesses++;
			//	bell for each wrong letter
			cout<<"\a";
			{
				//	condition to undertake the hanging step by step
				if(num_of_wrong_guesses==1)
					a[2][1]='O';
				else if(num_of_wrong_guesses==2)
					for(i=3;i<=5;i++)
						a[i][1]='|';
				else if(num_of_wrong_guesses==3)
				{
					a[3][0]=char(47);
					a[3][2]=char(92);
				}
				else if(num_of_wrong_guesses==4)
				{
					a[5][0]=char(47);
					a[5][2]=char(92);
				}
				else if(num_of_wrong_guesses==5)
					a[1][1]='|';
			}
		}
		// Check if user guessed the word
		if(word == unknown)
		{
			//	to clear screen
			clrscr();
			cout<<word<<endl<<endl;
			cout<<"\t\a\aYeah! You got it! You are safe\n\n\t\" Congradulations\""<<endl<<endl;
			cout<<"    		"<<char(2)<<"\n";
			cout<<"   	       \\|/\n";
			cout<<"    	       /|\\\n";
			cout<<endl<<"\tThankyou for playing...";
			break;
		}
		//to clear screen
		clrscr();
	}
	if(num_of_wrong_guesses == MAX_TRIES)
	{
		//loop for final hanging of the man.
		for(i=0;i<=6;i++)
		{
			cout<<endl<<"\t";
			for(j=0;j<=10;j++)
				cout<<a[i][j];
		}
	}
	cout<<"\a\a\n\nSorry, you lose... you've been hanged."<<endl;
	cout<<"The word was: "<<word<<endl<<"\t Thankyou for playing...";
	cin.ignore();
	cin.get();
	return 0;
}

int letterFill(char guess, string secretword,string &guessword)
{
	int i,matches=0,len = secretword.length();
	for(i=0;i<len;i++)
	{
		// did we already match this letter in the previous guess ?
		if(guess == guessword[i])
			return 0;
		// Is the guess in the secret word ?
		if(guess == secretword[i])
		{
			guessword[i]=guess;
			matches++;
		}
	}
	return matches;
}
//	END OF PROJECT
