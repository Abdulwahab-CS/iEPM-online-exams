
function delete_exam(exam_id, exam_name){

    Swal.fire({
      title: 'Are you sure ?',
      text: "Do you want to delete ( " + exam_name + " ) Exam ?",
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it !!'
    }).then((result) => {
      if (result.value) {

          window.location = '/delete_exam/' + exam_id + '/';

      }
    })

}
