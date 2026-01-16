import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, List<String>> map = new HashMap<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st_each = new StringTokenizer(br.readLine());
            st_each.nextToken();
            String S = st_each.nextToken();

            StringBuilder makeS = new StringBuilder();
            for (int j = 0; j < 3; j++) {
                makeS.append(st_each.nextToken());
            }
            map.computeIfAbsent(makeS.toString(), k -> new ArrayList<>()).add(S);
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer st_each = new StringTokenizer(br.readLine());
            StringBuilder b = new StringBuilder();

            for (int j = 0; j < 3; j++) {
                b.append(st_each.nextToken());
            }

            String sound = b.toString();

            if (!map.containsKey(sound)) {
                System.out.println("!");
            } else if (map.get(sound).size() == 1) {
                System.out.println(map.get(sound).get(0));
            } else {
                System.out.println("?");
            }
        }
    }
}
