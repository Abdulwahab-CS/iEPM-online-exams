
function delete_question(exam_id, question_id, question_number){

    Swal.fire({
      title: 'Are you sure ?',
      text: "You want to delete this question " + question_number,
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it !!'
    }).then((result) => {
      if (result.value) {

          window.location = '/delete_question/' + exam_id + '/' + question_id + '/';

      }
    })

}