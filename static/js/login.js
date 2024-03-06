const firebaseConfig = {
  apiKey: "AIzaSyBRSEIAjAOpEZIN0UKf9tDDb91YARFvWD0",
  authDomain: "random-gen-login.firebaseapp.com",
  databaseURL: "https://random-gen-login-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "random-gen-login",
  storageBucket: "random-gen-login.appspot.com",
  messagingSenderId: "56481594795",
  appId: "1:56481594795:web:68f267068bc221a595e6ee"
};
firebase.initializeApp(firebaseConfig);

// Login Form Handling
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = loginForm['email'].value;
  const password = loginForm['password'].value;

  firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // User logged in successfully
      const user = userCredential.user;
      console.log('User logged in:', user);
      // Redirect to home.html
      window.location.href = homePageUrl;
    })
    .catch((error) => {
      // Handle login error
      const errorCode = error.code;
      const errorMessage = error.message;
      console.error('Login error:', errorMessage);
      // Display an error message to the user
      alert('User not found. Please check your credentials.');
    });
});