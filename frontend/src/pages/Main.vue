<template>
    <div>
        <NavBar></NavBar>
        <Banner></Banner>
        <ProductList :products="products"/>
        <Services></Services>
        <Faq></Faq>
        <FormOrder
        @create="createOrder"/>
        <Gallery></Gallery>
        <Footer></Footer>
        
    </div>
    <confirmModal v-model:show="confirmOrderVisible"></confirmModal>
</template>

<script>
import NavBar from "@/components/NavBar.vue"
import Banner from "@/components/Banner.vue"
import Faq from "@/components/Faq"
import FormOrder from "@/components/FormOrder"
import Services from "@/components/Services.vue";
import Gallery from "@/components/Gallery.vue"
import ProductList from "@/components/ProductList.vue"
import Footer from "@/components/Footer.vue"
import confirmModal from "@/components/confirmModal.vue"
// import axios from 'axios'

export default{
    components:{
       NavBar, ProductList,Faq, FormOrder, Services, Gallery, Banner, Footer, confirmModal
    },
    data(){
        return {
            products:[
                {
                    id:1,
                    name:"t-shirt with anime custom",
                    price_start:2000,
                    dsc:"blabla",
                    img:"ncskncks",
                },
                {
                    id:2,
                    name:"t-shirt with anime custom",
                    price_start:2000,
                    dsc:"blabla",
                    img:"ncskncks",
                },
            ],
            confirmOrderVisible: true,
            orders:[]
        }
    },
    methods:{
        createOrder(order){
            this.orders.push(order);
            this.confirmOrderVisible = true;
            console.log(this.orders);
        }
    }
}
</script>