
var dept = document.getElementById('path').innerText.substring(17).replace('/','')

sessionStorage.setItem('dept_id', dept);
var fac = document.getElementById('path').innerText.substring(14).replace('/','')

sessionStorage.setItem('faculty', fac);
// sessionStorage.setItem('faculty_id',document.getElementById('path').innerText).substring(14).replace('/','');
// var dep_id = sessionStorage.getItem('dept_id');
// var fac_id = sessionStorage.getItem('faculty_id');
// document.getElementById('id_department').value = dep_id;
// document.getElementById('id_faculty').value = fac_id;
