

incomplete_fields_msg = "!! Please fill the missing fields first";
invalid_correct_ans_msg = "!! Invalid correct Answer field , must be from ( 1 - 4 )";
long_question_body_msg = "!! Long question body ( must be less than 4096 chars )";
long_op1_msg = "!! Long option 1 string ( must be less than 255 chars )";
long_op2_msg = "!! Long option 2 string ( must be less than 255 chars )";
long_op3_msg = "!! Long option 3 string ( must be less than 255 chars )";
long_op4_msg = "!! Long option 4 string ( must be less than 255 chars )";


function delete_question(exam_id, question_id, question_number){

    document.getElementById("question-" + question_id).click();

    Swal.fire({
      title: 'Are you sure ?',
      text: "Delete question " + question_number + " ?",
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it !!'
    }).then((result) => {
      if (result.value) {

          window.location = '/delete_question/' + exam_id + '/' + question_id + '/';

      }else {

        document.getElementById("question-" + question_id).click();
      }
    })

}

function addNewQuestion(exam_id){

        if( isThereEmptyFields() ){
            Swal.fire({
                title: 'Error , Incomplete form',
                text: incomplete_fields_msg,
                type: 'error'
            });

            return false;
        }
        if( !isValidNewQ_correctA($("#newQ_correctA").val()) ) {
            Swal.fire({
                title: 'Error',
                text: invalid_correct_ans_msg,
                type: 'error'
            });

            return false;
        }
        if( !isValidQuestionBodyLength($("#newQ_body").val()) ) {
            Swal.fire({
                title: 'Error',
                text: long_question_body_msg,
                type: 'error'
            });

            return false;
        }
        if( !isValidOptionLength($("#newQ_option1").val()) ) {
            Swal.fire({
                title: 'Error',
                text: long_op1_msg,
                type: 'error'
            });

            return false;
        }
        if( !isValidOptionLength($("#newQ_option2").val()) ) {
            Swal.fire({
                title: 'Error',
                text: long_op2_msg,
                type: 'error'
            });

            return false;
        }
        if( !isValidOptionLength($("#newQ_option3").val()) ) {
            Swal.fire({
                title: 'Error',
                text: long_op3_msg,
                type: 'error'
            });

            return false;
        }
        if( !isValidOptionLength($("#newQ_option4").val()) ) {
            Swal.fire({
                title: 'Error',
                text: long_op4_msg,
                type: 'error'
            });

            return false;
        }

        // Do the AJAX request to add the new question

        q_body = $("#newQ_body").val()
        op1 = $("#newQ_option1").val()
        op2 = $("#newQ_option2").val()
        op3 = $("#newQ_option3").val()
        op4 = $("#newQ_option4").val()
        correct_ans = $("#newQ_correctA").val()


        the_url = '/manage_exam/' + exam_id + '/add_question/';

        $.ajax({
            method: 'post',
            url: the_url,
            data: {
                newQ_body: q_body,
                newQ_option1: op1,
                newQ_option2: op2,
                newQ_option3: op3,
                newQ_option4: op4,
                newQ_correctA: correct_ans,

                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(msg) {

                if(msg == 1){

                    location.href = '/manage_exam/' + exam_id + '/' + 'manage_questions/';
                }

            }

        });


        // -------------------------------------------------- clear the carrosal input fields
        $("#newQ_body").val("");
        $("#newQ_option1").val("");
        $("#newQ_option2").val("");
        $("#newQ_option3").val("");
        $("#newQ_option4").val("");
        $("#newQ_correctA").val("");

        // --------------------------------------------------- hide the modal
        document.getElementById("addQuestion").click();






}

function isThereEmptyFields(){
    if( /^\s*$/.test($("#newQ_body").val()) || /^\s*$/.test($("#newQ_option1").val()) ||  /^\s*$/.test($("#newQ_option2").val()) ||  /^\s*$/.test($("#newQ_option3").val()) ||  /^\s*$/.test($("#newQ_option4").val()) ||  /^\s*$/.test($("#newQ_correctA").val()) )
    return true;
    else
    return false;
}

function isValidNewQ_correctA($correct_A){
    $pattern = /^[1-4]$/;
    if($pattern.test($correct_A)){
        return true;
    }else {
        return false;
    }
}

function isValidQuestionBodyLength($qBody) {
    if($qBody.length <= 4096)
        return true;
    else
        return false;
}

function isValidOptionLength($op) {
    if($op.length <= 255)
        return true;
    else
        return false;
}

function isEmptyFeild(input){
    if( /^\s*$/.test(input) )
      return true;
    else
      return false
}



var questionsList = document.getElementById("questionsList");
// add 'change' event on the current question collapse. if there is a change ,, make the 'update btn' enabled
questionsList.addEventListener('change', function(e){

    // access the question container (in my implementation is the 'form')
    var questionContainer = e.target.parentNode.parentNode;
    var updateBtnId = questionContainer.getElementsByClassName("updateQ_btn")[0].id;
    $("#"+updateBtnId+"").removeAttr('disabled');
});


function update_question(exam_id, question_id) {

    qBody = $("#question-" + question_id + "-body").val();
    op1 = $("#question-" + question_id + "-option-1").val();
    op2 = $("#question-" + question_id + "-option-2").val();
    op3 = $("#question-" + question_id + "-option-3").val();
    op4 = $("#question-" + question_id + "-option-4").val();
    correctA = $("#question-" + question_id + "-correctA").val();


    // check if the input fiels after editing is valid or not
    if( isEmptyFeild(qBody) || isEmptyFeild(op1) || isEmptyFeild(op2) || isEmptyFeild(op3) || isEmptyFeild(op4) || isEmptyFeild(correctA) )
    {
        Swal.fire({
            title: 'Error , Incomplete form',
            text: incomplete_fields_msg,
            type: 'error'
        });

    }else if( !isValidNewQ_correctA(correctA) ){
        Swal.fire({
            title: 'Error',
            text: invalid_correct_ans_msg,
            type: 'error'
        });

    }
    else if( !isValidQuestionBodyLength(qBody) ) {
        Swal.fire({
            title: 'Error',
            text: long_question_body_msg,
            type: 'error'
        });

    }
    else if( !isValidOptionLength(op1) ) {
        Swal.fire({
            title: 'Error',
            text: long_op1_msg,
            type: 'error'
        });

    }
    else if( !isValidOptionLength(op2) ) {
        Swal.fire({
            title: 'Error',
            text: long_op2_msg,
            type: 'error'
        });

    }
    else if( !isValidOptionLength(op3) ) {
        Swal.fire({
            title: 'Error',
            text: long_op3_msg,
            type: 'error'
        });

    }
    else if( !isValidOptionLength(op4) ) {
        Swal.fire({
            title: 'Error',
            text: long_op4_msg,
            type: 'error'
        });

    }
    else {
        // --> OK, all input is valild, now start updating <--

        // -------------------------------- update the question in the database
        $.ajax({
            method: 'POST',
            url: '/update_question/' + exam_id + '/' + question_id + '/',
            data : {
            exam_id: exam_id,
            question_id: question_id,
            qBody: qBody,
            op1: op1, op2: op2, op3: op3, op4: op4,
            correctA: correctA,

            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

            },

            success: function(r){
                if( r == 1 ){

                    // ------------------------------------------ update the question in the table GUI

                    // make the update btn disabled again
                    document.getElementById("updateQuestion-"+question_id+"-Btn").disabled = true;

                    location.href = '/manage_exam/' + exam_id + '/' + 'manage_questions/';

                }
            }

        });

    }





}



