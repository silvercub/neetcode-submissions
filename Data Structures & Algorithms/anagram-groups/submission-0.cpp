#include <unordered_map>
#include <vector>
#include <algorithm>
#include <string>

class Solution {
public:
    std::vector<std::vector<string>> groupAnagrams(std::vector<string>& strs) {
        std::unordered_map<string, vector<string>> anagrams;
        for (std::string& s: strs)
        {
            std::string key = s;
            std::sort(key.begin(), key.end());
            anagrams[key].push_back(s);
        }
        std::vector<std::vector<string>> result;
        for (auto& pr: anagrams) {
            result.push_back(pr.second);
        }
        return result;
    }
};
