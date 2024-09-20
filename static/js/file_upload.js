let uploadButton = document.getElementById("uploadButton");
let fileInput = document.getElementById("profilePic");
let fileInfo = document.getElementById("fileInfo");
let buttonContent = document.getElementById("buttonContent");

uploadButton.addEventListener("click", function() {
    fileInput.click();
})

fileInput.addEventListener("change", function() {
    var selectedFile = fileInput.files[0];
    if (selectedFile) {
        buttonContent.innerHTML = selectedFile.name
    }
})