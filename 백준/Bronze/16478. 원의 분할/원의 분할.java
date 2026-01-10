import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    double pab = Double.parseDouble(st.nextToken());
    double pbc = Double.parseDouble(st.nextToken());
    double pcd = Double.parseDouble(st.nextToken());

    double pda = (pab * pcd) / pbc;

    System.out.println(pda);
  }
}
