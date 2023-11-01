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

console.log(arr)

// 03 - Calling in an array context
// What is the result? Why?

let arr2 = ["a", "b"];

arr2.push(function() {
  alert( this );
});

alert(arr2[2]()); // ?

// 04 - Sum input numbers
// Write the function sumInput() that:

// Asks the user for values using prompt and stores the values in the array.
// Finishes asking when the user enters a non-numeric value, an empty string, or presses “Cancel”.
// Calculates and returns the sum of array items.
// P.S. A zero 0 is a valid number, please don’t stop the input on zero.

arr = []

const sumInput = () => {
    while (true) {
        let value = prompt("Digite um número")
        if (typeof(+value) !== "number" || value === "" || value === null) {
            break;
        } else {
            arr.push(value)
        }

    }
    accumulator = 0
    for (num of arr) {
        accumulator += Number(num)
    }
    alert(accumulator)

}

sumInput()