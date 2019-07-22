
function delete_exam(exam_id, exam_name){

    Swal.fire({
      title: 'Are you sure ?',
      text: "Delete ( " + exam_name + " ) Exam ?",
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

function publish_exam(exam_id, exam_name, num_of_questions){

    checkbox = document.getElementById('publish_exam_' + exam_id);

    if (num_of_questions == 0) {

        Swal.fire({
            type: 'error',
            title: 'Oops ..',
            text: "You can't publish exam with no questions",
            showConfirmButton: true,
        })

        checkbox.checked = false;

    }else {


    console.log(checkbox.checked)
    if (!checkbox.checked){

        Swal.fire({
          title: 'Are you sure ?',
          text: "Un-publish ( " + exam_name + " ) Exam ?",
          type: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, Un-publish !'
        }).then((result) => {
          if (result.value) {

              window.location = '/un_publish_exam/' + exam_id + '/';

          }else {

            checkbox.checked = true;
          }
        })

        }else {

            Swal.fire({
              title: 'Are you sure ?',
              text: "Publish ( " + exam_name + " ) Exam ?",
              type: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'Yes, publish !'
            }).then((result) => {
              if (result.value) {

                  window.location = '/publish_exam/' + exam_id + '/';

              }else {

                checkbox.checked = false;
              }
            })

        }

    }

}
