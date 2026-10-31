class Solution {
    public int solution(int hp) {
        int answer = 0;
        int boss = hp/5;
        int ww = (hp%5)/3;
        int www = (hp%5)%3;
        answer = boss + ww +www;
        return answer;
    }
}