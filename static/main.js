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


$(function () {                     // Aguarda a página carregar
	console.log("funciona");
   $("nav a").click(function () { // Associa uma função ao evento de click
      if($(this).attr("link")){
        var link =  $(this).attr("link");     // Armazena o estado selecionado
        $("#container_app").html($("#load").html());
        $("nav .active").removeClass("active");
        $(this).parent().addClass('active');
        console.log(link);
        $.ajax({                          // Inicia a definição da requisição
          url: link,                // Define a url da requisição
          data: {                       // Definição dos dados que serão enviados
           // 'estado': estado           // Adiciona dados a serem enviados
          },                            
          success: function (data) {     // Método de sucesso da requisição
            $("#container_app").html(data);      
          }
        });  
      }
     	
   });	
});