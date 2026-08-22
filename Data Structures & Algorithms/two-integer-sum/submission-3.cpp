#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        int match = 0;
        for(int i = 0; i < nums.size(); i++) {
            match = target - nums[i];
            auto it = seen.find(match);
            if (it != seen.end()) {
                if (i < seen[match]) {
                    return {i, seen[match]};
                } else {
                    return {seen[match], i};
                }
            }
            seen[nums[i]] = i;
        }
        return {-1, -1};
    }
};
