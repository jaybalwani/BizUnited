let dropdownToggle = document.getElementById('dropdownToggle');
let dropdownMenu = document.getElementById('dropdownMenu');
let dropdownValue = document.getElementById('dropdownValue')

let noneObj = document.getElementById('none')
let psObj = document.getElementById('pre_seed')
let sObj = document.getElementById('seed')
let saObj = document.getElementById('series_a')
let sbObj = document.getElementById('series_b')
let scObj = document.getElementById('series_c')
let sdObj = document.getElementById('series_d')

let submit = document.getElementById('submit')
onboardForm = document.getElementById('onboardForm')

function handleClick() {
    if (dropdownMenu.className.includes('block')) {
        dropdownMenu.classList.add('hidden')
        dropdownMenu.classList.remove('block')
    } else {
        dropdownMenu.classList.add('block')
        dropdownMenu.classList.remove('hidden')
    }
}


dropdownToggle.addEventListener('click', handleClick);

noneObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = noneObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'none'
})
psObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = psObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'pre_seed'
})
sObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = sObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'seed'
})
saObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = saObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'series_a'
})
sbObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = sbObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'series_b'
})
scObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = scObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'series_c'
})
sdObj.addEventListener('click', ()=>{
    dropdownToggle.innerHTML = sdObj.innerHTML
    dropdownMenu.classList.add('hidden')
    dropdownMenu.classList.remove('block')

    dropdownValue.value = 'series_d'
})

submit.addEventListener('click', () => {
    onboardForm.submit()
    console.log('YO')
})