var res = [];


function clearstr(str)
{
  str = str.replaceAll('\n', "")
  str = str.replaceAll('\t  ', "")
  str = str.replaceAll('\t', "")
  return str
}



$(document).ready(function() {
  var table = $('#myTable').DataTable();
  var excursion_name = document.getElementById('excursion_name').innerText;

  $(".addButton").click(function () {
    var $row = $(this).closest("tr");    // Find the row
    var $text = table.row($row).data()
    $text.pop()
    for (let i = 0; i < $text.length; i++)
      $text[i] = clearstr($text[i])
    res.push($text)
    this.disabled=true
  });


  $(".sendButton").click(function () {
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/excursions/create_excursion/sight_add/" + excursion_name,
        data: {result: res,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}
      })

  })

});


