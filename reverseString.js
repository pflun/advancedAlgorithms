var reverseString = function(s) {
    var res = "";
    var high = s.length - 1;
    var i
    for(i = high; i >= 0; i--) {
        res += s.charAt(i);
    }

    return res

};