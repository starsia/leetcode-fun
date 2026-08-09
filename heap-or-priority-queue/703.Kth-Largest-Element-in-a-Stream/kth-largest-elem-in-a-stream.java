import java.util.PriorityQueue;

class KthLargest {

    private PriorityQueue<Integer> heap;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.heap = new PriorityQueue<Integer>(k);
        this.k = k;

        for (int i = 0; i < nums.length; i ++) {
            add(nums[i]);
        }
    }
    
    public int add(int val) {
        if (this.heap.size() < this.k) {
            this.heap.add(val);
        }

        else {
            if (this.heap.peek() < val) {
                this.heap.poll();
                this.heap.add(val);
            }
        }
        return this.heap.peek();
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
