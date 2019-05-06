/**
 * Created by Raul on 9/25/2016.
 */

var list = [
                {em1: "Good-mood", em2: "Bad-mood"},
                {em1: "Happy", em2: "Sad"},
                {em1: "Satisfied", em2: "Depressed"},
                {em1: "Cheerful", em2: "Gloomy"},
                {em1: "Pleased", em2: "Displeased"},
                {em1: "Joyful", em2: "Sorrowful"},
            ];

jQuery(document).ready(function ($) {

    
    setSliders();

//    var input;// = $('#id_slide1text');


    var numSliders = list.length;

    for (var iSlide = 0; iSlide<= numSliders; iSlide ++){

        $('#id_slide'+ iSlide + 'text').val(null);
        $('#slide'+ iSlide+ "text").val(null);

        $("#slide" + iSlide).slider({
          orientation: "horizontal",
          max: 10,min: 0,
            value: -1,
          slide: function (event, ui){
              var tempName = this.id;
              $('#id_'+ tempName + 'text').val(ui.value);
              ui.handle.style.display = "inline";
              console.log(tempName);
              $('#'+ tempName + "text").val(ui.value);
              updateValues(tempName);
              checkValid(tempName);
          }
          ,
            change : function (event, ui) {
                var tempName = this.id;
              $('#id_'+ tempName + 'text').val(ui.value);
              ui.handle.style.display = "inline";
              console.log(tempName);
              $('#'+ tempName + "text").val(ui.value);
              updateValues(tempName);
              checkValid(tempName);
            },
            start: function (event, ui) {
                var tempName = this.id;
              $('#id_'+ tempName + 'text').val(ui.value);
              ui.handle.style.display = "inline";
              console.log(tempName);
              $('#'+ tempName + "text").val(ui.value);
              updateValues(tempName);
              checkValid(tempName);
            }
        });
    };


    function setSliders() {
            console.log("called the slider function");
            //var length = $(".item").length;
            //console.log("length", length);

        for(var i = 0; i < list.length; i++) {
             $("<div class='row'> <div class='item'>" +
                        "<div class='col-md-2'>(<span class=slide" + i + " ></span>)"
                        + list[i].em1 + "</div>" +
                        "<div class='col-md-8' id=slide" + i+ "></div>" +
                        "<div class='col-md-2'>" + list[i].em2 + "(<span class=slide" + i + "x id=slide" + i+ "text type=hidden readonly ></span>)</div>" + "<br>" +
                        "<input type=hidden name=survey_response" + i + " id=id_slide" + i + "text value=0>"
                        + "</div></div>").appendTo(".controls");
        }
    }
    
    function checkValid(){
        var myVal;
        for(var j = 0; j < numSliders; j++){
            myVal = $('#id_slide' + j + 'text').val() ;
            console.log("my Val: ", myVal);
            if( !myVal){
                $("#hideNext").hide();
                return
            } else{
                $("#hideNext").show();
            }
        }
    };

    $(".ui-slider-handle").hide();
    $("#hideNext").hide();


    function updateValues(name) {
        $('.' + name).text(10 - $("#" + name + 'text').val());
        $('.' + name + 'x').text($("#" + name + 'text').val());
    }
});