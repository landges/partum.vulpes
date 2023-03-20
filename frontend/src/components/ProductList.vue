<template>
    <div class="popular-and-price" id="products" v-if="products.length > 0">
        <div class="container">
            <h2 class="section-title">Популярные товары</h2>
            <!-- <a class="btn to-catalog" href="#" title="Посмотреть все товары">Каталог</a> -->
            <div class="popular-items clearfix swiper">
        
                <div class="swiper-wrapper">
    
                <product 
                v-for="product in products"
                :product="product"
                :key="product.id"
                />
                </div>

            </div>
        </div>
    </div>
    <h2 v-else>Posts is empty</h2>
</template>
<script>
import Product from '@/components/Product';
export default {
    components:{
        Product,
    },
    props:{
        products:{
            type: Array,
            required: true,
        }
    }
}
</script>
<style scoped>
.popular-and-price {
  padding-top: 70px;
  padding-bottom: 90px;
  background-color: #F4F0EA;
}

.popular-and-price .container {
  position: relative;
}
</style>