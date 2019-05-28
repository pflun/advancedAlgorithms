function primeFactors(n){
  var res = [],
      divisor = 2;
  while (n > 2){
    if (n % divisor == 0) {
            res.push(divisor);
            n = n / divisor;
        }
    else {
            divisor += 1
        }
  }
  return res
}

console.log(primeFactors(69));