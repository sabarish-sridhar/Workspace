// Source : https://leetcode.com/problems/smallest-index-with-equal-value/submissions/
class Solution {
public:
    int smallestEqual(vector<int>& nums) {
        
        for(int i=0;i<size(nums);i++)
        {
            if(i%10==nums[i])
            {
                return i;
            }
        }
        return -1;
    }
};