var zzz_ndn=(()=>{function n(t,e,n){var r=new Date,n=(r.setTime(r.getTime()+24*n*60*60*1e3),"expires="+r.toUTCString()),r=window.location.hostname;document.cookie=t+"="+e+";"+n+";domain="+r+";path=/"}function r(t){var n=t+"=";let r=[""];try{var e=decodeURIComponent(document.cookie);r=e.split(";")}catch(t){return""}for(let e=0;e<r.length;e++){let t=r[e];for(;" "==t.charAt(0);)t=t.substring(1);if(0==t.indexOf(n))return t.substring(n.length,t.length)}return""}function o(t,e){try{localStorage.setItem(t,e)}catch(t){}}function t(){var t="ndn",e=r(t);return""!=e?(n(t,e,365),o(t,e)):""!=(e=function(t){let e="";try{e=localStorage.getItem(t)||""}catch(t){}finally{return e}}(t))?n(t,e,365):(n(t,""!=(e=r("BCSessionID"))?e:e=function(){var t=new Date;let e="",n="undefined"==typeof crypto?t=>Math.floor(16*Math.random()).toString(16):t=>(Number(t)^crypto.getRandomValues(new Uint8Array(1))[0]&15>>Number(t)/4).toString(16);try{e=(String(1e7)+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g,t=>n(t))+-t.getTime()}catch(t){}return e}(),365),o(t,e)),e}try{return t()}catch{return-999}})();