import java.util.Stack;

/*
 * @lc app=leetcode id=341 lang=java
 *
 * [341] Flatten Nested List Iterator
 */

// @lc code=start
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    private Stack<NestedInteger> stack;
    private Stack<NestedInteger> flat_stack;

    public NestedIterator(List<NestedInteger> nestedList) {
        this.stack = new Stack<NestedIterator>();

        for (NestedInteger nestedInteger : nestedList) {
            this.stack.push(nestedInteger);
        }
    }


    public void explode(){
    while (!this.stack.isEmpty()) {

        if(this.stack.peek().isInteger())
    }
    }

    @Override
    public Integer next() {
        
    }

    @Override
    public boolean hasNext() {
        
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
// @lc code=end

