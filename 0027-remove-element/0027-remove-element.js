/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    if( nums.length === 0){
        return 0;
    }

    let res_i = 0;
    for(let check_i=0;check_i<nums.length;check_i++){
        if(nums[check_i] !== val){
            nums[res_i] = nums[check_i];
            res_i++;
        }
    }
    return res_i;
};