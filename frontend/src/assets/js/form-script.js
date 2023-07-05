
<script>
    function getFormData($form){
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};
        $.map(unindexed_array, function(n, i){
            indexed_array[n['name']] = n['value'];
        });
        return indexed_array;
    }
    
    $(function() {
      //задание заполнителя с помощью параметра placeholder
      $("#phone").mask("+7(999)999-9999", {placeholder: "+7(___)___-____" });
    });
    $.validator.setDefaults( {
        submitHandler: function () {
            var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
            var $form = $("form");
            var data = getFormData($form);
            $.ajax({
                url: '/',
                type: 'post',
                cache: true,
                data: data,
                success: function(responce){
                    $(':input','#contactForm')
                    .not(':button, :submit, :reset, :hidden')
                    .val('')
                    .prop('checked', false)
                    .prop('selected', false);
                }
            });
            
            var modal = $('.js-modal-my');
            
            modal.addClass('is-show');
            $('.js-modal-overlay').addClass('is-show');
        }
    } );

    $(document).ready( function () {
        $(':input','#contactForm')
        .not(':button, :submit, :reset, :hidden')
        .val('')
        .prop('checked', false)
        .prop('selected', false);
        $("#contactForm").validate( {
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                email: {
                    required: true,
                    email: true
                },
            },
            messages: {
                name: {
                    required: "Пожалуйста введите ваше имя",
                    minlength: "Ваше имя должно состоять как минимум из 2 символов"
                },
                email: "Введите корректный адрес электронной почты",
            },
            errorElement: "em",
            errorPlacement: function ( error, element ) {
                // Add the `help-block` class to the error element
                error.addClass( "help-block" );

                if ( element.prop( "type" ) === "checkbox" ) {
                    error.insertAfter( element.parent( "label" ) );
                } else {
                    error.insertAfter( element );
                }
            },
            success: function ( label, element ) {
                // Add the span element, if doesn't exists, and apply the icon classes to it.
                if ( !$( element ).next( "span" )[ 0 ] ) {
                    $( "<span class='glyphicon glyphicon-ok form-control-feedback'></span>" ).insertAfter( $( element ) );
                }
                
            },
            highlight: function ( element, errorClass, validClass ) {
                $( element ).parents( ".col-sm-5" ).addClass( "has-error" ).removeClass( "has-success" );
            },
            unhighlight: function (element, errorClass, validClass) {
                $( element ).parents( ".col-sm-5" ).addClass( "has-success" ).removeClass( "has-error" );
            }
        } );
        
         
         $('.js-modal-close').click(function() {
            $(this).parent('.js-modal-my').removeClass('is-show');
            $('.js-modal-overlay').removeClass('is-show');
         });
            
         $('.js-modal-overlay').click(function() {
            $('.js-modal-my.is-show').removeClass('is-show');
            $(this).removeClass('is-show');
         })
    });

</script>