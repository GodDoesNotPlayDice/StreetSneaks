const fileInput = document.getElementById('formFile');
const imgPreview = document.querySelector('.content__img');

fileInput.addEventListener('change', function() {
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', function() {
        imgPreview.src = reader.result;
    });

    if (file) {
        reader.readAsDataURL(file);
    }
});