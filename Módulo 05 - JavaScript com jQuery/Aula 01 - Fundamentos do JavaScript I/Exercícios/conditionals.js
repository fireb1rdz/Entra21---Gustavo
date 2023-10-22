// 01 - if (a string with zero)
// Will alert be shown?

if ("0") {
    alert( 'Hello' );  // Yes, it will be shown, because all strings except an empty one becomes true in the logical context
  }

  // -----------------------------------------------------------------------------------------------------

// 02 - The name of JavaScript
// Using the if..else construct, write the code which asks: ‘What is the “official” name of JavaScript?’
// If the visitor enters “ECMAScript”, then output “Right!”, otherwise – output: “You don’t know? ECMAScript!”

guess = prompt("What is the `Official` name of JavaScript?")

if (guess === "ECMAScript") {
    alert("Right!");
    } else {
        alert("You don't know? ECMAScript!")
}


// --------------------------------------------------------------------------------------------------------------
// 03 - Show the sign
// Using if..else, write the code which gets a number via prompt and then shows in alert:

// 1, if the value is greater than zero,
// -1, if less than zero,
// 0, if equals zero.
// In this task we assume that the input is always a number.

number = prompt("Write a number")

if (number > 0) {
    alert("1")
} else if (number < 0){
    alert("-1")
} else {
    alert("0")
}