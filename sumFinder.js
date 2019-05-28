// Two Sum
// twoSum.py is a better solution (rm dupicates)
function sumFinder(arr, sum){
    var dic = {};
    var res = [];
    for(var i = 0; i < arr.length; i++) {
        dic[arr[i]] = i;
    }

    for(var i = 0; i < arr.length; i++) {
        if(sum - arr[i] in dic) {
            // return pairs of indexes
            res.push([i, dic[sum - arr[i]]]);
        }
    }
    return res;
}

console.log(sumFinder([6,4,3,2,1,7], 9));