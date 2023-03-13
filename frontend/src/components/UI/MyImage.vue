<template>
    <a class="image-link" href="{{product.img.url}}" data-lightbox="example-2">
            <img
            src="{{product.img.url}}"
            alt="{{product.name}}"
            />
            </a>
</template>
<script>
export default {
    name: "my-image"
}
</script>
<style scoped>

</style>