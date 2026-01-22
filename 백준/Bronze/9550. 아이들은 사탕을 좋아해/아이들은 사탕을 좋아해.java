import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            StringTokenizer type = new StringTokenizer(br.readLine());

            int ans = 0;
            for(int j = 0; j < N; j++) {
                int candy = Integer.parseInt(type.nextToken());
                ans += candy / K;
            }
            System.out.println(ans);
        }
    }
}
