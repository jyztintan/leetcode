class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for (auto& s : strs) {
            res += to_string(s.length()) + "#" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        int index = 0;
        vector<string> res;
        while (index < s.length()) {
            int pos = s.find('#', index);
            if (pos == string::npos) {
                break;
            }
            int len = stoi(s.substr(index, pos - index));
            string to_add = s.substr(pos + 1, len);
            res.push_back(to_add);

            index = pos + len + 1;
        }
        return res;
    }
};
