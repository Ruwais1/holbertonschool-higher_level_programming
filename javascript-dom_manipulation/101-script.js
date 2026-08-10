document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.querySelector('#btn_translate');
  
  btnTranslate.addEventListener('click', function () {
    const langCode = document.querySelector('#language_code').value;
    
    fetch(`https://hellosalut.stefanbohacek.com/?lang=${langCode}`)
      .then(response => response.json())
      .then(data => {
        document.querySelector('#hello').textContent = data.hello;
      });
  });
});
