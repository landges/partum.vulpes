<template>
    <div>
        <Services></Services>
        <Faq></Faq>
        <FormOrder></FormOrder>
        
    </div>
</template>

<script>
import Faq from "@/components/Faq"
import FormOrder from "@/components/FormOrder"
import Services from "@/components/Services.vue";

export default{
    components:{
        Faq, FormOrder, Services
    }
}
</script>