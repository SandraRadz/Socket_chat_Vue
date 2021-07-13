<template>
  <div class="messages-list-container">
    <div class="title-block-header">
      <div class="title">Chat with {{this.$store.state.current_chat_name}}</div>
    </div>
    <div class="message-list">
      <div v-for="(message, index) in messages" v-bind:key="index">
        <Message :message="message"/>
      </div>
    </div>
  </div>
</template>

<script>
import Message from "./ui-elements/Message";
export default {
  name: "MessagePanel",
  comments: Message,
  components: {
    Message
  },
  props: {
    messages: {
      require: true
    }
  }
}
</script>

<style scoped>

.title-block-header{
  border-bottom: #5b7899 solid 1px;
  padding: 20px 10px;
}

.title{
  text-align: left;
  font-size: 24px;
  color: #2c3e50;
  font-weight: bold;
}
.message-list {
  padding-left: 10px;
  padding-right: 10px;
}

</style>
