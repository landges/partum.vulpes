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
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{{quenstion.id}}" aria-expanded="false" aria-controls="collapse{{quenstion.id}}">
                                {{quenstion.title}}
                            </button>
                        </h4>
                        <div id="collapse{{quenstion.id}}" class="accordion-collapse collapse" aria-labelledby="heading{{quenstion.id}}" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                {{quenstion.answer}}
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
                    "id":1,
                    "title":"h1",
                    "answer":'a1'
                },
                {
                    "id":2,
                    "title":"h3",
                    "answer":'a3'
                },
                {
                    "id":3,
                    "title":"h4",
                    "answer":'a5'
                }

            ],
        }
    },
}
</script>