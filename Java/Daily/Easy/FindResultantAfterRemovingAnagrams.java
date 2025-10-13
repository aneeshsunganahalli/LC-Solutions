package Easy;
import java.util.*;
// 2273
class Solution {
    static String sortString(String s) {
    char[] arr = s.toCharArray();
    Arrays.sort(arr);
    return new String(arr);
}
    public List<String> removeAnagrams(String[] words) {
    String prev="";
    List<String>ans=new ArrayList<>();
    for(int i=0;i<words.length;i++)
    {
        String str=sortString(words[i]);
        if(!str.equals(prev))
        {
            prev=str;
            ans.add(words[i]);
        }
    }
    return ans;
    }
}