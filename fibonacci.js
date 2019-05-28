function fibonacci(n){
  var fibo = [0, 1];

  if (n <= 2) return 1;

  for (var i = 2; i <=n; i++ ){
   fibo[i] = fibo[i-1] + fibo[i-2];
  }

 return fibo[n];
}

console.log(fibonacci(6));