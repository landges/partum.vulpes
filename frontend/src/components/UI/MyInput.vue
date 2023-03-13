<template>
   <input type="text" name="name" id="fullname">
</template>
<script>
export default {
    name: "my-input"
}
</script>
<style scoped>
input[type="text"], select, textarea {
    box-sizing: border-box;
    width: 100%;
    height: 54px;
    padding: 9px 15px;
    font: inherit;
    color: inherit;
    border: 2px solid #d5d5d5;
}
</style>