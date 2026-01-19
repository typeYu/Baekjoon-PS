import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt((br. readLine()));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int sum = 0;
        
        for(int i = 0; i < 3; i++) {
            int val = Integer.parseInt(st.nextToken());
            
            if(val < N) {
                sum += val;
            } else {
                sum += N;
            }
        }
        
        System.out.println(sum);
    }
}
