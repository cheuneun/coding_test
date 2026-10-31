class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String s = num + "";
        char kk = (char) (k + '0');
        
        for (int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if (ch == kk){
                answer = i+1;
                break;
            }
        }
        return answer;
    }
}