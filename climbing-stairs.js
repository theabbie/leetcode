/**
 * @param {number} n
 * @return {number}
 */

const memo = {};

var climbStairs = function(n) {
    if (n < 0) return 0;
    if (n == 0) return 1;
    if (memo[n] != undefined) return memo[n];
    let res = climbStairs(n - 1) + climbStairs(n - 2);
    memo[n] = res;
    return res;
};