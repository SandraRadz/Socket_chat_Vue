<template>
  <div id="app">
    <div class="column left-column">
      <UserNameModel/>
      <div class="left-column-container">
          <div id="user-list-column" class="column">
            <div class="greeting" v-if="this.$store.state.my_name ">Hi, {{ this.$store.state.my_name }}</div>
            <UserPanel tab_name="Online Users" :users="this.$store.state.online_user_list"/>
          </div>
          <div id="message-column" class="column">
            <div class="flex-column">
              <div class="message-list-block">
                <MessagePanel :messages="this.$store.state.message_list"/>
              </div>
              <div class="create-message-block">
                <b-input-group>
                  <b-form-input v-model="message" @keydown.enter="sendMessage"></b-form-input>
                  <b-input-group-append>
                    <b-button variant="success" class="submit-button" @click="sendMessage">Send</b-button>
                  </b-input-group-append>
                </b-input-group>
              </div>
            </div>
          </div>
      </div>
    </div>
    <div class="column right-column">
      <div>
        111
      </div>
    </div>
  </div>
</template>

<script>
import UserPanel from './components/UserPanel'
import MessagePanel from "./components/MessagePanel";
import UserNameModel from "./components/UserNameModal";

export default {
  name: 'App',
  components: {
    UserNameModel,
    MessagePanel,
    UserPanel
  },

  data: function() {
    return {
      message: ''
    }
  },
  methods: {
    sendMessage(e) {
      e.preventDefault();
      let msg = {
        message_type: "send_message",
        from_user_id: this.$store.state.my_hash,
        to_user_id: this.$store.state.current_chat_id,
        message: this.message
      }
      this.$store.state.connection.send(JSON.stringify(msg))

      this.message = '';
      console.log("send message");
    },

  },
  created: function() {
        this.$store.state.connection.onopen = function(event) {
      console.log("Successfully connected to the echo websocket server...")
      console.log(event)
    }

    this.$store.state.connection.onclose = function(event) {
      console.log(event)
      console.log("closed")
    }

  },
  mounted() {
    let app_this = this
    this.$store.state.connection.onmessage = function(event) {
      let parsed_data = JSON.parse(event.data)
      let message_type = parsed_data["message_type"]
      if (message_type === 'user_id'){
        app_this.$store.commit('set_my_hash', parsed_data['user_id'])
      }
      else if (message_type === 'user_list'){
        let user_list = parsed_data['user_list']
        app_this.$store.commit('update_online_user_list', user_list)
      }
      else if (message_type === 'message_list'){
        let message_list = parsed_data['message_list']
        app_this.$store.commit('update_message_list', message_list)
      }
      else if (message_type === 'new_message'){
        let new_message = parsed_data['new_message']
        app_this.$store.commit('add_new_message', new_message)
      }
      console.log("Successfully got message!")
      console.log(event)
    }
  }
}
</script>

<style>
body, html, #app, .column, .left-column-container{
  height: 100%;
}

body{
  overflow: hidden;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.column{
  display: inline-block;
}

.left-column{
  width: 60%;
}

.greeting{
  text-align: left;
  font-size: 18px;
  color: #2c3e50;
  font-weight: bold;
  padding: 20px 10px;
}

#user-list-column, #message-column{
  border-right: #5b7899 solid 1px;
}

.right-column{
  width: 40%;
}

#user-list-column{
  width: 250px;
  float: left;
}

#message-column{
  float: left;
  flex-grow: 1;
  min-width: 300px;
}

.left-column-container{
  display: flex;
}

.flex-column{
  display: flex;
  flex-direction: column;
  height: 100%;
}

.message-list-block{
  flex: 1;
}

.create-message-block{
  height: 40px;
  margin-bottom: 15px;
  margin-top: 10px;
  padding: 7px;
}
.submit-button {
  background: darkcyan!important;
}

</style>
