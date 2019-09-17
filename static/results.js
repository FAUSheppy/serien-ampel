function unfoldElement(elementID){
    targetFold = document.getElementById("fold-" + elementID)
    if(targetFold.style.display == "none")
        targetFold.style.display = "block"
    else
        targetFold.style.display = "none"
}
