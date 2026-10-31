class Solution {
    public int solution(int n) {
        int answer = 0;
        int s = (int)Math.sqrt(n);
        
        if ((s*s)==n){
            answer = 1;
        }
        else{
            answer = 2;
        }
        return answer;
    }
}