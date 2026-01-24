import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int t = Integer.parseInt(br.readLine());

    for (int i = 0; i < t; i++) {
      int time = Integer.parseInt(br.readLine());

      if (time % 25 < 17) {
        System.out.println("ONLINE");
      } else {
        System.out.println("OFFLINE");
      }
    }
  }
}
