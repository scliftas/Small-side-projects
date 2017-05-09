//Basic C# Caesar Cipher, written by Shaun Clift 6 Jan 2017
using System;
using System.Collections.Generic; //Allows for creation of lists

namespace Cipher
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			string Message;
			string Mode;

			Console.WriteLine ("Welcome to this Caesar Cipher encryption program! Do you want to ENCRYPT or DECRYPT?");
			Mode = Console.ReadLine ();
			Console.WriteLine ("Please type your message:");
			Message = Console.ReadLine ();

			if (Mode == ("encrypt")){
				List<string> Characters = new List<string>(); //Create a list that will store the converted characters
				foreach(char c in Message) //foreach loop that converts all Message characters to ASCII and does the following
				{
					int encMessage = ((int)c + 5); //add 5 onto all ASCII values from Message
					char encMessage2 = Convert.ToChar(encMessage); //Convert the values of encMessage to characters
					Characters.Add (Char.ToString(encMessage2)); //Convert characters to strings and add them to a list to be displayed outside of the loop
				}
				string Result = string.Join ("", Characters.ToArray()); //Convert the list to an array and join all array values
				Console.WriteLine ("Your encrypted message is: " + Result); //Display the encrypted message
			}

			if (Mode == ("decrypt")){
				List<string> Characters = new List<string>();
				foreach(char c in Message)
				{
					int encMessage = ((int)c - 5);
					char encMessage2 = Convert.ToChar(encMessage);
					Characters.Add (Char.ToString(encMessage2));
				}
				string Result = string.Join ("", Characters.ToArray());
				Console.WriteLine ("Your decrypted message is: " + Result);
			} //The second if statement decrypts, does exactly the same as the encrypt statement but minuses 5 in the foreach loop instead
		}
	}
}
