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

alert(`A soma dos salários é R$ ${sumSalaries(salaries)}`)