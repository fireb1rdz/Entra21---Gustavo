// 01 - The postfix and prefix forms
// What are the final values of all variables a, b, c and d after the code below?

let f = 1, b = 1;

let c = ++f; // 2
let d = b++; // 1

alert(c);
alert(d);

// --------------------------------------------------------------------------------------------

// 02 - Assignment result
//What are the values of a and x after the code below?

let a = 2;

let x = 1 + (a *= 2); // 5

alert(`O resultado de X é ${x}`)

// --------------------------------------------------------------------------------------------

// 03 - Type conversions
//What are results of these expressions?

"" + 1 + 0 // 10
"" - 1 + 0 // -1
true + false // 1
6 / "3" // 2
"2" * "3" // 6
4 + 5 + "px" // 9px
"$" + 4 + 5 // $45
"4" - 2 // 2
"4px" - 2 // NaN
"  -9  " + 5 //  -9  5
"  -9  " - 5 // -14
null + 1 // 1
undefined + 1 // NaN
" \t \n" - 2 // -2
