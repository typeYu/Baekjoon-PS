import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

	Scanner scanner = new Scanner(System.in);
	
	int ab = scanner.nextInt();//ab의 길이
	int bc = scanner.nextInt();
	int cd = scanner.nextInt();
	
	double da = ab*bc/cd;

	System.out.println(String.format("%.6f", da));
	
	}
	
}