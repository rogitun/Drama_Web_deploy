
let searchForm = document.getElementById('searchForm')
//검색 폼
console.log(`searchform ==> ${searchForm}`)
let pageLink = document.getElementsByClassName('page-link') // 버튼
console.log(`pageLink ==> ${pageLink}`)

for(let j = 0;j<searchForm.length;j++){
    console.log(`SearchForm-j ==> ${searchForm[j]}`)
}



if (searchForm) {
    for (let i = 0; i < pageLink.length; i++) {
        console.log(`pg-i ==> ${pageLink[i]}`)
        pageLink[i].addEventListener('click', function (event) {
            event.preventDefault()

            let page = this.dataset.pag
          
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            
            searchForm.submit()
        })
    }

}

