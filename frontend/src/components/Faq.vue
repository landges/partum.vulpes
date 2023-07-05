<template>
    <section class="page-section" id="accordion">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">FAQ</h2>
            <h3 class="section-subheading text-muted">Кликните, чтобы получить подробную информацию.</h3>
        </div>
        <article class="my-3">
            <div class="bd-example">
                <div class="accordion" id="accordionExample">
                    
                    <div class="accordion-item" v-for="quenstion in faq">
                        <h4 class="accordion-header" id="heading">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{{forloop.counter}}" aria-expanded="false" aria-controls="collapse{{forloop.counter}}">
                                {{quenstion.title|safe}}
                            </button>
                        </h4>
                        <div id="collapse{{forloop.counter}}" class="accordion-collapse collapse" aria-labelledby="heading{{forloop.counter}}" data-bs-parent="#accordionExample" style="">
                            <div class="accordion-body">
                                {{quenstion.answer|safe}}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </article>
    </div>
</section>
</template>
<script>
export default{
    data(){
        return {
            faq:[
                {
                    "title":"h1",
                    "answer":'a1'
                }
            ],
        }
    },
}
</script>