
// Алгоритм кнопки "Добавить новость" 
async function add_news(){  
  let form = document.querySelector('.addNews__form')

  let token_value = document.querySelector('[name=csrfmiddlewaretoken]').value
  let url = window.location.href
  let response = await fetch(url, {
    method: 'post',
    headers: {
      'X-CSRFToken': token_value
    },
    body: new FormData(form)
  })
  response = await response.text()
  if (response == 'OK'){
    console.log('data has been sent')
  }
  location.reload()
}

let button_add_news = document.querySelector('.addNews')
let addNews_submit = document.querySelector('.addNews__submit')

addNews_submit.addEventListener('click', (event) => {
  event.preventDefault()
  add_news()
})
button_add_news.addEventListener('click', (event) => {
  console.log('Click')
  let addNews_form = document.querySelector('.addNews__form')
  addNews_form.classList.toggle('addNews__form_open')
})