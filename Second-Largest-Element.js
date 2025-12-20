class Solution {
    secondLargestElement(nums) {
        let L=nums[0]
        let SL=0 
        for(let i=0; i<nums.length-1;i++){
            if (nums[i]<nums[i+1]){
                SL=L
                L=nums[i+1]
            }
            if (L>nums[i]>SL){
                SL=nums[i]
            }
        }
        if (SL===0){
            return '-1'
        }
        else if (L>nums[i+1]>SL){ 
            SL=nums[i+1]
        }
        return SL
    }
}
let n=[7, 7, 2, 2, 10, 10, 10]
console.log(new Solution().secondLargestElement(n))
