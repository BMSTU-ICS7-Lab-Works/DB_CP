var res = [];

$(document).ready(function() {
  $(".addButton").click(function () {
    // var $item = $(this).closest("tr")   // Finds the closest row <tr>
    //     .find(".nr")     // Gets a descendent with class="nr"
    //     .text();         // Retrieves the text within <td>
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.text(); // Find the text
    res.push($text)
    alert($text);
    // $("#resultas").append($item);       // Outputs the answer
  });

  $('#myTable').DataTable();

  $(".sendButton").click(function () {
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/excursions/watch_excursions/",
        data: {result: res,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}
      })
  })



    // $('.sendButton').click(function () {
    //     $.post("http://127.0.0.1:8000/excursions/watch_excursions/",
    //         res)
    // });
});


