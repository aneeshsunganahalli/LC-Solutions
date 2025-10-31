// 8
package medium

import (
	"strings"
	"unicode"
)

func myAtoi(s string) int {
    
    str := strings.TrimSpace(s)
    n := len(str)
    if n == 0 {
        return 0
    }

    i := 0
    res := 0
    sign := 1

    if str[i] == '-' {
        sign = -1
        i++
    } else if str[i] == '+' {
        i++
    }

    for i < n {
        if !unicode.IsDigit(rune(str[i])) {
            break
        }
        res = res * 10 + int(str[i] - '0')
        if res * sign >  2147483647 {
            return  2147483647
        } 
        if res * sign  < - 2147483648 {
            return  -2147483648
        }
        i++
    }

    return res * sign

}