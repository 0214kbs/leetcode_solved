class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 1) return 1;
        int left = 0;
        int i = 0;
        for(int right = 0; right<nums.length;right++){
            if(nums[left] == nums[right]){
                if(right - left <2){
                    nums[i] = nums[right];
                    i+=1;
                }
            }else{
                left = right;
                nums[i] = nums[right];
                i++;
            }
        }
        return i;
    }
}