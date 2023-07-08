<template>
    <div class="modal-my js-modal-my" 
        :class="{
           'is-show': show
        }"
        data-modal="return" 
        v-if="show">
        <svg @click.stop="hideDialog" class="modal__cross js-modal-close" 
        xmlns="http://www.w3.org/2000/svg" 
        viewBox="0 0 24 24">
            <path d="M23.954 21.03l-9.184-9.095 9.092-9.174-2.832-2.807-9.09 9.179-9.176-9.088-2.81 2.81 9.186 9.105-9.095 9.184 2.81 2.81 9.112-9.192 9.18 9.1z"/>
        </svg>
        
        <p class="title">Отлично!</p>
        <p class="text">Спасибо, что выбрали нас! Скоро с вами свяжется наш менеджер.</p>
        
       
    </div>
    <div class="overlay js-modal-overlay"
        :class="{
            'is-show': show
            }"
        v-if="show"
        @click.stop="hideDialog"></div>
</template>
<script>
    import toggleMixin from '@/mixins/toggleMixin';
    
    export default{
        name: "confirm-dialog",
        mixins:[toggleMixin],  
    }

</script>
