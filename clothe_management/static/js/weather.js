$(document).ready(function() {
  let weatherIcon = {
    '01' : 'fas fa-sun fa-2xl',
    '02' : 'fas fa-cloud-sun fa-2xl',
    '03' : 'fas fa-cloud fa-2xl',
    '04' : 'fas fa-cloud-meatball fa-2xl',
    '09' : 'fas fa-cloud-sun-rain fa-2xl',
    '10' : 'fas fa-cloud-showers-heavy fa-2xl',
    '11' : 'fas fa-poo-storm fa-2xl',
    '13' : 'far fa-snowflake fa-2xl',
    '50' : 'fas fa-smog fa-2xl'
  };

$.ajax({

  
url:'https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=a99a1b7720bd33ed7901198df53a2096&units=metric',

dataType:'json',
type:'GET',
success:function(data){
  var $Icon = (data.weather[0].icon).substr(0,2);
  var $Temp = Math.floor(data.main.temp) + 'º';
  var $city = data.name;

  $('.CurrIcon').append('<i class="' + weatherIcon[$Icon]+'"></i>');
  $('.CurrTemp').prepend($Temp);
  $('.City').append($city);

  let today = new Date();
  let year = today.getFullYear();
  let month = today.getMonth()+1;
  let date = today.getDate();

  const weekday = ['일','월','화','수','목','금','토'];
  let day = weekday[today.getDay()];

  var $today_write = year+'.'+month+'.'+date+'('+day+')';
  $('.today_date').append($today_write);

  loadSet($Icon);

  }
})

}
);

function loadSet($Icon){
  var todayweather;

  if($Icon=='01'){
  document.getElementById("weather_logo").src="../static/img/w0102.png";
  todayweather="화창한 날씨";
  }
  else if($Icon=='02'){
      document.getElementById("weather_logo").src="../static/img/w0102.png";
      todayweather="화창하지만 구름 살짝 있는 날씨";
  }
  else if($Icon=='03'){
      document.getElementById("weather_logo").src="../static/img/w0304.png";
      todayweather="살짝 흐린 날씨";
      document.getElementById("wicon").back;
  }
  else if($Icon=='04'){
      document.getElementById("weather_logo").src="../static/img/w0304.png";
      todayweather="흐린 날씨";
  }
  else if($Icon=='09'){
      document.getElementById("weather_logo").src="../static/img/w0910.png";
      todayweather="부슬비 내리는 날씨";
  }
  else if($Icon=='10'){
      document.getElementById("weather_logo").src="../static/img/w0910.png";
      todayweather="비가 많이 오는 날씨";
  }
  else if($Icon=='11'){
      document.getElementById("weather_logo").src="../static/img/w1113.png";
      todayweather="폭풍이 치는 날씨";
  }
  else if($Icon=='13'){
      document.getElementById("weather_logo").src="../static/img/w1113.png";
      todayweather="눈오는 날씨";
  }
  else if($Icon=='50'){
      document.getElementById("weather_logo").src="../static/img/w50.png";
      todayweather="안개가 자욱한 날씨";
  }

  document.getElementById("todayweather").append('"'+todayweather+'"');

}
