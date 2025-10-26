// 1903
package easy

func largestOddNumber(num string) string {

    for i := len(num) - 1; i >= 0; i-- {
        digit := num[i] - '0'
        if digit % 2 == 1 {
            return num[:i + 1]
        }
    }
    return ""
}