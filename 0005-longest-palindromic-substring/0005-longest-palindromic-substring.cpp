class Solution {
public:
    string longestPalindrome(string s) {
        string res = "";

        for (int i = 0; i < s.size(); i++) {
            int l = i, r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > res.size())
                    res = s.substr(l, r - l + 1);
                l--;
                r++;
            }

            l = i;
            r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > res.size())
                    res = s.substr(l, r - l + 1);
                l--;
                r++;
            }
        }

        return res;
    }
};