import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        Arrays.sort(numbers);
        
        int max = numbers[0] * numbers[1];
        int min = numbers[numbers.length-1] * numbers[numbers.length - 2];
        if (max>min){
            answer = max;
        }
        else{
            answer = min;
        }
        return answer;
    }
}