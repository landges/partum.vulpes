import { createApp } from 'vue'
import App from './App.vue'
import components from "@/components/UI"
import router from "@/router/router"
import VueMask from 'v-mask'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import './assets/css/styles.css'
import './assets/js/scripts.js'

// Vue.use(Vuelidate)  
const app = createApp(App)

components.forEach(component =>{
    app.component(component.name, component);
})
app.directive('mask', VueMask.VueMaskDirective);
app
    .use(router)
    .mount('#app')
