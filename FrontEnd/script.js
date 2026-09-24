/*
const password = document.querySelector("#password");
const button = document.querySelector("#toggleButton");

button.addEventListener("click", function() {
    if (password.type === "password") {
        password.type = "text";
        button.textContent = "Hide password";
    } else {
        password.type = "password";
        button.textContent = "Show password";
    }
})
*/

const input = document.querySelector("orderTotal");

const button = document.querySelectorAll("checkDelivery");

const message = document.querySelector("deliveryMessage");

button.addEventListener("click", function() {
    const enterValue = input.value.trim();
    const total = Number(enterValue);

    if (enterValue === "" || !Number.isFinite(total) || total < 0) {
        
    }
})
