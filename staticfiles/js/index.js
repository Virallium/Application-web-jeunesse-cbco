function activerLecteur(conteneur){
    const origine=window.location.origin;
    const VideoId=conteneur.getAttribute('data-id')
    const lecture=document.createElement('iframe')
    lecture.setAttribute('src',`https://www.youtube.com/embed/${VideoId}?autoplay=1&rel=0&origin=${origine}`)
    lecture.setAttribute('frameborder','0')
    lecture.setAttribute('allow','accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture')
    lecture.style.width="100%"
    lecture.style.height="100%"
    conteneur.innerHTML=''
    conteneur.appendChild(lecture)
}