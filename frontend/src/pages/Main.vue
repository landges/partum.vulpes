<template>
    <div>
        <NavBar></NavBar>
        <Banner></Banner>
        <ProductList :products="products"/>
        <Services></Services>
        <Faq></Faq>
        <FormOrder
        @create="createOrder"/>
        <Gallery :photos="photos"></Gallery>
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
import axios from 'axios'

export default{
    components:{
       NavBar, ProductList,Faq, FormOrder, Services, Gallery, Banner, Footer, confirmModal
    },
    data(){
        return {
            isProductsLoading: false,
            products:[],
            confirmOrderVisible: false,
            orders:[]
        }
    },
    methods:{
        createOrder(order){
            this.orders.push(order);
            this.PostOrder(order);
        },
        async fetchProducts(){
            try{
                this.isPostLoading =true;
                const response = await axios.get('http://127.0.0.1:8000/api/get/products',{
                    params:{
                        page: this.page,
                        limit:this.limit,
                    }
                });
                // this.totalPage = 10;
                this.products = response.data;
            }
            catch(e){
                alert("Error");
            }
            finally{
                this.isPostLoading = false;
            }
        },
        async fetchGallery(){
            try{
                this.isPostLoading =true;
                const response = await axios.get('http://127.0.0.1:8000/api/get/gallery',{
                    params:{
                        page: this.page,
                        limit:this.limit,
                    }
                });
                // this.totalPage = 10;
                this.photos = response.data;
            }
            catch(e){
                alert("Error");
            }
            finally{
                this.isPostLoading = false;
            }
        },
        async PostOrder(order){
            const response = await axios.post('http://127.0.0.1:8000/api/post/order/create', order)
            console.log(response);
            if (response.status == 201 || response.status == 200    ){
                console.log('hello')
                this.confirmOrderVisible = true;
            }
        },
    },
    mounted(){
        this.fetchProducts();
        this.fetchGallery();
    },
}
</script>