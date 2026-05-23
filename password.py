<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title> Password Strength Analyzer </title>

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      font-family: 'Poppins', sans-serif;
    }

    body{
      height:100vh;
      display:flex;
      justify-content:center;
      align-items:center;
      background: linear-gradient(135deg,#141e30,#243b55);
    }

    .container{
      width:400px;
      background:white;
      padding:35px;
      border-radius:20px;
      box-shadow:0 10px 30px rgba(0,0,0,0.3);
      text-align:center;
      animation:fadeIn 1s ease;
    }

    @keyframes fadeIn{
      from{
        opacity:0;
        transform:translateY(20px);
      }
      to{
        opacity:1;
        transform:translateY(0);
      }
    }

    h1{
      color:#243b55;
      margin-bottom:10px;
    }

    p{
      color:#666;
      margin-bottom:20px;
      font-size:14px;
    }

    .input-box{
      position:relative;
    }

    input{
      width:100%;
      padding:14px;
      border:2px solid #ccc;
      border-radius:12px;
      outline:none;
      font-size:16px;
      transition:0.3s;
    }

    input:focus{
      border-color:#243b55;
    }

    .strength-bar{
      height:12px;
      width:100%;
      background:#ddd;
      border-radius:10px;
      margin-top:20px;
      overflow:hidden;
    }

    .strength-fill{
      height:100%;
      width:0%;
      transition:0.5s;
      border-radius:10px;
    }

    .message{
      margin-top:15px;
      font-size:18px;
      font-weight:bold;
    }

    .tips{
      margin-top:20px;
      text-align:left;
      font-size:14px;
      color:#444;
      line-height:1.8;
    }

    .suggestion{
      margin-top:15px;
      padding:10px;
      background:#f1f5ff;
      border-radius:10px;
      color:#243b55;
      font-weight:600;
    }

  </style>
</head>

<body>

  <div class="container">
    <h1>Password Strength Analyzer</h1>
    <p>Check your password security instantly 🔐</p>

    <div class="input-box">
      <input type="password" id="password" placeholder="Enter your password" onkeyup="checkStrength()">
    </div>

    <div class="strength-bar">
      <div class="strength-fill" id="strengthFill"></div>
    </div>

    <div class="message" id="message"></div>

    <div class="suggestion" id="suggestion">
      Suggestion will appear here...
    </div>

    <div class="tips">
      <h3>Strong Password Tips:</h3>
      ✔ Use uppercase letters<br>
      ✔ Add numbers and symbols<br>
      ✔ Minimum 8 characters<br>
      ✔ Avoid common passwords
    </div>
  </div>

  <script>
    function checkStrength(){

      let password = document.getElementById("password").value;
      let strengthFill = document.getElementById("strengthFill");
      let message = document.getElementById("message");
      let suggestion = document.getElementById("suggestion");

      let strength = 0;

      if(password.length >= 8){
        strength++;
      }

      if(/[A-Z]/.test(password)){
        strength++;
      }

      if(/[0-9]/.test(password)){
        strength++;
      }

      if(/[!@#$%^&*]/.test(password)){
        strength++;
      }

      if(strength == 1){
        strengthFill.style.width = "25%";
        strengthFill.style.background = "red";
        message.innerHTML = "Weak Password ❌";
        message.style.color = "red";
        suggestion.innerHTML = "Try adding uppercase letters, numbers, and symbols.";
      }

      else if(strength == 2){
        strengthFill.style.width = "50%";
        strengthFill.style.background = "orange";
        message.innerHTML = "Medium Password ⚠";
        message.style.color = "orange";
        suggestion.innerHTML = "Add special characters for better security.";
      }

      else if(strength == 3){
        strengthFill.style.width = "75%";
        strengthFill.style.background = "#00b894";
        message.innerHTML = "Good Password 👍";
        message.style.color = "#00b894";
        suggestion.innerHTML = "Almost strong! Increase password length.";
      }

      else if(strength == 4){
        strengthFill.style.width = "100%";
        strengthFill.style.background = "green";
        message.innerHTML = "Strong Password 🔥";
        message.style.color = "green";
        suggestion.innerHTML = "Excellent! Your password is highly secure.";
      }

      else{
        strengthFill.style.width = "0%";
        message.innerHTML = "";
        suggestion.innerHTML = "Suggestion will appear here...";
      }
    }
  </script>

</body>
</html>
