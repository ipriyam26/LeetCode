import java.util.HashMap;

/*
 * @lc app=leetcode id=208 lang=java
 *
 * [208] Implement Trie (Prefix Tree)
 */

// @lc code=start

class TrieNode {

  HashMap<Character, TrieNode> character;
  boolean isLast;
  Character value;

  public TrieNode(char val) {
    value = val;
    character = new HashMap<>();
    isLast = false;
  }
}

class Trie {

  TrieNode root;

  public Trie() {
    root = new TrieNode(' ');
  }

  public void insert(String word) {
    TrieNode temp = root;
    for (int i = 0; i < word.length(); i++) {
      char letter = word.charAt(i);
      if (temp.character.containsKey(letter)) {
        temp = temp.character.get(letter);
      } else {
        temp.character.put(letter, new TrieNode(letter));
        temp = temp.character.get(letter);
      }
    }
    temp.isLast = true;
  }

  public boolean search(String word) {
    TrieNode temp = root;
    for (int i = 0; i < word.length(); i++) {
      char letter = word.charAt(i);
      if (!temp.character.containsKey(letter)) {
        return false;
      }
    }
    return temp.isLast;
  }

  public boolean startsWith(String word) {
    TrieNode temp = root;
    for (int i = 0; i < word.length(); i++) {
      char letter = word.charAt(i);
      if (!temp.character.containsKey(letter)) {
        return false;
      }
    }
    return true;
  }
}
/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
// @lc code=end
