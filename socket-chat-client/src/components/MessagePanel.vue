<template>
  <div>
    <div class="user-block-header">
      <div class="title"> {{current_chat_name}}</div>
    </div>
    <div class="user-list">
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
    current_chat_name: {
      require: true
    },
    messages: {
      require: true
    }
  }
}
</script>

<style scoped>

</style>