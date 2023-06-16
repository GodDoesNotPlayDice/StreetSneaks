
const aSelect = document.getElementById("a-select");

function tt(element, id) {
    console.log("tt");
    modalElement = id
    console.log(id);
    aSelect.setAttribute("href", "http://127.0.0.1:8000/delete/" + id);
}