import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int p = Integer.parseInt(br.readLine());
            int min_num = Integer.MIN_VALUE;
            String answer = "";
            for (int j = 0; j < p; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                String b = st.nextToken();

                if (a > min_num) {
                    min_num = a;
                    answer = b;
                }
            }
            System.out.println(answer);
        }
    }
}
