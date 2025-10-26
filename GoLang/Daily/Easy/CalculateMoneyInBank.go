// 1716
package easy

func sumofAP(n int, a int, d int) int {
        return n * (2*a + (n-1)*d) / 2
}

func totalMoney(n int) int {
    res := 0
    count := 1
    i := 1
    weeks := n / 7

    for i <= weeks {
        res += sumofAP(7, count, 1)
        i++
        count++
    }
    res += sumofAP(n % 7, count, 1)
    return res
}