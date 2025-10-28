// 3354
package easy

// absInt must be defined outside (Go doesn’t allow nested functions)
func absInt(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func countValidSelections(nums []int) int {
    left, res, right := 0, 0, 0
    for _, val := range nums {
        right += val
    }

    for _, num := range nums {
        if num == 0 {
            if absInt(right-left) == 1 {
                res += 1
            }
            if left == right {
                res += 2
            }
        } else {
            left += num
            right -= num
        }
    }
    return res
}
