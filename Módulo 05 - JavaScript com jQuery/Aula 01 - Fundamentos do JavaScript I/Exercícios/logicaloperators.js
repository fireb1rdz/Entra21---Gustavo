// 01 - What's the result of OR?
// What is the code below going to output?

alert(null||2||undefined)

// It will show the number 2, because it is the first truthy value

//------------------------------------------------------------

// 02 - What's the result of OR'ed alerts?
// What will the code below output?

alert(alert(1) || 2 || alert(3));

// It will show the first alert and the number 2

//------------------------------------------------------------

// 03 - What is the result of AND?
//What is this code going to show?

alert( 1 && null && 2);

// The result is the null, because it is the first falsy value

//------------------------------------------------------------

// 04 - What is the result of AND'ed alerts?
// What will this code show?

alert( alert(1) && alert(2) );

// It will show both alerts, because they are falsy

//------------------------------------------------------------

// 05 - The result of OR AND OR
// What will the result be?

alert( null || 2 && 3 || 4 );

// It will show only the 4, because it is the only truly value