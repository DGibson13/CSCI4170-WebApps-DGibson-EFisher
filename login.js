// JavaScript source code
 var username;
 var password;
 var login;
    function outputUserInfoAuto(){
    if (login == 1){
        document.getElementById("username").placeholder = username;
        document.getElementById("dropdownMenuButton1").innerHTML = username;
     }
     else {

     }
    }
    function outputUserInfo(){
            
     		username = document.getElementById("username").value;
            password = document.getElementById("password").value;

            document.getElementById("username").placeholder = username;
            document.getElementById("dropdownMenuButton1").innerHTML = username;
            login = 1;
		}