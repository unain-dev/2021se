var checkpw=0;

function checkAll() {  
var id=document.getElementById('id1').value;
var password1=document.getElementById('password1').value;
var password2=document.getElementById('password2').value;
var jname=document.getElementById('name').value;
var email=document.getElementById('email').value;

   if (checkpw!=1){
     alert("비밀번호를 검사해주세요");
     return false;
   }
  
   if (!checkExistData(id, "아이디를"))
     return false;
   if (!checkExistData(password1, "비밀번호를"))
     return false;
   if (!checkExistData(password2, "비밀번호 확인을 위해"))
     return false;
     if(password1!=password2){
        alert("비밀번호가 일치하지 않습니다");
        return false;
      }
   if (!checkExistData(jname, "이름을"))
     return false;
   if (!checkExistData(email, "이메일을"))
     return false;
   
   alert("정상적으로 가입되었습니다. 감사합니다.");
   return true;
}   



function checkExistData(value, dataName) {
    if (value == "") {
        alert(dataName + " 입력해주세요!");
        return false;
    }
    return true;
}



 function pwtest1()
{
    
    var p1=document.getElementById('password1').value;
    var password1RegExp = /^[a-zA-z0-9]{8,12}$/;
    if(! password1RegExp .test(p1))
    { 
        alert('비밀번호는 숫자와 영문자 조합으로 8~12자리를 사용해야 합니다.'); 
        return false;
    }

  
    var chk_num = p1.search(/[0-9]/g);
    var chk_eng = p1.search(/[a-z]/ig);

    if(chk_num < 0 || chk_eng < 0)

    {
        alert('비밀번호는 숫자와 영문자를 혼용하여야 합니다.');
        return false;
    }
    alert("적절한 비밀번호입니다");
    checkpw=1;
}





