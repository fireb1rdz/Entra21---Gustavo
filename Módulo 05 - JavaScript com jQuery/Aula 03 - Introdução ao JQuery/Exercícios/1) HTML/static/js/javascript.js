$button = $("#clicker")
$p = $("#secret")

isShown = false

showInfo = () => {
    isShown = !isShown
    if (isShown) {
        $button.text("Esconder!")
        $p.css("display", "flex")
    } else {
        $button.text("Revelar!")
        $p.css("display", "none")
    }
}
$button.click(showInfo)