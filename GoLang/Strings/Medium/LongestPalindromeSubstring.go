// 5
package medium

func expand(l, r int, s string) string {
    for l >= 0 && r < len(s) && s[l] == s[r] {
        l--
        r++
    }
    return s[l + 1: r]
}
func longestPalindrome(s string) string {

    longest := ""
    for i := 0; i < len(s); i++ {
        odd := expand(i, i, s)
        even := expand(i, i + 1, s)

        if len(odd) > len(longest) {
            longest = odd
        }
        if len(even) > len(longest) {
            longest = even
        }
    }
    return longest   
}