import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            int y = Integer.parseInt(new StringBuilder(String.valueOf(x)).reverse().toString());

            String z = String.valueOf(x + y);
            String reversed_z = new StringBuilder(z).reverse().toString();

            if (z.equals(reversed_z)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
