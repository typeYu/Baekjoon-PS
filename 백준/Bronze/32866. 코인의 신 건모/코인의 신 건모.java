import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int X = sc.nextInt();

        double coinAmount = N * (1 - X / 100.0);
        double Y = (N / coinAmount - 1) * 100;

        System.out.printf("%.6f\n", Y);

        sc.close();
    }
}
