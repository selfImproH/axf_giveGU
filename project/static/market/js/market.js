$(document).ready(function(){

        var alltybtn = document.getElementById('alltypebtn')
        var showortbtn = document.getElementById('showsorbtn')
        var typediv = document.getElementById('typediv')

        var sortdiv = document.getElementById('sortdiv')

        typediv.style.display = 'none'
        sortdiv.style.display = 'none'
        alltybtn.addEventListener('click',function () {
                 console.log('------->1')
            typediv.style.display = 'block'
            sortdiv.style.display = 'none'
        },false)

       showsortbtn.addEventListener("click", function(){
               console.log('------->2')
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)
        typediv.addEventListener('click',function () {
                 console.log('------->3')
            typediv.style.display = 'none'
        },false)
        sortdiv.addEventListener('click',function () {
                console.log('------->4')
            sortdiv.style.display = 'none'
        },false)
    // - 0 + 默认点击+显示
    var subBtn = document.getElementsByClassName('subShopping')
    var addBtn = document.getElementsByClassName('addShopping')
    var num = document.getElementsByClassName('num')


})