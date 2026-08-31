class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = new Map();
        for(let str of strs){
            let sortedStr = str.split('').sort().join('');
            map.set(sortedStr,[...(map.get(sortedStr) || []),str]);
        }
        return [...map.values()];
    }
}
