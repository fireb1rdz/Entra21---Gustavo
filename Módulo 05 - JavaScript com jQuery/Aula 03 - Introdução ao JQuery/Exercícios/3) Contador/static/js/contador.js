$buttonMinus = $("#minus")
$buttonPlus = $("#plus")
$counter = $("#counter")

let accumulator = 0

const plus = () => {
    accumulator += 1
    $counter.text(accumulator)
}

const minus = () => {
    accumulator -= 1
    $counter.text(accumulator)
}

$buttonPlus.click(plus)
$buttonMinus.click(minus)