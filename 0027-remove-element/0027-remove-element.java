class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length == 0){
            return 0;
        }

        int res_i = 0;
        for(int check_i=0;check_i<nums.length;check_i++){
            if(nums[check_i] != val){
                nums[res_i] = nums[check_i];
                res_i++;
            }
        }

        return res_i;
    }
}