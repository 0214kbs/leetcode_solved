/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length === 0) return 0; 
    let ri = 0; // result index
    let ci = 1; // check index

    while (ci < nums.length){
        if(nums[ri] !== nums[ci]){
            ri++;
            nums[ri] = nums[ci];
            ci++;
        }else{
            ci++;
        }
    }
    return ri+1;
};