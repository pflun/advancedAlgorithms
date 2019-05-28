var isPrime = function(n){
    divisor = 2;
    while (n > divisor){
        if (n % divisor == 0) {
            return false;
        }
        else {
            divisor += 1;
        }
    }
    return true
}

console.log(isPrime(237));