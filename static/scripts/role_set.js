function get_id(str)
{
  var num = '';
  for (let i = 0; i < str.length; i++)
  {
    if (str[i]==='_')
    {
      for (let j = i+1; j < str.length; j++) {
        if ('0'<str[j]<'9')
        {
          num += str[j];
        }
        else{
          break;
        }
        break;
      }
    }
  }
  return parseInt(num)
}

$(document).ready(function() {
    var table = $('#myTable').DataTable();

    $(".setButton").click(function () {
    var $row = $(this).closest("tr");    // Find the row
    var $text = table.row($row).data();
    var username = $text[0];
    var selel = document.getElementById("select_"+get_id($text[2]));
    var valsel = selel.options[selel.selectedIndex].text
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/accounts/set/role",
        data: {newrole: valsel,
            username: username,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}
      })

  });
})