var res = [];
var sum = 0;
var dayofWeek = '';
var day = '';
var month = '';
var year = '';
var date = '';

var RuEngDays = {
'Mon': "Понедельник",
  'Tue': "Вторник",
  'Wed': "Среда",
  'Thu': "Четверг",
  'Fri': "Пятница",
  'Sat': "Суббота",
  'Sun': "Воскресенье",
};

function clearstr(str)
{
  str = str.replaceAll('\n', "")
  str = str.replaceAll('\t  ', "")
  str = str.replaceAll('\t', "")
  return str
}

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



  $(".addButton").click(function () {
    var $row = $(this).closest("tr");    // Find the row
    var $text = table.row($row).data()

    var selel = document.getElementById("select_"+get_id($text[6]));
    var valsel = selel.options[selel.selectedIndex].text
    //console.log(RuEngDays[dayofWeek])
    //console.log(valsel.split(' ')[0])
    if ((day !== '') && (RuEngDays[dayofWeek] === valsel.split(' ')[0]))
    {
        for (let i = 0; i < $text.length; i++)
              $text[i] = clearstr($text[i])
        var resdate = [day, month, year]
        res.push([$text[0], resdate, valsel])
        sum += parseInt($text[3])
        document.getElementById('sum').innerText = "Текущая сумма: " + sum;
        this.disabled=true

    }
    else
    {
      alert('День выбранной даты и поля со временем должен совпадать!')
    }
    //console.log($text[0])
    //location.href = "schedule_choose/" + $text[0];

  });


  $(".sendButton").click(function () {
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/excursions/watch_excursions/",
        data: {result: res,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}
      })
  })
  jQuery.datetimepicker.setLocale('ru');
  $( ".datetimepicker" ).datetimepicker({
    format:'Y/m/d',
    step:30,
    closeOnDateSelect:false,
    closeOnTimeSelect:true,
    timepicker: false,
    lang: 'ru',
    allowTimes:['9:00','12:00','15:00','19:00','21:00'],
    minDate:0.,

    onChangeDateTime: function (ct, $i)
    {
      var strdate = ct.toString();
      dayofWeek = strdate.split(' ')[0];
      month = strdate.split(' ')[1];
      day = parseInt(strdate.split(' ')[2]);
      year = parseInt(strdate.split(' ')[3]);
    },
      }
  );
// {
//         onSelect: function(date) {
//
//         }
//       }
});


