<template>
    <input 
        class="form-control"
        :value="modelValue"
        @input="updateInput"/>
</template>

<script>
export default{
    name: "my-input",
    props:{
        modelValue: [String, Number]
    },
    methods:{
        updateInput(event){
            this.$emit('update:modelValue', event.target.value);
        }
    }    
}
</script>
