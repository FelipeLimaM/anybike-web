// Initialize collapse button
  $(".button-collapse").sideNav();
  // Initialize collapsible (uncomment the line below if you use the dropdown variation)
  $('.collapsible').collapsible();

  // $('.button-collapse').sideNav({
  //     menuWidth: 300, // Default is 240
  //     edge: 'right', // Choose the horizontal origin
  //     closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
  //   }
  // );

$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    format: 'dd/mm/yyyy', 
  });


 $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
    //select
    $('select').material_select();

    $(".item-service").click(function() {
        var id = [];
        $(".item-service").each(function() {
            if ($(this).is(":checked")){
              id.push($(this).val());
            }
        });
        getservices(id);
    });

    jQuery("#id_cpf").mask("999.999.999-99");

    jQuery("#id_phone_number").mask("(99) 9999-9999");
    

  });



function getservices(list_service) {
  var data_send = {
    csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
    service: list_service,
  }
  $.ajax({
    url : "/ajax/getvalue",
    type: "POST",
    data : data_send,
    dataType : "json",
    success: setprice,
    // error: alert("erro server"),
  });
}

function setprice(data) {
  $("#id_value").val(data);
  console.log(data);
}