// 01 - Is "else" required?

function checkAge(age) {
    if (age > 18) {
        return true;
    }
    return confirm("Did your parents allowed you?");
    
}

alert(checkAge(19))

// Answer: No, it is not needed.

// --------------------------------------

// 02 - Rewrite the function using '?' or '||'
// The following function returns true if the parameter age is greater than 18.
// Otherwise it asks for a confirmation and returns its result.

// Using ? operator

let age = 18

function checkAge2(age) {
    return (age > 18) ? true : confirm("Did your parents allowed you");
}

alert(checkAge2(age))

// Using || 

function checkAge3(age) {
    return (age > 18) || confirm("Did your parents allowed you?")
}

alert(checkAge3(age))

// --------------------------------------

// 03 - Function min(a, b)
// Write a function min(a,b) which returns the least of two numbers a and b.

function min(a, b) {
    return a < b ? a : b
}

alert(min(5, 2))

// 04 = Function pow(x,n)
// Write a function pow(x,n) that returns x in power n. Or, in other words, multiplies x by itself n times and returns the result.

numero1 = prompt("Digite o primeiro número:")
numero2 = prompt("Digite o segundo número:")

/**
 * Retorna o primeiro valor elevado à potência do segundo valor
 * @param {Number} a primeiro valor 
 * @param {Number} b segundo valor
 * @returns {Number} Valor resultante
 */

function pow(a, b) {
    return a ** b
}

alert(pow(numero1, numero2))

