// 1781
func beautySum(s string) int {

	res := 0
	n := len(s)

	for i := 0; i < n; i++ {
		count := make([]int, 26)

		for j := i; j < n; j++ {
			count[s[j]-'a']++

			max := 1
			min := 1000

			for _, v := range count {
				if v > 0 {
					if max < v {
						max = v
					}
					if min > v {
						min = v
					}
				}
			}
			res += max - min
		}
	}
	return res
}