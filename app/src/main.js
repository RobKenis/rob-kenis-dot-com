import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faTimes, faQuestion} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

[faTimes, faQuestion].forEach(icon => library.add(icon));

Vue.component('FontAwesomeIcon', FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  render: h => h(App)
});