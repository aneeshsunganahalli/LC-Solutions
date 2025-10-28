// 451
package medium
import "sort"

func frequencySort(s string) string {
	freq := make(map[rune]int)
	for _, ch := range s {
		freq[ch]++
	}

	type pair struct {
		ch   rune
		freq int
	}
	pairs := make([]pair, 0, len(freq))
	for ch, f := range freq {
		pairs = append(pairs, pair{ch, f})
	}

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].freq > pairs[j].freq
	})

	res := make([]rune, 0, len(s))
	for _, p := range pairs {
		for i := 0; i < p.freq; i++ {
			res = append(res, p.ch)
		}
	}
	return string(res)
}
