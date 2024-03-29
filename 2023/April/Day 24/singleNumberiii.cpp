// Source : https://leetcode.com/problems/single-number-iii/submissions/
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        
        sort(nums.begin(),nums.end());
        vector<int> out;
        for(int i=0;i<size(nums);i++)
        {
            if(size(out)==2){break;}
            if(i==0)
            {
                if(nums[i]!=nums[i+1])
                {
                    out.insert(out.end(),nums[i]);
                }
            }
            else if(i==size(nums)-1)
            {
                if(nums[i]!=nums[i-1])
                {
                    out.insert(out.end(),nums[i]);
                }
            }
            
            else
            {
                
                if( (nums[i]!=nums[i-1]) && (nums[i]!=nums[i+1])) 
                {
                    out.insert(out.end(),nums[i]);
                }
            }
        }
        return out;
        
    }
};