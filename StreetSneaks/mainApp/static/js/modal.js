const deleteButtons = document.querySelectorAll('[data-modal-target="popup-modal"]');
const deleteLink = document.querySelector('#popup-modal a');

deleteButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        const productId = event.currentTarget.dataset.productId;
        deleteLink.href = `http://127.0.0.1:8000/zapatillas/delete/${productId}`;
    });
});