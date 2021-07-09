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
// import Home from './components/Home.vue'

export default {
  name: 'App',
  // components: {
  //   Home
  // },

  data: function() {
    return {
      message: '',
      messages: [],
      connection: null
    }
  },
  methods: {
    sendMessage(e) {
      e.preventDefault();
      this.connection.send({
        user: 'Sasha',
        msg: this.message
      });

      this.message = '';
      console.log("send message");
    }
  },
  created: function() {
    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket("ws://localhost:5000/echo")

    this.connection.onmessage = function(event) {
      console.log("Successfully got message!")
      console.log(event);
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

    this.connection.onclose = function(event) {
      console.log(event)
      console.log("closed")
    }

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
