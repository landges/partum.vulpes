<template>
    <div class="modal-my js-modal-my" data-modal="return" v-if="show" @click.stop="hideDialog">
        <svg @click.stop class="modal__cross js-modal-close" 
        xmlns="http://www.w3.org/2000/svg" 
        viewBox="0 0 24 24">
            <path d="M23.954 21.03l-9.184-9.095 9.092-9.174-2.832-2.807-9.09 9.179-9.176-9.088-2.81 2.81 9.186 9.105-9.095 9.184 2.81 2.81 9.112-9.192 9.18 9.1z"/>
        </svg>
        
        <p class="title">Отлично!</p>
        <p class="text">Спасибо, что выбрали нас! Скоро с вами свяжется наш менеджер.</p>
    </div>
    
</template>
<script>
    import toggleMixin from '@/mixins/toggleMixin';
    
    export default{
        name: "confirm-dialog",
        mixins:[toggleMixin],  
    }
    
</script>
<style scoped>
.modal-my {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  
  border: 1px solid #000;
  
  padding: 10px; 
  z-index: 20;
  background-color: #fff;
  display: none;
}

.modal-my.is-show,
.overlay.is-show{
  display: block;
}

.modal__cross {
  position: absolute;
  top: 20px;
  right: 20px;
  
  width: 20px;
  height: 20px;
  cursor: pointer;

}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .4);
  z-index: 10;
  display: none;
}
em{
  color: white;
}</style>