import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        Double a = Double.parseDouble(st.nextToken());
        Double b = Double.parseDouble(st.nextToken());

        System.out.println(a / b);
        }
    }