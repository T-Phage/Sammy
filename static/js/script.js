//*************************************************
//Upload modal script
//*************************************************

function setFileName(name)
      {
        document.getElementById('file').innerHTML = name;

        var img = new RegExp(".png|.jpeg|.jpg|.jpe|.jif|.jfif|.jfi|.webp|.raw|.arw|.cr2|.nrw|.k25|.bmp|.psd|.svg|.tiff|.tif|.gif$|.svg|.svgz");
        var doc = new RegExp(".docx|.doc|.txt|.odt$")
        var html = new RegExp(".htm|.html|.mhtml$")
        var pdf = new RegExp(".pdf$")
        var audio = new RegExp(".mp3|.wav|.wma|.wv|.amr$")
        var power = new RegExp(".ppt|.pptx|.xps|.pptm$")

        if (img.test(name)) {
          document.getElementById('img').style.display = "block";
          document.getElementById('docs').style.display = "none";
          document.getElementById('html').style.display = "none";
          document.getElementById('pdf').style.display = "none";
          document.getElementById('aud').style.display = "none";
          document.getElementById('pow').style.display = "none";
          document.getElementById('def').style.display = "none";
        }
        else if(doc.test(name)) {
          document.getElementById('docs').style.display = "block";
          document.getElementById('html').style.display = "none";
          document.getElementById('img').style.display = "none";
          document.getElementById('pdf').style.display = "none";
          document.getElementById('aud').style.display = "none";
          document.getElementById('pow').style.display = "none";
          document.getElementById('def').style.display = "none";
        }
        else if(html.test(name)){
          document.getElementById('html').style.display = "block";
          document.getElementById('docs').style.display = "none";
          document.getElementById('img').style.display = "none";
          document.getElementById('pdf').style.display = "none";
          document.getElementById('aud').style.display = "none";
          document.getElementById('pow').style.display = "none";
          document.getElementById('def').style.display = "none";
        }
        else if(pdf.test(name)){
          document.getElementById('pdf').style.display = "block";
          document.getElementById('html').style.display = "none";
          document.getElementById('docs').style.display = "none";
          document.getElementById('img').style.display = "none";
          document.getElementById('aud').style.display = "none";
          document.getElementById('pow').style.display = "none";
          document.getElementById('def').style.display = "none";
        }
        else if(audio.test(name)){
          document.getElementById('aud').style.display = "block";
          document.getElementById('pow').style.display = "none";
          document.getElementById('pdf').style.display = "none";
          document.getElementById('html').style.display = "none";
          document.getElementById('docs').style.display = "none";
          document.getElementById('img').style.display = "none";
          document.getElementById('def').style.display = "none"
        }
        else if(power.test(name)){
          document.getElementById('pow').style.display = "block";
          document.getElementById('aud').style.display = "none";
          document.getElementById('pdf').style.display = "none";
          document.getElementById('html').style.display = "none";
          document.getElementById('docs').style.display = "none";
          document.getElementById('img').style.display = "none";
          document.getElementById('def').style.display = "none";
        }
        else {
          document.getElementById('def').style.display = "block"
          document.getElementById('pow').style.display = "none";
          document.getElementById('aud').style.display = "none";
          document.getElementById('pdf').style.display = "none";
          document.getElementById('html').style.display = "none";
          document.getElementById('docs').style.display = "none";
          document.getElementById('img').style.display = "none";
        }
      }

//******************************************************************
// Chane default labels for the cmodal inputs
//*****************************************************************
//var el = document.getElementsByTagName ('label');
//for(var x=0; x<el.length; x++)
//{
//    el[x].style.display = "none";
//}

