// 1513
package medium
func numSub(s string) int {
    
    res, ones := 0, 0
    const MOD = 1000000007

    for i := range s {
        if s[i] == '1' {
            ones++
        } else {
            res += (ones * (ones + 1)) / 2
            ones = 0
        }
        res = res % MOD
    }
    res += (ones * (ones + 1)) / 2
    return res % MOD
}