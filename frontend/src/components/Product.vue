<template>
    <div class="col-lg-4 col-sm-6 mb-4">
        <!-- Portfolio item 1-->
        <div class="portfolio-item">
            <a class="portfolio-link" data-bs-toggle="modal" href="#portfolioModal{{product.id}}" @click="openModal">
                <div class="portfolio-hover">
                    <div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div>
                </div>
                <img class="img-fluid" src="{{product.img}}" alt="..." />
            </a>
            <div class="portfolio-caption">
                <div class="portfolio-caption-heading">{{product.name}}</div>
                <div class="portfolio-caption-subheading text-muted">{{product.price_start}} Р.</div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "product",
    props:{
        product:{
            type: Object,
            required:true,
        }
    },
    methods:{
        openModel(){
            this.emit("openModalid", this.product.id);
        }
    }
}
</script>