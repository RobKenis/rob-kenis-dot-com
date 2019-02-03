import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  el: '#app',
  render: h => h(App)
});