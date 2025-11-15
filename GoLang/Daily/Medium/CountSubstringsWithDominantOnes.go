// 3234
package medium
func numberOfSubstrings(s string) int {
    
    res, N := 0, len(s)
    next_zero := make([]int, N)
    next_zero[N - 1] = N

    for i := N - 2; i >= 0; i-- {
        if s[i + 1] == '0' {
            next_zero[i] = i + 1
        } else {
            next_zero[i] = next_zero[i + 1]
        }
    }

    for l := range s {
        zeros := 0
        if s[l] == '0' {
            zeros = 1
        }
        r := l
        for zeros * zeros <= N {
            next_z := next_zero[r]
            ones := next_z - l - zeros
            if ones >= zeros * zeros {
                additional := ones - zeros * zeros + 1
                if additional > next_z - r {
                    additional = next_z - r
                }
                res += additional
            }
            r = next_z
            zeros++
            if r == N { break }
        }
    }
    return res 
}