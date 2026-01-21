import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        int answer = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ring = br.readLine();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String S = br.readLine();
            for (int j = 0; j < S.length(); j++) {
                StringBuilder res = new StringBuilder();
                for (int k = 0; k < ring.length(); k++) {
                    char c = S.charAt((j + k) % S.length());
                    res.append(c);
                }
                if (res.toString().equals(ring)) {
                    answer += 1;
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}
