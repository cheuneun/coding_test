import java.util.Arrays;
class Solution {
    public int[] solution(String my_string) {
        int count = 0;
        for (int i=0;i<my_string.length();i++){
            char ch = my_string.charAt(i);
            if (Character.isDigit(ch)){
                count ++;
            }
        }
        int idx = 0;
        int[] answer = new int[count];
        for (int i=0;i<my_string.length();i++){
            char ch = my_string.charAt(i);
            if (Character.isDigit(ch)){
                answer[idx] = ch - '0';
                idx ++;
            }
        }
        Arrays.sort(answer);
        return answer;
    }
}