function firstNonRepeatChar(str){
  var len = str.length,
      char,
      // dict
      charCount = {};
  for(var i =0; i<len; i++){
    char = str[i];
    if(charCount[char]){
      charCount[char]++;
    }
    else
      charCount[char] = 1;
  }
  console.log(charCount)
  for (var j in charCount){
    if (charCount[j]==1)
       return j;
  }
}

console.log(firstNonRepeatChar('aabbcdeef'))