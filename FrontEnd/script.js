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
/*
const input = document.querySelector("orderTotal");

const button = document.querySelectorAll("checkDelivery");

const message = document.querySelector("deliveryMessage");

button.addEventListener("click", function() {
    const enterValue = input.value.trim();
    const total = Number(enterValue);

    if (enterValue === "" || !Number.isFinite(total) || total < 0) {
        message.textContent = "Please enter a valid total.";
        message.style.color = "red";
    } else if (total >= 50) {
        message.textContent = "You colify for free delivery!";
        message.style.color = "green";
    } else {
        const remaining = 50 - total;

        message.textContent =
        `Spend ${remaining.toFixed(2)} more for free delivery.`;

        message.style.color = "blue";
    }
})*/

/*
const products = [
    {name: "Keyboard", price: 25, inStock: true},
    {name: "Mouse", price: 15, inStock: false},
    {name: "Monitor", price: 123, inStock: true}
];

const list = document.querySelector("#productsList");

for (const product of products) {
    const item = document.createElement("li");

    if (product.inStock) {
        item.textContent = `${product.name} - £${product.price} - Available`;

        item.style.color = "white";
    } else {
        item.textContent = `${product.name} - Sold out`;

        item.style.color = "red";
    }

    list.appendChild(item);

}
*/

/*
const button = document.querySelector("#showButton");
const list = document.querySelector("#numberList");

button.addEventListener("click", function(){
    list.replaceChildren();

    for (let number = 1; number <= 6; number++) {
      const item = document.createElement("li");

      if (number % 2 === 0) {
         item.textContent = `${number} - Even`;
         item.classList.add("even");
         item.style.color = "blue"
      } else {
        item.textContent = `${number} - Odd`;
        item.classList.add("odd");
        item.style.color = "red"
      }

      list.appendChild(item);
    }
});
*/

