/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    nums.sort();

    let cur_num = nums[0];
    let cur_cnt = 0;
    let answer = nums[0];
    let max_cnt = 0;
    for(let i=0;i<nums.length;i++){
        if(cur_num != nums[i]){
            if(max_cnt < cur_cnt){
                max_cnt = cur_cnt;
                answer = cur_num;
            }
            cur_num = nums[i];
            cur_cnt = 1;
        }else{
            cur_cnt +=1;
        }
    }
    if(max_cnt < cur_cnt){
        return cur_num;
    }
    return answer;
};