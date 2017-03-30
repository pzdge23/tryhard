var listItems = document.getElementsById("sake").getElementsByTagName("input");
total = 0;
for(i=0;i<listItems.length;i++)
{
  total = listItems[i];
}
// document.getElementById('total_ex').innerHtml = total;

function jsFunction() {
  alert(total)
}
