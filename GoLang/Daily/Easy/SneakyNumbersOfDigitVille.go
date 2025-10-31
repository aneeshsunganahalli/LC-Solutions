// 3289 

package easy
func getSneakyNumbers(nums []int) []int {

    var res []int
    n := len(nums)

    for i := 0; i < n; i++ {
        x := nums[i] % n
        nums[x] += n
    }

    for i := 0; i < n; i++ {
        if nums[i] / n == 2 {
            res = append(res, i)
        }
    }
    return res
}