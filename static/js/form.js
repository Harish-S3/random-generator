const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");

signupBtn.onclick = () => {
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
};

loginBtn.onclick = () => {
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
};

signupLink.onclick = () => {
  signupBtn.click();
  return false;
};

document.getElementById('signupForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form from submitting normally
  let username = document.getElementById('signupUsername').value;
  let password = document.getElementById('signupPassword').value;
  let confirmPassword = document.getElementById('confirmPassword').value;

  // Check if passwords match
  if (password !== confirmPassword) {
    alert("Passwords do not match.");
    return;
  }

  // Save username and password to sessionStorage
  sessionStorage.setItem('username', username);
  sessionStorage.setItem('password', password); // Note: Storing passwords in plain text is not secure

  alert('Sign-up successful. You can now log in.');
   // Toggle back to the login form
   document.querySelector('label.login').click();
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form from submitting normally
  let loginUsername = document.getElementById('loginUsername').value;
  let loginPassword = document.getElementById('loginPassword').value;

  // Retrieve username and password from sessionStorage
  let storedUsername = sessionStorage.getItem('username');
  let storedPassword = sessionStorage.getItem('password');

  // Check if entered credentials match stored credentials
  if (loginUsername === storedUsername && loginPassword === storedPassword) {
    alert('Login successful.');
    window.location.href = homePageUrl;
  } else {
    alert('Invalid username or password.');
  }
});
