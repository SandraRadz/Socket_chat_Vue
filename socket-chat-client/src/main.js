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
    my_hash: '',
    my_name: '',
    online_user_list:  [],
    message_list: [],
    current_chat_id: '',
    current_chat_name: ''
  },
  mutations: {
    set_my_hash(state, user_hash){
      state.my_hash = user_hash
    },
    set_my_name(state, user_name) {
      state.my_name = user_name
    },
    update_online_user_list(state, items){
      Vue.set(state, 'online_user_list', [...items]);
    },
    update_message_list(state, items){
      Vue.set(state, 'message_list', [...items]);
    },
    add_new_message(state, item){
      state.message_list.push(item)
    },
    set_current_chat_id(state, new_id){
      state.current_chat_id = new_id
    },
    set_current_chat_name(state, new_name){
      state.current_chat_name = new_name
    }
  }
})

new Vue({
  store: store,
  render: h => h(App),
}).$mount('#app')
