$pause = $("#pause")
$resume = $("#resume")
$reset = $("#reset")
$number = $(".numbers")

const time = () => {
    $number.text(new Date().toLocaleTimeString())
}

const timer = () => setInterval(time, 1000)



timer()