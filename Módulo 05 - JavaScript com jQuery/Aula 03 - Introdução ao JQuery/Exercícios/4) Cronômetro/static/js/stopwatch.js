$pause = $("#pause")
$resume = $("#resume")
$reset = $("#reset")
$number = $(".numbers")

const timer = () => {
    $number.text(new Date(0,0).toLocaleTimeString())
}

timer()