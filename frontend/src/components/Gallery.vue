<template>
    <div class="py-5">
        <div class="container">
            <div class="text-center">
                <h2 class="section-heading text-uppercase">Фотографии от наших клиентов</h2>
                <!-- <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3> -->
            </div>
            <div class="row align-items-center">
                {%for photo in photos%}
                <div class="col-md-3 col-sm-6 my-3">
                    <a href="{{photo.img.url}}" class="image-link" data-lightbox="example-1">
                        <img class="img-fluid d-block mx-auto" src="{{photo.img.url}}" alt="..." aria-label="Photo" />
                    </a>
                </div>
                {%endfor%}
            </div>
        </div>
    </div>
</template>
<script>
export default{
    
}
</script>