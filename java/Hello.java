import java.util.Scanner;

public class Hello{


	public static void main(String []args){

		Scanner keyboard = new Scanner(System.in);
		System.out.print("Enter something: ");

		String s = keyboard.nextLine();
		System.out.println(s);
		System.out.println("End of program.");
	}

}