// Source : https://leetcode.com/problems/sum-of-unique-elements/
class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int s=0;
        for(auto&i:nums)
        {
            if(std::count(nums.begin(),nums.end(),i)==1)
            {
                s+=i;
            }
        }
        return s;
    }
};
