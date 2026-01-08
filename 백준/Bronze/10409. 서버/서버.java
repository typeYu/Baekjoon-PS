import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		//일의 수
		int n = Integer.parseInt(st.nextToken());
		//주어진 시간
		int T = Integer.parseInt(st.nextToken());
		//끝낸 일의 수
		int i = 0;
		
		st = new StringTokenizer(br.readLine());
		for(i = 0; i < n; i++) {
			//주어진 시간에 입력된 시간을 빼준다.
			T -= Integer.parseInt(st.nextToken());
			//주어진 시간이 다 지나가면 반복문 종료
			if(T < 0) {
				break;
			}
		}
		//끝낸 일의 수를 출력
		System.out.println(i);
	}

}
