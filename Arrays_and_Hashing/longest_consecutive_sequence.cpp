#include<unordered_set>
#include<vector>
using namespace std;
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        unordered_set<int> allNums;
        for (int i = 0; i < nums.size(); i++) {
            allNums.insert(nums[i]);
        }
        
        int longest = 0;
        
        for (int num: allNums) {
            if (allNums.find(num - 1) == allNums.end()) {
                int length = 1;
                while (allNums.find(num + length) != allNums.end()) {
                    length ++;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};
