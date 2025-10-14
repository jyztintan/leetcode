
/*
 * prices -> array of integers,
 * price[i] > 0 -> price of stock on i-th day
 * buy and sell stock on DIFFERENT days
 * max profit obtained
 * only buy and sell once
 */
import java.lang.Math;

public class BuySellStock {
    public static int simulate(int[] prices) {
        int profit = 0;
        int lowest = Integer.MAX_VALUE;
        // iterate
        for (int i = 0; i < prices.length; i++) {
            int current = prices[i];
            if (current <= 0) {
                throw new RuntimeException("Prices cannot be less than 0");
            }
            profit = Math.max(profit, current - lowest); // syntax
            lowest = Math.min(lowest, current);
        }
        return profit;
    }

    public static void main(String args[]) {
        int tc1[] = { 1, 2, 3, 4, 5 }; // ans: 4
        int tc2[] = { 3, 4, 10, 1, 9 }; // ans: 8
        int tc3[] = {}; // ans: 0
        int tc4[] = { 5, 5, 5, 5, 5, 5, 5 }; // ans: 0
        int tc5[] = { 3, 4, 10, 1, 9 }; // ans: 8
        int tc6[] = { 3, 4, -10, 1, 9 }; // ans: RuntimeException
        System.out.println(BuySellStock.simulate(tc1));
        System.out.println(BuySellStock.simulate(tc2));
        System.out.println(BuySellStock.simulate(tc3));
        System.out.println(BuySellStock.simulate(tc4));
        System.out.println(BuySellStock.simulate(tc5));
        System.out.println(BuySellStock.simulate(tc6));
        return;
    }
}
