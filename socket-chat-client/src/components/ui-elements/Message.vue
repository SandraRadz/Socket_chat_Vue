<template>
  <div class="message-container" v-bind:class="[message['name'] === 'me' ? myMessageContainer : otherUserMessageContainer]">
    <div class="message-block" v-bind:class="[message['name'] === 'me' ? myMessage : otherUserMessage]">
<!--    <div v-bind:style="{background: user['icon_color']}" class="user-logo"></div>-->
    <div class="user-name">{{ message['name'] }}</div>
    <div class="message">{{ message['text'] }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Message",
  data: function (){
    return {
      myMessageContainer: 'my-message-container',
      otherUserMessageContainer: 'other-user-message-container',
      myMessage: 'my-message',
      otherUserMessage: 'other-user-message'
    }
  },
  props: {
    message: {
      require: true
    },

  }
}
</script>

<style scoped>
  .message-container{
    display: block;
    /*padding: 5px 15px 5px 40px;*/

    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .my-message-container{
    padding-left: 50px;
  }
  .other-user-message-container{
    padding-right: 50px;
  }

  .message-block{
    min-height: 35px;
    border-radius: 10px;
    padding: 7px;
  }

  .my-message{
    background: rgba(127, 255, 212, 0.76);
  }
  .other-user-message{
    background: rgba(100, 149, 237, 0.69);
  }
  .user-name{
    font-weight: bold;
    margin-bottom: 5px;
    display: block;
    font-size: 12px;
    text-align: left;
  }
  .message{
    display: block;
    text-align: left;
  }
</style>
