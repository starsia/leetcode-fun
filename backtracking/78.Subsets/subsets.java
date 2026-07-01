class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();

        private static void dfs(int x) {
            if (x > nums.length() - 1) {
                res.append(subset);
            }
            subset.append(x);
            dfs(x + 1);

            subset.pop();
            dfs(x - 1);
            return
        }


        dfs(0);
        return res;
    }
}
