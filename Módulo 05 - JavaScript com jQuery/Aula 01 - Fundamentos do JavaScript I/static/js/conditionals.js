const javascriptAge = +prompt("Quantos anos o JavaScript possui?");

if (javascriptAge > 27) {
    alert("A idade digitada é maior do que a real");
} else if (javascriptAge < 27) {
    alert("A idade digitada é menor do que a real");
} else {
    alert("Você acertou!")
}

const currentHour = new Date().getHours();

// && (AND)

if (currentHour < 7 && currentHour < 19) {
    alert("Escritório aberto");
} else {
    alert("Escritório fechado")
}

// || (OR)

if (currentHour < 8 || currentHour > 18) {
    alert("Escritório fechado");
} else {
    alert("Escritório aberto")
}

// NOT
alert(!true)

// Diferente -> !==

const currentMonth = new Date().getMonth() + 1;

switch (currentMonth) {
    case 1:
        alert("Janeiro");
        break;

    case 2:
        alert("Fevereiro")
        break;
    
    case 3:
        alert("Março");
        break;
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
    case 11:
    case 12:
        alert("outros meses");
        break
    default:
        alert("Mês inválido!");
        break;
}

