let dropdownToggle = document.getElementById('dropdownToggle');
let dropdownMenu = document.getElementById('dropdownMenu');


let entObj = document.getElementById('ent')
let invObj = document.getElementById('inv')
let conObj = document.getElementById('con')

let dropdownValue = document.getElementById('dropdownValue');

let uploadButton = document.getElementById("uploadButton");
let fileInput = document.getElementById("profilePic");
let fileInfo = document.getElementById("fileInfo");
let buttonContent = document.getElementById("buttonContent");

function handleClick() {
    if (dropdownMenu.className.includes('block')) {
        dropdownMenu.classList.add('hidden')
        dropdownMenu.classList.remove('block')
    } else {
        dropdownMenu.classList.add('block')
        dropdownMenu.classList.remove('hidden')
    }
}

entObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = entObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'ent'
})

invObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = invObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'inv'

})

conObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = conObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'con'
})

dropdownToggle.addEventListener('click', handleClick);

uploadButton.addEventListener("click", function() {
    fileInput.click();
})

fileInput.addEventListener("change", function() {
    var selectedFile = fileInput.files[0];
    if (selectedFile) {
        buttonContent.innerHTML = selectedFile.name
    }
})