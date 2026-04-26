function Menu(){
    const menu=document.querySelector('#menu')
    const listnav=document.querySelector('ul')
    const closed=document.querySelector('#closed')
    const header=document.querySelector('header')
    menu.addEventListener('click',()=>{
        listnav.classList.toggle('ul_active')
        header.classList.toggle('header_active')
        closed.classList.add('closed_appear')
        
    })
}
Menu()

function LoadingAnimation(){
    const loadingBox=document.querySelector('.loading')
    window.addEventListener('load',()=>{
        setTimeout(() => {
            loadingBox.classList.add('loadingEnd')
        }, 2000);
    })
}
LoadingAnimation()

function login_register(){
    const formafter_a=document.querySelector('form_after a')    
    const formafter=document.querySelector(".form_after")
    formafter_a.addEventListener("click",()=>{
        formafter.classList.add('form_after_active')
    })

}