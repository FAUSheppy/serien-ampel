function searchButton(){
    string = document.getElementById("search-field").value
    if(string == ""){
        alert("Must input some text")
        return
    }

    window.location.href = '/search-results' + "?query=" + string

}

function suggestButton(){
    filters = document.getElementsByClassName("suggest-filter")
    string  = ""

    for(i = 0; i < filters.length; i++) {
        console.log(i)
        if(filters[i].checked){
            string += filters[i].id + ","
        }
    }

    if(string == ""){
        alert("Must select at least one filter")
        return
    }

    window.location.href = '/suggest-results' + "?query=" + string
    console.log("done")
}

function unfoldElement(elementID){
    targetFold = document.getElementById("fold-" + elementID)
    if(targetFold.style.display == "none")
        targetFold.style.display = "block"
    else
         targetFold.style.display = "none"
}
