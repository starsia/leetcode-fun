func maxProfit(prices []int) int {
    curr := prices[0]
    res := 0

    for i := 1; i < len(prices); i++ {
        if prices[i] < curr {
            // lowest price is lower
            curr = prices[i]
        } else if (prices[i] - curr > res) {
            // profit is more
            res = prices[i] - curr
        }
    }

    return res
}
