const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const usernameError = document.getElementById("usernameError");
const passwordError = document.getElementById("passwordError");

function validateUsername() {
    const username = usernameInput.value;
    const usernameRegex = /^[a-zA-Z0-9.]+$/;

    if (!usernameRegex.test(username)) {
        usernameError.textContent = "Username should contain only letters, numbers, and dots.";
    } else {
        usernameError.textContent = "";
    }
}

function validatePassword() {
    const password = passwordInput.value;
    const passwordRegex = /^(?=.*[A-Z]).{8,}$/;

    if (!passwordRegex.test(password)) {
        passwordError.textContent = "Password should be at least 8 characters long and start with a capital letter.";
    } else {
        passwordError.textContent = "";
    }
}

usernameInput.addEventListener("input", validateUsername);
passwordInput.addEventListener("input", validatePassword);