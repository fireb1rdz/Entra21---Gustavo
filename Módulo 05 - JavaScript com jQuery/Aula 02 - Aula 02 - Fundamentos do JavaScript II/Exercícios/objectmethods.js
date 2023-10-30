// 01 - Sum the properties

let salaries = {
    "John": 100,
    "Pete": 300,
    "Mary": -250
};

const sumSalaries = obj => {
    let accumulator = 0
    for (let key in obj) if (obj[key] >= 0) {
        accumulator += obj[key]
    }
    return accumulator
}
console.log(`A soma dos salários é R$ ${sumSalaries(salaries)}`)

// -------------------------------------------

// Count properties
// Write a function count(obj) that returns the number of properties in the object:

const contProperties = (obj) => {
    counter = 0
    for (key in obj) {
        counter += 1
    } return counter
}

alert(`A quantidade de propriedades desse objeto é ${contProperties(salaries)}`)