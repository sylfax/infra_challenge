import Vue from 'vue'

import App from './App.vue'
import router from './router'
import * as bootstrap from 'bootstrap'
import 'bootstrap-icons/font/bootstrap-icons.css';
import './assets/main.css'
import './scss/styles.scss'

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
