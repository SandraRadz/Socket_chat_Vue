import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    connection: new WebSocket("ws://localhost:5000/echo"),
    my_hash: ''
  },
  mutations: {
    set_my_hash(state, user_hash){
      state.my_hash = user_hash
    }
  }
})

new Vue({
  store: store,
  render: h => h(App),
}).$mount('#app')
