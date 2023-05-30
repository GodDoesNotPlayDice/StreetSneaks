const fileInput = document.getElementById('file_input');
const imgPreview = document.querySelector('.preview');

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