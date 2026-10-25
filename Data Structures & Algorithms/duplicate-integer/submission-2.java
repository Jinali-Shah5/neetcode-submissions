class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
       
       for(int i = 0;i<nums.length;i++){
        int left = i+1;
       int right = nums.length-1;
       while(left<=right){
        int mid = (left+right)/2;
        if(nums[i]>nums[mid]){
            left=mid+1;
        }
        else if(nums[i]==nums[mid]){
            return true;
        }
        else{
            right = mid-1;
        }
        
       }

    }
    return false;}}
