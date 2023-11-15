$(document).ready(() => {
    const $cardsContainer = $("#cardsContainer")
    const $form = $("#searchForm")
    const $characterNameInput = $("#characterNameInput")
    const $formSubmitButton = $("#formSubmitButton")
    
    $form.validate({
        submitHandler: (form, event) => {
            event.preventDefault();
        }
    })

    let firstCharacter = true
    let previousCharacter = ""

    $form.on("submit", function () {
        $cardsContainer.empty()
        let currentCharacter = $characterNameInput.val()

        fetch(`https://rickandmortyapi.com/api/character/?name=${$characterNameInput.val()}`)
            .then(res => res.json())
            .then(data => {
                resultados = data.results
                resultados.forEach(element => {
                    $newCard = $("<div></div>").addClass("card m-2").css("width", "18rem")
                    $cardImage = $(`<img src="${element.image}"></img>`).addClass("card-img-top")
                    $cardBody = $("<div></div>").addClass("card-body")
                    $cardTitle = $("<h5></h5>").addClass("card-title").text(element.name)
                    $cardText = $("<p></p>").addClass("card-text").text(`Espécie: ${element.species} / Gênero: ${(element.gender === "Male") ? "masculino" : "feminino" }`)
    
                    $cardBody.append($cardTitle, $cardText)
                    $newCard.append($cardImage, $cardBody)
                    $cardsContainer.append($newCard)
                });
            })
            .finally(() => {
            })

    })
})