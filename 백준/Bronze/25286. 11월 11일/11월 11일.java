import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (b == 1) {
                System.out.println((a - 1) + " " + 12 + " " + 31);
            }
            else if (b == 2 || b == 4 || b == 6 || b == 8 || b == 9 || b == 11) {
                System.out.println(a + " " + (b - 1) + " " + 31);
            }
            else if (b == 3) {
                if ((a % 100 != 0 && a % 4 == 0) || a % 400 == 0) {
                    System.out.println(a + " " + 2 + " " + 29);
                }
                else {
                    System.out.println(a + " " + 2 + " " + 28);
                }
            }
            else {
                System.out.println(a + " " + (b - 1) + " " + 30);
            }
        }
    }
}