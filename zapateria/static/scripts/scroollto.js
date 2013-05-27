
var SC = {
  mov : [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1],
  ret : 45,
  url : (document.location.href.split('#'))[0],
  $ : function(id){var elem = document.getElementById(id);return elem;},
  ev : function(x,y,z){(document.addEventListener) ? x.addEventListener(y,z,false) : x.attachEvent('on'+y,z);},
  pD : function(x){(x.preventDefault) ? x.preventDefault() : x.returnValue = false;},
  sc : function(e){
    SC.pD(e);
    e.target ? e = e.target : e = e.srcElement;
    e.toString().match('#') ? e = e : e = e.parentNode;
    var o = 0,ID = (e.toString().split('#'))[1],y = SC.$(ID),x = 0,dir = 0,dis = 0,inc = 0;
    window.pageYOffset ? o = window.pageYOffset : o = document.documentElement.scrollTop;
    while(y){x += y.offsetTop;y = y.offsetParent;}
    (x>o) ? dir = 1 : dir = -1;
    dis = Math.abs(x-o);
    var fot = 0;
    function mover(){
      if(fot<SC.mov.length){
        setTimeout(
          function(){
            inc = Math.round((dir*(dis*(SC.mov[fot]/100))));
            o += inc;
            window.scrollTo(0,o);
            fot++;
            mover();
          }
        ,SC.ret); 
      } else {
        window.scrollTo(0,x);
        document.location.href = SC.url+'#'+ID;
        fot = 0;
      }
    }
    mover(); 
  },
  inicio : function(){
    var vs = document.getElementsByTagName('a');
    for(var i=0;i<vs.length;i++){
      if(vs[i].href.match(SC.url+'#')){
        SC.ev(vs[i],'click',SC.sc);
      } 
    }
  } 
}
 