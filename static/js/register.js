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
  
  // Registration Form Handling
  const registerForm = document.getElementById('registerForm');
  registerForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = registerForm['email'].value;
    const password = registerForm['password'].value;
    const confirmPassword = registerForm['confirmPassword'].value;
  
    if (password !== confirmPassword) {
      console.error('Passwords do not match');
      // You can display an error message to the user here
      return;
    }

    if (password.length < 6) {
        console.error('Password should be at least 6 characters');
        // You can display an error message to the user here
        return;
      }
  
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .then((userCredential) => {
        // User registered successfully
        const user = userCredential.user;
        console.log('User registered:', user);
  
        // Store additional user data in Firestore or Realtime Database
        const username = registerForm['username'].value;
        const dob = registerForm['dob'].value;
        // You can store the username and dob in your preferred database
  
        window.location.href = loginUrl;
      })
      .catch((error) => {
        // Handle registration error
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error('Registration error:', errorMessage);
        // You can display an error message to the user here
      });
  });