#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> letter_count;
        for (const char& c: s) {
            auto it = letter_count.find(c);
            if (it != letter_count.end()) {
                letter_count[c]++;
            } else {
                letter_count[c] = 1;
            }
        }
        for (const char& c: t) {
            auto it = letter_count.find(c);
            if(it != letter_count.end()) {
                letter_count[c]--;
            } else {
                return false;
            }
            if (letter_count[c] == 0) {
                letter_count.erase(c);
            }
        }
        if (letter_count.empty()) {
            return true;
        }
        return false;
    }
};
