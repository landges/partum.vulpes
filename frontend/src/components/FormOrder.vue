<template>
    <section class="page-section" id="contact">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">Свяжитесь с нами</h2>
            <h3 class="section-subheading text-muted">Заполните форму и мы свяжемся с вами</h3>
        </div>
        <form id="contactForm" method="post" @submit.prevent>
           
            <div class="row align-items-stretch mb-5">
                <div class="col-md-6" style="margin:auto;">
                    <div class="form-group text-center">
                        <!-- Name input-->
                        <my-input id="name" name="name" type="text" placeholder="Ваше Имя *" data-sb-validations="required" v-model="order.name"/>
                        <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
                        {{v$.order.name.error}}
                    </div>
                    <div class="form-group">
                        <!-- Email address input-->
                        <input class="form-control" id="email" name="email" type="email" placeholder="Email *" data-sb-validations="required,email" />
                        <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
                        <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
                    </div> 
                    <div class="form-group mb-md-0 text-center">
                        <!-- Phone number input-->
                        <my-input id="phone" name="phone" v-mask="'####-##'" type="tel" placeholder="Ваш номер телефона *" data-sb-validations="required" 
                        v-model="order.phone"/>
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
            <div class="text-center">
                <button class="btn btn-primary btn-xl text-uppercase" id="submitButton" type="submit" @click="createOrder">
                    Отправить
                </button>
            </div>
        </form>
    </div>
</section>
</template>
<script>
import  {useVuelidate} from '@vuelidate/core'
import { required, email } from '@vuelidate/validators'

export default {
    setup () {
        return { v$: useVuelidate() }
    },
    data(){
        return {
            order:{
                name:"",
                phone:"",
            }
        }
    },
    validations () {
        return {
            order:{
                name: { required }, // Matches this.firstName
                phone: { required }, // Matches this.lastName
                email: { required, email } // Matches this.contact.email
            }
            
            
        }
    },
    methods:{
        createOrder(){
            this.order.id = Date.now();
            if (this.checkForm() == true){
                this.$emit('create', this.order);
                this.order = {
                    name:"",
                    phone:"",
                }
            } 
            
        },
        checkForm(){
            return true
        }
    }
}
</script>