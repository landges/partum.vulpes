<template>
    <section class="page-section bg-light" id="portfolio">
        <div class="container">
            <div class="text-center">
                <h2 class="section-heading text-uppercase">Портфолио</h2>
                <h3 class="section-subheading text-muted">Кликните, чтобы получить подробную информацию.</h3>
            </div>
            <div class="row">
                <product 
                v-for="product in products"
                :product="product"
                :key="product.id"
                
                />
            </div>
        </div>
    </section>
</template>
<script>
import Product from '@/components/Product';
export default {
    components:{
        Product,
    },
    props:{
        products:{
            type: [],
            required: true,
        }
    }
}
</script>