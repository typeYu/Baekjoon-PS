import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			
			String input = br.readLine();
			
			if(input.contentEquals("#")) {
				System.exit(0);	
			}
			
			char c;
			int v = 1;
			for(int i = 0; i<input.length();i++) {
				c = input.charAt(i);
				if(c!='i' &&c!='o' &&c!='v' &&c!='w' &&c!='x' &&c!='b' &&c!='d' &&c!='p' &&c!='q')
					v = 0;
			}
			for(int i = input.length()-1; i>=0; i--) {
				if(v==0) {System.out.print("INVALID"); break;}
				c = input.charAt(i);
				if(c == 'b') System.out.print("d");
				else if(c == 'd') System.out.print("b");
				else if(c == 'p') System.out.print("q");
				else if(c == 'q') System.out.print("p");
				else System.out.print(c);
			}
			System.out.println();
		}
	}
}