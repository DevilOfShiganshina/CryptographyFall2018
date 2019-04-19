#include <iostream>
using namespace std; 

void LetterCounter(string str, int arr[], int stringSize, int arraySize)
{
	char c = 'A';

	for (int i = 0; i < arraySize; i++)
	{
		for (int j = 0; j < stringSize; j++)
		{
			if (str[j] == c)
			{
				arr[i]++;
			}
		}

		c++;
	}
}

void Replace(string &str, char find, char replace)
{
	int size = str.size();

	for(int i = 0; i < size; i++)
	{
		if (str[i] == find)
		{
			str[i] = replace;
		}
	}
}

void LetterOccurance(int arr[], int size)
{
	char c = 'A';
	for (int i = 0; i < 26; i++)
	{
		if (arr[i] == 0)
		{
			c++;
			continue;
		}

		else
		{
			cout << c << "\t" << arr[i] << endl;
		}
		c++;
	}
}

int main()
{
	string str = "WBYAYAGHQTWBJNJUYHHYHUGVWBJPJKRGHYHUWBYAYAGHQTWBJVYPAWAYIWBJVYPAWVGPJWFAWJGVFNYWWJPKEICBYKBCYQQNJIPGVVJPJLWGEATJFPNTTJFPEHQJAA,NTFAEIPJDJPJKGOJPTGVDGPFQBJFQWBFHLDFPWYFQOYUGP,CJFPYAJFUFYHFHLWFRJGEPAWFHLVGPVPJJLGDFAYHWBJGQLJHWYDJ";

	int arr[26] = {0};

	int arrSize = sizeof(arr)/sizeof(*arr);

	int size = str.size();

	LetterCounter(str, arr, size, arrSize);

	LetterOccurance(arr, arrSize);

	cout << endl << "Ciphertext" << endl << str << endl;

	// Since J appears 28 times within the ciphertext, we can most
	// likely be sure that 'J' is actually the letter 'E'.
	// So we replace every J with E in the cipher text.

	Replace(str, 'J', 'E');

	// Next largest letter occurance is 19, but uh-oh, there are 3 letters,
	// and each of them occurs 19 times in the cipher text. This is where I
	// made an educated guess. I looked at the cipher text and realized that
	// YAYA occurs at the beginning after WB. So I figured the first two words
	// would have to be "This is", so I replaced every occurance of 'W' with 'T'
	// and every occurance of 'B' with 'H', every 'Y' with 'I', and every 'A' with
	// 'S'.

	Replace(str, 'Y', 'I');
	Replace(str, 'T', 'Y');
	Replace(str, 'W', 'T');
	Replace(str, 'N', 'X');
	Replace(str, 'H', 'N');
	Replace(str, 'B', 'H');
	Replace(str, 'X', 'B');
	Replace(str, 'A', 'S');

	// After changing "WBYAYA" to "THISIS", I noticed that "THE" occurs after 4 cipher
	// letters after "THISIS". So I again made an educated guess and replaced "GHQT" with
	// "ONLY". But there's a problem. I noticed that if I replaced T with Y, then the
	// plaintext would not make any sense. So before replacing W with T, I replaced T with
	// Y, and right before that, replaced Y with I.

	// Changing G = O
	//     "    H = N // Before changing 'B' to 'H'
	//     "    Q = L

	Replace(str, 'G', 'O');
	Replace(str, 'Q', 'L');

	// After the decrypting the first couple of words, I noticed the next few letters of the
	// cipher text, especially "NEUINNINU". By the context clues and the similarities of the
	// cipher letters "NEUINNINU", I again make an educated guess and decide to change it to
	// the word "BEGINNING". I go back and correctly replace the letters. Then I proceed to
	// replace all the occurances of 'U' with 'G'.

	Replace(str, 'U', 'G');

	// After replacing the occurances of U with G, I notice the next two cipher letter "OV"
	// and right after it the word "THE", so again by the context clues I make an educated
	// guess and replace 'V' with 'F', so the plaintext so far would read "This is only the
	// beginning of the".

	Replace(str, 'V', 'F');

	// I was stumped after decrypting the cipher up until "This is only the beginning of the".
	// So I looked further into the ciphertext. I noticed after "PEKRONING" that the plaintext
	// read "THISISONLYTHEFIPST", therefore I replaced 'P' with R, so "FIPST" becomes "FIRST".

	Replace(str, 'K', 'C');
	Replace(str, 'R', 'K');
	Replace(str, 'P', 'R');

	// After changing 'P' to 'R', by the context clues I noticed "REKRONING" could possibly be
	// "RECKONING". So before replacing 'P' to 'R', I replaced 'K' with 'C' and 'R' with 'K'.

	// At this point I realized that this cipher is a quote by Winston Churchill. So the
	// plaintext of this ciphertext is:

	// "This is only the beginning of the reckoning. This is only the first sip, the first
	// foretaste of a bitter cup which will be proffered to us year by year unless by a
	// supreme recovery of moral health and martial vigour, we arise again and take our
	// stand for freedom as in olden time."

	cout << endl << "Plaintext" << endl << str << endl;
	return 0;
}