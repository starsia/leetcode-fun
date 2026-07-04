class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int last = nums[right];

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] > last) {
                left = mid + 1;
            }

            else {
                right = mid;
            }
        }

        return nums[left];

    }
}
