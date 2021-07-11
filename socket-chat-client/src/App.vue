<template>
  <div id="app">
    <div class="column left-column">
      <UserNameModel/>
      <div class="left-column-container">
          <div id="user-list-column" class="column">
            <UserPanel tab_name="My Chats" :users="users"/>
            <UserPanel tab_name="Online Users" :users="users"/>
          </div>
          <div id="message-column" class="column">
            <div class="flex-column">
              <div class="message-list-block">
                <MessagePanel :messages="messages" :current_chat_name="current_chat_name"/>
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
      message: '',
      messages: [{name: "me", text: "Hello"}, {name: "Kelly", text: "How are you"}, {name: "me", text: "Fine"}],
      current_chat_name: 'Kelly',
      users: [{name: "Sasha", icon_color: "aqua"}, {name: "Kelly", icon_color: "darkcyan"}, {name: "Ann", icon_color: "cornflowerblue"}],
    }
  },
  methods: {
    sendMessage(e) {
      e.preventDefault();
      this.$store.state.connection.send(this.message);

      this.message = '';
      console.log("send message");
    },

  },
  created: function() {
    let app_this = this
    this.$store.state.connection.onmessage = function(event) {
      let parsed_data = JSON.parse(event.data)
      let message_type = parsed_data["message_type"]
      if (message_type === 'user_id'){
        app_this.$store.commit('set_my_hash', parsed_data['user_id'])
      }
      console.log("Successfully got message!")
      console.log(event);

    }

    this.$store.state.connection.onopen = function(event) {
      console.log("Successfully connected to the echo websocket server...")
      console.log(event)
    }

    this.$store.state.connection.onclose = function(event) {
      console.log(event)
      console.log("closed")
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
