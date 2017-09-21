$(document).ready(function () {
    var account = document.getElementById('accunt')
    var accunterr = document.getElementById("accunterr")//格式
    var checkerr = document.getElementById("checkerr")//账户被占用

    account.addEventListener("blur",function () {
        instr = this.value
        if(instr.length<6||instr.length>12){
            accunterr.style.display ='block'
            return
        }

        $.post('/checkuserId/',{'userid':instr},function(data) {
            if (data.status == 'error'){
                checkerr.style.display = 'block'
            }
        })
    },false)

})