// 01 - Last loop value
// What is the last value alerted by this code? Why?

// let i = 3;

// while (i) {
//   alert( i-- );
// }

//--------------------------------------------------

// 02 - Which values does the while loop show?
// For every loop iteration, write down which value it outputs and then compare it with the solution.

// Both loops alert the same values, or not?

// The prefix form ++i:

let a = 0;
while (++a < 5) 
alert( a );

// The postfix form i++

let i = 0;
while (i++ < 5) 
alert( i );

//-------------------------------------------------

// 03 - Which values get shown by the "for" loop?
// For each loop write down which values it is going to show. Then compare with the answer.

// Both loops alert same values or not?

// The postfix form:

for (let i = 0; i < 5; i++) alert( i );

// The prefix form:

for (let i = 0; i < 5; ++i) alert( i );

// -----------------------------------------------

// 04 - Output even numbers in the loop
// Use the for loop to output even numbers from 2 to 10.

for (let n = 2; n <= 10; ++n) alert (n)