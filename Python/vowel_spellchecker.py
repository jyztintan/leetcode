class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            ret = []
            for c in word:
                if c in "aeiouAEIOU":
                    ret.append('*')
                else:
                    ret.append(c)
            return "".join(ret).lower()

        exact_match = set(wordlist)
        case_match = {}
        vowel_match = {}
        for word in wordlist:
            low = word.lower()
            if low not in case_match:
                case_match[low] = word
            devoweled = devowel(word)
            if devoweled not in vowel_match:
                vowel_match[devoweled] = word

        resp = []
        for query in queries:
            if query in exact_match:
                resp.append(query)
            elif query.lower() in case_match:
                resp.append(case_match[query.lower()])
            elif devowel(query) in vowel_match:
                resp.append(vowel_match[devowel(query)])
            else:
                resp.append("")
        return resp
