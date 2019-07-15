

//$('.submitBtn').on('click', function(e){
//
//      if( isThereEmptyQuestions() ){
//          Swal.fire({
//              title: 'Error , Empty Question',
//              text: '! Please answer all questions',
//              type: 'error'
//          });
//
//      }else {
//
//          Swal.fire({
//              title: 'OK',
//              text: 'Exam Completed successfully',
//              showConfirmButton: false,
//              timer: 1500,
//              type: 'success'
//
//          });
//
//          // ---------------------------------------- get all answers, and send it to a url to calc the score
//
//          var questionsNumber = $('#questionsNum').text();
//          var answers = [];
//          for(var i=1; i<=questionsNumber; i++){
//              var item = $('input[name=question-'+i+'-opts]:checked').val(); // the item can be either (1, 2, 3, or 4) indicates to the selected option
//              answers.push(item);
//          }
//
//          var examID = $("#examID").text();
//          var studentID = $("#studentID").text();
//
//
//          location.href = "/users"
//
//
////          $.ajax({
////            method: 'POST',
////            url: the_url,
////            data: {"examID":examID, "studentID":studentID, "allAnswers":answers},
////            success: function(){
////
////                setTimeout(function(){
////                    alert('YYYYYY !!');
////                }, 1500);
////
////            }
////          });
//
//      }
//
//  });



function exit_exam(){
    Swal.fire({
      title: 'Are you sure ?',
      text: "You will lost the exam data",
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, Exit !!'
    }).then((result) => {
      if (result.value) {

        Swal.fire({
            type: 'success',
            title: 'OK',
            text: 'Exit Exam',
            showConfirmButton: false,
            timer: 1000
          })

        setTimeout(() => {

            location.href = '/users'

        }, 1000);
      }
    })
}


function submit_exam(){

  if( isThereEmptyQuestions() )
  {
      Swal.fire({
          title: 'Error , Empty Question',
          text: '! Please answer all questions',
          type: 'error'
      });

  }else {
      Swal.fire({
          title: 'OK',
          text: 'Exam completed successfully',
          showConfirmButton: false,
          timer: 1500,
          type: 'success'
      });

       // ---------------------------------------- get all answers, and send it to a url to calc the score

          var questionsNumber = $('#questionsNum').text();
          var answers = [];
          for(var i=1; i<=questionsNumber; i++){
              var item = $('input[name=question-'+i+'-opts]:checked').val(); // the item can be either (1, 2, 3, or 4) indicates to the selected option
              answers.push(item);
          }

          var examID = $("#examID").text();
          var studentID = $("#studentID").text();


          $.ajax({
            method: 'POST',
            url: '/submit_exam2',
            data: {"examID":examID, "studentID":studentID, "allAnswers":answers},
            success: function(){

                setTimeout(function(){
                    alert('YYYYYY !!');
                }, 1500);

            }
          });

//          setTimeout(() => {
//
//                location.href = '/submit_exam/' + examID + '/' + studentID + '/';
//
//          }, 1500);

  }
}

function isThereEmptyQuestions(){

   var questionsNumber = $('#questionsNum').text();
   var empty_Q_Found = false;

   for(var i=1; i<=questionsNumber; i++){
      var item = $('input[name=question-'+i+'-opts]:checked').val();

      if ( typeof item == "undefined" ){

          empty_Q_Found = true;
      }
   }

   return empty_Q_Found;
}