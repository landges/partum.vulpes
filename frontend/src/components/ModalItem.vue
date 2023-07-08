<template>
    <!-- Portfolio item 1 modal popup-->
<div class="portfolio-modal modal fade" id="portfolioModal{{forloop.counter}}" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="close-modal" data-bs-dismiss="modal"><img src="{%static 'img/close-icon.svg'%}" alt="Close modal" /></div>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8">
                        <div class="modal-body">
                            <!-- Project details-->
                            <h2 class="text-uppercase">{{product.name}}</h2>
                            <p class="item-intro text-muted">.</p>
                            <img class="img-fluid d-block mx-auto" :src="product.img_url" alt="..." />
                            
                            <p v-if="product.dsc">{{product.dsc}}</p>
                            
                            <ul class="list-inline">
                                <li>
                                    <strong>Цена:</strong>
                                    {{product.price_start}}
                                </li>
                                
                            </ul>
                            <button class="btn btn-primary btn-xl text-uppercase" data-bs-dismiss="modal" type="button">
                                <i class="fas fa-xmark me-1"></i>
                                Закрыть
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

</template>
<script>
import axios from 'axios'

export default{
    
}
</script>