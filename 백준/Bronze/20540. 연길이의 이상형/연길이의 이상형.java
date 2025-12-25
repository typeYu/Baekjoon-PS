import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String mbti = br.readLine();

        Map<Character, Character> map = new HashMap<>();
        map.put('E', 'I');
        map.put('I', 'E');
        map.put('S', 'N');
        map.put('N', 'S');
        map.put('T', 'F');
        map.put('F', 'T');
        map.put('P', 'J');
        map.put('J', 'P');

        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < mbti.length(); i++) {
            char s = mbti.charAt(i);
            char res = map.get(s);
            answer.append(res);
        }

        System.out.println(answer);
    }
}
