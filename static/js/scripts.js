/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


const list = document.querySelectorAll(".list li");
for(let el of list){
    el.addEventListener("click", e=>{
        e.preventDefault();
        console.log(e.currentTarget);
    })
}


// link.addEventListener("click",(e)=>{
//     e.preventDefault()
//     console.log("링크를 클릭했습니다.")
// });