function reverseInPlace(str){
    str = str.split('');
    var left = 0;
    for(var right = 0; right < str.length; right++){
        if (str[right] == ' '){
            reverse(str, left, right - 1);
            left = right + 1;
        }
    }

    reverse(str, left, str.length - 1);

    function reverse(str, left, right) {
        while (left < right) {
            var tmp;
            tmp = str[left];
            str[left] = str[right];
            str[right] = tmp;
            left ++;
            right --;
        }
    }
    return str.join('');
}

console.log(reverseInPlace('aabb cd eef'))