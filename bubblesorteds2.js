
function checkInt(x) {
  var val = parseInt(x);
  if (isNaN(val)) {
    return false;
  }
  else {
    return true;
  }
}

function bubbleSort(n,dir) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("myTable");
  switching = true;
  //Set the sorting direction to ascending:
  rows = table.getElementsByTagName("TR");
  len = rows.length;
  while (switching) {
    switching = false;
    for (var i=1;i<(len-1);i++) {
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (checkInt(x.innerHTML)) {
        if (dir == 0) {
          if (parseInt(x.innerHTML) >parseInt(y.innerHTML)) {
            //if so, mark as a switch and break the loop:
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
          }
        }
        else if (dir == 1) {
          if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
            //if so, mark as a switch and break the loop:
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
          }
        }
      }
      else {
        if (dir == 0) {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            //if so, mark as a switch and break the loop:
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
          }
        }
        else if (dir == 1) {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            //if so, mark as a switch and break the loop:
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
          }
        }
      }
    }
  }
}
