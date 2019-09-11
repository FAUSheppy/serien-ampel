function searchButton(){

}

function suggestButton(){
    filters = document.getElementsByClassName("suggest-filter")
    string  = ""

    for(i = 0; i < filters.length; i++) {
        console.log(i)
        if(filters[i].checked){
            string += filters[i].id
        }
    }

    if(string == ""){
        alert("Must select at least one filter")
    }

    window.location.href = '/suggest-results' + "?query=" + string
    console.log("done")
}
