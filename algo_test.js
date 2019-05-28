function js_test(str){
    return str + str;
//  return str.concat(str);
}

function isTwoPassed(){
  var args = Array.prototype.slice.call(arguments);
  return args.indexOf(2) != -1;
}

function returnArg(){
    return arguments;
}

function log(){
  var args = Array.prototype.slice.call(arguments);
  var my_array = new Array('1','2','3','4');
  var my_array1 = new Array('5','6');
  var my_array2 = new Array('7','8');
  var new_array = my_array.concat(my_array1,my_array2);

  d = new Date();
  day = d.getDay();
  console.log(args.toString());
}

isTwoPassed(1,4); //false
console.log(isTwoPassed(5,3,1,2)); //true

console.log(js_test('aabbcdeef'))

console.log(returnArg('aabbcdeef', '222'))

log('my message');

var a = 1;
function b() {
    a = 10;
    return;
//    var a;
}
b();
console.log(a);

function addBase(){
    var base = arguments[0];
    return function(num){
        return base + num;
    }
}

var addTen = addBase(10);
console.log(addTen(5)); //15
console.log(addTen(80)); //90