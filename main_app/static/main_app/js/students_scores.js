

$('#clearBtn').click(function(){

    Swal.fire({
      title: 'Are you sure ?',
      text: "Do you want to clear all scores ?",
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, clear !!'
    }).then((result) => {
      if (result.value) {

         window.location = '/clear_scores/';
      }
    })

});