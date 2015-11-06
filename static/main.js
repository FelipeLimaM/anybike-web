// Initialize collapse button
  $(".button-collapse").sideNav();
  // Initialize collapsible (uncomment the line below if you use the dropdown variation)
  //$('.collapsible').collapsible();

  // $('.button-collapse').sideNav({
  //     menuWidth: 300, // Default is 240
  //     edge: 'right', // Choose the horizontal origin
  //     closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
  //   }
  // );

$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15 // Creates a dropdown of 15 years to control year
  });


 $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
  });