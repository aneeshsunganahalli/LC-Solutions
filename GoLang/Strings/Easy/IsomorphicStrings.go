// 205
package easy

func isIsomorphic(s string, t string) bool {
    var map1 [256]int
    var map2 [256]int

    for i := 0; i < len(s); i++ {
        if map1[s[i]] != map2[t[i]] {
            return false
        }
        map1[s[i]] = i + 1
        map2[t[i]] = i + 1
    }
    return true
}
