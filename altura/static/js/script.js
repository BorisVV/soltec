
function cookiehintfadeOut(el){
  el.style.opacity = 1;

  (function fade() {
    if ((el.style.opacity -= .1) < 0) {
      el.style.display = "none";
    } else {
      requestAnimationFrame(fade);
    }
  })();
}  
	
window.addEventListener('load',	
	function () {
		document.getElementById('cookiehintsubmit').addEventListener('click', function (e) {
			e.preventDefault();
			document.cookie = 'reDimCookieHint=1; expires=Sat, 07 Sep 2019 23:59:59 GMT;57; path=/';
			cookiehintfadeOut(document.getElementById('redim-cookiehint'));
			return false;
		},false);
				document.getElementById('cookiehintsubmitno').addEventListener('click', function (e) {
			e.preventDefault();
			document.cookie = 'reDimCookieHint=-1; expires=0; path=/';
			cookiehintfadeOut(document.getElementById('redim-cookiehint'));
			return false;
		},false);		
			}
);
