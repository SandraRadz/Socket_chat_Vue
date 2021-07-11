<template>
  <div class="message-container">
<!--    <div v-bind:style="{background: user['icon_color']}" class="user-logo"></div>-->
    <div class="user-name">{{ message['name'] }}</div>
    <div class="message">{{ message['text'] }}</div>
  </div>
</template>

<script>
export default {
  name: "Message",
  props: {
    message: {
      require: true
    }
  }
}
</script>

<style scoped>
  .message-container{
    display: flex;
    /*padding: 5px 15px 5px 40px;*/
    min-height: 35px;
  }
  .user-name{
    font-weight: bold;
    margin-bottom: 10px;
    display: block;
  }
  .message{
    display: block;
  }
</style>