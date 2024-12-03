import java.util.Arrays;

class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int cur_num = nums[0];
        int cur_cnt = 0;
        int max_cnt = 0;
        int answer = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i] == cur_num){
                cur_cnt +=1;
            }else{
                if(max_cnt < cur_cnt){
                    max_cnt = cur_cnt;
                    answer = cur_num;
                }
                cur_num = nums[i];
                cur_cnt = 1;
            }
        }
        if(max_cnt < cur_cnt){
            max_cnt = cur_cnt;
            answer = cur_num;
        }
        return answer;

    }
}