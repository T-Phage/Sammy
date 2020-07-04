
//*********************************
 //mysite icons script
 //***********************************
function myFunction() {

  var img = new RegExp(".png|.jpeg|.jpg|.jpe|.jif|.jfif|.jfi|.webp|.raw|.arw|.cr2|.nrw|.k25|.bmp|.psd|.svg|.tiff|.tif|.gif$|.svg|.svgz");
  var doc = new RegExp(".docx|.doc|.txt|.odt$");
  var html = new RegExp(".htm|.html|.mhtml$");
  var pdf = new RegExp(".pdf$");
  var audio = new RegExp(".mp3|.wav|.wma|.wv|.amr$");
  var power = new RegExp(".ppt|.pptx|.xps|.pptm$");

  // var fs = document.getElementById('id_filepath').innerHTML;
  var h = document.getElementsByClassName('filename');
  //fs = h.innerText
  for (var i=0; i<h.length; i++)
  {
      //console.log(document.getElementsByClassName('img_doc')[i].src);
      if (doc.test(h[i].innerText)) {
          document.getElementsByClassName('img_doc')[i].src = "/static/images/fileicons/docs.png"
          }
      else if(pdf.test(h[i].innerText)){
          document.getElementsByClassName('img_doc')[i].src = "/static/images/fileicons/pdficon.png"
          }
      else if(html.test(h[i].innerText)){
          document.getElementsByClassName('img_doc')[i].src = "/static/images/fileicons/htmlicon.png"
      }
      else if(audio.test(h[i].innerText)){
          document.getElementsByClassName('img_doc')[i].src = "/static/images/fileicons/audioicon.jpeg"
      }
      else if(img.test(h[i].innerText)){
        document.getElementsByClassName('img_doc')[i].src = "/static/images/fileicons/imageicon.png"
      }
      else if(power.test(h[i].innerText)){
          document.getElementsByClassName('img_doc')[i].src = "/static/images/fileicons/powicon.jpeg"
      }
      else {
          document.getElementsByClassName('img_doc')[i].src = "/static/images/fileicons/deficon.png"
      }
  }

};

//*************************************************
//Upload modal script
//*************************************************

function setFileName(name)
      {
        document.getElementById('file').innerHTML = name;
        // dept_id = sessionStorage.getItem('dept_id');
        // document.getElementById('id_department').value = dept_id;;
        
        // console.log(document.getElementById('id_uploaded_by'));
        // for(var i=0; i<document.getElementById('id_uploaded_by').options.length; i++)
        // {
        //   if (document.getElementById('id_uploaded_by').options[i].label === sessionStorage.getItem('username'))
        //     document.getElementById('id_uploaded_by').value = document.getElementById('id_uploaded_by').options[i].value;
        // }

        var img = new RegExp(".png|.jpeg|.jpg|.jpe|.jif|.jfif|.jfi|.webp|.raw|.arw|.cr2|.nrw|.k25|.bmp|.psd|.svg|.tiff|.tif|.gif$|.svg|.svgz$");
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
      };

/**************************************************
Sitemodal scripts
******************************************************/
// $(document).ready(function(){
   $("#id_site_name").keyup(function(){
    $('#id_site_id')[0].value=$('#id_site_name').val().toLowerCase();

      // Replace whitepsaces with "-"
      var replaceSpace = $(this).val();
      var result = replaceSpace.replace(/ /g, "-");
      document.getElementById("id_site_id").value = result;
  });
//  });