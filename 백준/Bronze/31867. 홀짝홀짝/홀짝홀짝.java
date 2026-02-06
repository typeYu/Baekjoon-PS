import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    String k = sc.next();

    int evenCount = 0;
    int oddCount = 0;

    for (int i = 0; i < n; i++) {
      int digit = k.charAt(i) - '0';
      if (digit % 2 == 0) {
        evenCount++;
      } else {
        oddCount++;
      }
    }

    if (evenCount > oddCount) {
      System.out.println(0);
      return;
    }

    if (oddCount > evenCount) {
      System.out.println(1);
      return;
    }

    System.out.println(-1);
  }
}
