// A function that toggles a dropdown on the navbar using a specified id
function toggleDropdown(id) {
    var dropdown = document.getElementById(id);
    if (dropdown.style.display === "none") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}