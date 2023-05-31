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

const fileInput1 = document.getElementById('file_input1');
const imgPreview1 = document.querySelector('.preview1');

fileInput1.addEventListener('change', function() {
    const file = fileInput1.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', function() {
        imgPreview1.src = reader.result;
    });

    if (file) {
        reader.readAsDataURL(file);
    }
});

const fileInput2 = document.getElementById('file_input2');
const imgPreview2 = document.querySelector('.preview2');

fileInput2.addEventListener('change', function() {
    const file = fileInput2.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', function() {
        imgPreview2.src = reader.result;
    });

    if (file) {
        reader.readAsDataURL(file);
    }
});