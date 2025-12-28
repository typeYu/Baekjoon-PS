import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();

        // while문으로 각 자릿수를 계속 판별
        while (true) {
            // 모두 4와 7로 구성되었는지 판별하는 함수
            boolean is_47 = true;

            // 각 자릿수 판별
            for (int i = 0; i < N.length(); i++) {
                char n = N.charAt(i);
                if (n != '4' && n != '7') {
                    is_47 = false;
                    break;
                }
            }

            // 만약 반복문을 돌려서 모든 자릿수가 4나 7이라면 break 후 출력
            if (is_47) {
                break;
            // 그렇지 않다면 1을 빼줌
            } else {
                N = String.valueOf(Integer.parseInt(N) - 1);
            }
        }
        System.out.println(N);
    }
}
