<template>
    <section class="page-section" id="contact">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">Свяжитесь с нами</h2>
            <h3 class="section-subheading text-muted">Заполните форму и мы свяжемся с вами</h3>
        </div>
        <!-- * * * * * * * * * * * * * * *-->
        <!-- * * SB Forms Contact Form * *-->
        <!-- * * * * * * * * * * * * * * *-->
        <!-- This form is pre-integrated with SB Forms.-->
        <!-- To make this form functional, sign up at-->
        <!-- https://startbootstrap.com/solution/contact-forms-->
        <!-- to get an API token!-->
        <form id="contactForm" action="{%url 'main'%}" method="post">
           
            <div class="row align-items-stretch mb-5">
                <div class="col-md-6" style="margin:auto;">
                    <div class="form-group text-center">
                        <!-- Name input-->
                        <input class="form-control" id="name" name="name" type="text" placeholder="Ваше Имя *" data-sb-validations="required" />
                        <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
                    </div>
                    <div class="form-group">
                        <!-- Email address input-->
                        <input class="form-control" id="email" name="email" type="email" placeholder="Email *" data-sb-validations="required,email" />
                        <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
                        <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
                    </div> 
                    <div class="form-group mb-md-0 text-center">
                        <!-- Phone number input-->
                        <input class="form-control" id="phone" name="phone" type="tel" placeholder="Ваш номер телефона *" data-sb-validations="required" />
                        <div class="invalid-feedback" data-sb-feedback="phone:required">A phone number is required.</div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group form-group-textarea mb-md-0">
                        <!-- Message input-->
                        <textarea class="form-control" id="message" name="content" placeholder="Ваши пожелания *" data-sb-validations="required"></textarea>
                        <div class="invalid-feedback" data-sb-feedback="message:required">A message is required.</div>
                    </div>
                </div> 
            </div>
            <!-- Submit success message-->
            <!---->
            <!-- This is what your users will see when the form-->
            <!-- has successfully submitted-->
            
            <!-- Submit Button-->
            <div class="text-center">
                <button class="btn btn-primary btn-xl text-uppercase" id="submitButton" type="submit">
                    Отправить
                </button>
            </div>
        </form>
        <!-- <script> -->
        //     function getFormData($form){
        //         var unindexed_array = $form.serializeArray();
        //         var indexed_array = {};
        //         $.map(unindexed_array, function(n, i){
        //             indexed_array[n['name']] = n['value'];
        //         });
        //         return indexed_array;
        //     }
            
        //     $(function() {
        //       //задание заполнителя с помощью параметра placeholder
        //       $("#phone").mask("+7(999)999-9999", {placeholder: "+7(___)___-____" });
        //     });
        //     $.validator.setDefaults( {
        //         submitHandler: function () {
        //             var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        //             var $form = $("form");
        //             var data = getFormData($form);
        //             $.ajax({
        //                 url: '/',
        //                 type: 'post',
        //                 cache: true,
        //                 data: data,
        //                 success: function(responce){
        //                     $(':input','#contactForm')
        //                     .not(':button, :submit, :reset, :hidden')
        //                     .val('')
        //                     .prop('checked', false)
        //                     .prop('selected', false);
        //                 }
        //             });
                    
        //             var modal = $('.js-modal-my');
                    
        //             modal.addClass('is-show');
        //             $('.js-modal-overlay').addClass('is-show');
        //         }
        //     } );
    
        //     $(document).ready( function () {
        //         $(':input','#contactForm')
        //         .not(':button, :submit, :reset, :hidden')
        //         .val('')
        //         .prop('checked', false)
        //         .prop('selected', false);
        //         $("#contactForm").validate( {
        //             rules: {
        //                 name: {
        //                     required: true,
        //                     minlength: 2
        //                 },
        //                 email: {
        //                     required: true,
        //                     email: true
        //                 },
        //             },
        //             messages: {
        //                 name: {
        //                     required: "Пожалуйста введите ваше имя",
        //                     minlength: "Ваше имя должно состоять как минимум из 2 символов"
        //                 },
        //                 email: "Введите корректный адрес электронной почты",
        //             },
        //             errorElement: "em",
        //             errorPlacement: function ( error, element ) {
        //                 // Add the `help-block` class to the error element
        //                 error.addClass( "help-block" );
    
        //                 if ( element.prop( "type" ) === "checkbox" ) {
        //                     error.insertAfter( element.parent( "label" ) );
        //                 } else {
        //                     error.insertAfter( element );
        //                 }
        //             },
        //             success: function ( label, element ) {
        //                 // Add the span element, if doesn't exists, and apply the icon classes to it.
        //                 if ( !$( element ).next( "span" )[ 0 ] ) {
        //                     $( "<span class='glyphicon glyphicon-ok form-control-feedback'></span>" ).insertAfter( $( element ) );
        //                 }
                        
        //             },
        //             highlight: function ( element, errorClass, validClass ) {
        //                 $( element ).parents( ".col-sm-5" ).addClass( "has-error" ).removeClass( "has-success" );
        //             },
        //             unhighlight: function (element, errorClass, validClass) {
        //                 $( element ).parents( ".col-sm-5" ).addClass( "has-success" ).removeClass( "has-error" );
        //             }
        //         } );
                
                 
        //          $('.js-modal-close').click(function() {
        //             $(this).parent('.js-modal-my').removeClass('is-show');
        //             $('.js-modal-overlay').removeClass('is-show');
        //          });
                    
        //          $('.js-modal-overlay').click(function() {
        //             $('.js-modal-my.is-show').removeClass('is-show');
        //             $(this).removeClass('is-show');
        //          })
        //     });
        // 
    <!-- </script> -->
    </div>
</section>
</template>
<script>
export default {
    
}
</script>