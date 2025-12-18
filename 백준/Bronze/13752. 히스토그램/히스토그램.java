import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int testCase = sc.nextInt();

        for (int i = 0; i < testCase; i++) {
            int histogram_val = sc.nextInt();
            String bar = "=";
            String histogram_bar = bar.repeat(histogram_val);

            System.out.println(histogram_bar);
        }
    }
}