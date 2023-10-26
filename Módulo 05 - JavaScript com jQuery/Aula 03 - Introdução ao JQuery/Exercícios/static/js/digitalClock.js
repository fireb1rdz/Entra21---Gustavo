// Selecionando os elementos do DOM
const $clock = $(".clock");
const $date = $(".date");
const $toggleButton = $("#toggleButton")

/**
 *Atualiza o relógio
 */
const updateClock = () => $clock.text(new Date().toLocaleTimeString());

/**
 * Formata o dia da semana de número para o formato português
 * @param {number} dayOfWeek - Dia da semana 
 * @returns {string} dia da semana formatado
 */
const formatDayOfWeek = (dayOfWeek) => {
    const daysOfWeek = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"];
    return daysOfWeek[dayOfWeek];
};

/**
 * Formata o mês de número para português
 * @param {number} month - número do mês 
 * @returns {string} dia do mês formatado
 */
const formatMonth = (month) => {
    const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
    return monthNames[month];
};

/**
 * Formata o dia do mês para que ele sempre possua duas casas
 * @param {number} day - dia do mês
 * @returns {string} dia do mês com duas casas
 */
const formatDay = (day) => String(day).padStart(2, "0");

/**
 * Atualiza a data
 */
const updateDate = () => {
    const today = new Date();
    const dayOfWeek = formatDayOfWeek(today.getDay());
    const month = formatMonth(today.getMonth());
    const day = formatDay(today.getDate());
    const year = today.getFullYear();

    $date.text(`${dayOfWeek}, ${day} de ${month} de ${year}`);
};


updateClock();
updateDate();

// setInterval() -> Executar uma ação em um determinado intervalo, para sempre!
// setTimeout() -> Exercutar uma ação em um determinado intervalo de uma vez.

let clockTimer = setInterval(updateClock, 1000)

// Controla o estado do relógio
let isPaused = false;

const toggleTimer = () => {
    isPaused = !isPaused;
        if (isPaused) {
            clearInterval(clockTimer);
            $toggleButton.text("Resumir");
            $toggleButton.css("background-color", "#ADE25D");
        } else {
            updateClock;
            clockTimer = setInterval(updateClock, 1000)
            $toggleButton.text("Pausar");
            $toggleButton.css("background-color", "rgb(6, 164, 236)");
        }
}

$toggleButton.click(toggleTimer)

