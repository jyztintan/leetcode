import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        Set<Character> allowedChars = new HashSet<>();
        for (char c : allowed.toCharArray()) {
            allowedChars.add(c);
        }

        int count = 0;
        outerLoop:
        for (String word: words) {
            for (char c: word.toCharArray()) {
                if (!allowedChars.contains(c)) {
                    continue outerLoop;
                }
            }
            count += 1;
        }
        return count;
    }
}
