package strings;

import java.util.Scanner;

public class palindrome {
	public static void main(String[] args) {
		String word = "";
		Scanner sc = new Scanner(System.in);

		System.out.println("Type Y to exit");
		
		while (!word.equalsIgnoreCase("Y")) {
			System.out.println("Enter the word:");
			word = sc.nextLine();
			System.out.println("Word entered: " + word);
			
			if (word.length() > 1) {
				if (word.equals(reverse(word)))
					System.out.println("It's a palindrome !");
				else
					System.out.println("It isn't a palindrome !");
			}

			System.out.println("");
		}
		
		sc.close();
		System.out.println("End program !");
	}
	
	public static String reverse(String text) {
		String wordReverse = "";
		
		for (int i = text.length() - 1; i >= 0; i--) {
			wordReverse = wordReverse + text.charAt(i);
		}
		
		return wordReverse;
	}
}
