// 2125
package medium

func numberOfBeams(bank []string) int {
    res, prev := 0, 0
    for _, row := range bank {
        cams := 0
        for _, c := range row {
            if c == '1' {
                cams++
            }
        }
        if cams > 0 {
            res += cams * prev
            prev = cams
        }
    }
    return res
}
