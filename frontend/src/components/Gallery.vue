<template>
    <div class="py-5">
        <div class="container">
            <div class="text-center">
                <h2 class="section-heading text-uppercase">Фотографии от наших клиентов</h2>
                <!-- <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3> -->
            </div>
            <div class="row align-items-center">
                <div class="col-md-3 col-sm-6 my-3" v-for="photo in photos">
                    <a :href="photo.img_url" class="image-link" data-lightbox="example-1">
                        <img class="img-fluid d-block mx-auto" :src="photo.img_url" alt="..." aria-label="Photo" />
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default{
    props:{
        photos:{
            type: [],
            required: true,
        }
    },
}
</script>