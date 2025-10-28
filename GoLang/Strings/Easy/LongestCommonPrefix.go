// 14
package easy
import "sort"

func longestCommonPrefix(strs []string) string {
    
    sort.Strings(strs)
    first := strs[0]
    last := strs[len(strs) - 1]

    smaller := first
    if len(smaller) > len(last) {
        smaller = last
    }
    index := 0
    for i := 0; i < len(smaller); i++ {
        if first[i] != last[i] {
            break
        }
        index++
    }
    return smaller[:index]
}