// 1262
package medium
func maxSumDivThree(nums []int) int {
    
    total := 0
    smallest_one := 100000
    smallest_two := 100000

    for _, val := range nums {
        total += val
        if val % 3 == 1 {
            if smallest_two > smallest_one + val {
                smallest_two = smallest_one + val
            }
            if smallest_one > val {
                smallest_one = val
            }
        } else if val % 3 == 2 {
            if smallest_one > smallest_two + val {
                smallest_one = smallest_two + val
            }
            if smallest_two > val {
                smallest_two = val
            }
        }
    }

    if total % 3 == 0 { return total }
    if total % 3 == 1 { return total - smallest_one }
    if total % 3 == 2 { return total - smallest_two } 
    return -1
}