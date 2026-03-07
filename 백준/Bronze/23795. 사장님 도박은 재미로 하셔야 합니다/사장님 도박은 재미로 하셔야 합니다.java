import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main extends Exception {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int sum = 0;

        while(true){
            int num = Integer.parseInt(br.readLine());

            if (num == -1){
                break;
            }else{
                sum += num;
            }
        }
        
        sb.append(sum);
        System.out.println(sb.toString());
    }
}