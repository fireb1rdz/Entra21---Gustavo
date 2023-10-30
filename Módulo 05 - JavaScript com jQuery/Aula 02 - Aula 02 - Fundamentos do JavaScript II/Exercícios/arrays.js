// 01 - Is array copied?
// What is this code going to show?

// let fruits = ["Apples", "Pear", "Orange"];

// push a new value into the "copy"
// let shoppingCart = fruits;
// shoppingCart.push("Banana");

// what's in fruits?
// alert( fruits.length ); // ?

// Answer: it is going to show 4

// -----------------------------------------------------------

// 02 - Array operations
// Let’s try 5 array operations.

// Create an array styles with items “Jazz” and “Blues”.
// Append “Rock-n-Roll” to the end.
// Replace the value in the middle with “Classics”. Your code for finding the middle value should work for any arrays with odd length.
// Strip off the first value of the array and show it.
// Prepend Rap and Reggae to the array.
// The array in the process:

// Jazz, Blues
// Jazz, Blues, Rock-n-Roll
// Jazz, Classics, Rock-n-Roll
// Classics, Rock-n-Roll
// Rap, Reggae, Classics, Rock-n-Roll

let arr = ["Jazz", "Blues"]

arr.push("Rock-n-Roll")

arr.splice((arr.length-1)/2, 1, "Classics")

alert(arr.shift())

arr.unshift("Rap", "Reggae")

alert(arr)