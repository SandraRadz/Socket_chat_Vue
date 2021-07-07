<template>
  <div id="app">
    <b-container class="bv-example-row">
      <b-row>
        <b-col>HOME!</b-col>
        <b-col>
          <div class="message-list-block">
            sdf
          </div>
          <div class="create-message-block">
            <b-input-group>
              <b-form-input v-model="message"></b-form-input>
              <b-input-group-append>
                <b-button variant="success" @click="sendMessage">Send</b-button>
              </b-input-group-append>
            </b-input-group>
          </div>
        </b-col>
        <b-col>3 of 3</b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
const io = require('socket.io-client')
// import Home from './components/Home.vue'

export default {
  name: 'App',
  // components: {
  //   Home
  // },
  methods: {
    sendMessage(e){
      e.preventDefault();
      console.log("click");
      this.socket.emit('send_message', {
        user: 'Sasha',
        msg: this.message
      });

      this.message = '';
      console.log("send message");
    }
  },
  data () {
    return {
      message: '',
      messages: [],
      socket: io('ws://localhost:5000/ ', {transports: ['websocket']})
    }
  },

  mounted () {
    this.socket.on('MESSAGE1', (socket) => {
      console.log("get message")
      this.messages = socket
      console.log(this.messages)
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
