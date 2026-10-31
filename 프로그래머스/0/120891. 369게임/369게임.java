class Solution {
    public int solution(int order) {
        int answer = 0;
        
        while (order>0){
            int s = order%10;
            if ((s==3) || (s==6) ||(s==9)){
                answer ++;
            }
            order = order / 10;
        }
        return answer;
    }
}