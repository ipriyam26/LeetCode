/*
 * @lc app=leetcode id=394 lang=java
 *
 * [394] Decode String
 */

// @lc code=start
class Solution {
    public String decodeString(String s) {
return processString(s);
    }

    public boolean containsNumber(String s) {
        for (Character item : s.toCharArray()) {
            if (item >= '0' && item <= '9') {
                return true;
            }
        }

        return false;
    }

    public boolean isDigit(Character a) {
        if ( a>= '0' && a <= '9') {
            return true;

        }
        return false;
    }

    public String multiplyString(String str, int times) {
        String result = "";
        while (times != 0) {
            result += str;
            times--;
        }
        return result;
    }

    public String processString(String str) {
        int i = 0;
        String result = "";

        while (i < str.length()) {
            char a = str.charAt(i);
            if (isDigit(a)) {
                int controllingDigit = a - '0';
                i += 2;
                String temp = "";
                int settle = 1;
                boolean containsMoreBrackets = false;
                while (settle != 0) {
                    char ans = str.charAt(i);
                    if (ans == '[') {
                        settle++;
                        containsMoreBrackets = true;
                    } else if (ans == ']') {
                        settle--;
                    }
                    temp += ans;
                    i++;
                }
                temp = temp.substring(0,temp.length());

                if (containsMoreBrackets) {
                    temp += processString(str);
                }
                result += multiplyString(str, controllingDigit);
            } else {
                result += a;
            }

            i++;

        }

        return result;

    }
}
// @lc code=end
