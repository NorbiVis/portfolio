let searchTrigger = document.getElementById('SearchTrigger')
let searchForm = document.getElementById('SearchForm')
let menuTrigger = document.getElementById('MenuTrigger')
let menu = document.getElementById('Menu')

searchTrigger.addEventListener('click', () => {
    searchForm.classList.toggle('Active')
})

menuTrigger.addEventListener('click', () => {
    menu.classList.toggle('Active')
})