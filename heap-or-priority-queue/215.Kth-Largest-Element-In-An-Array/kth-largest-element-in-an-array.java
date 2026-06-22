class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        // smallest number should be at the root, so we use a min heap. in java, this is the default.
        // we keep a heap with a fixed size of k and anything smaller than the accessed element gets 
        // pushed off

        // time complexity is O(n log k) as heap operations will take O(log k) time. Each element
        // is accessed once. 
        // space complexity is O(k) depending on the size of the priority queue. 

        for (int i = 0; i < nums.length; i++) {
            if (pq.size() < k) {
                pq.add(nums[i]);
            }
            else {
                if (pq.peek() < nums[i]) {
                    pq.poll();
                    pq.add(nums[i]);
                }
            }
        }
        return pq.peek();
    }
}
