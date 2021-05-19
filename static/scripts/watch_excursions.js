var res = [];
var sum = 0;

function clearstr(str)
{
  str = str.replaceAll('\n', "")
  str = str.replaceAll('\t  ', "")
  str = str.replaceAll('\t', "")
  return str
}

//sum.innerText = "Aboba"

$(document).ready(function() {
  var table = $('#myTable').DataTable();

  $(".addButton").click(function () {
    var $row = $(this).closest("tr");    // Find the row
    var $text = table.row($row).data()
    $text.pop()
    for (let i = 0; i < $text.length; i++)
      $text[i] = clearstr($text[i])
    res.push($text)
    sum += parseInt($text[3])
    document.getElementById('sum').innerText = "Текущая сумма: " + sum;
    this.disabled=true
  });


  $(".sendButton").click(function () {
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/excursions/watch_excursions/",
        data: {result: res,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}
      })
  })

});


