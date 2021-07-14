<template>
  <div class="user-info-container" @click="openChat(user)">
    <div v-bind:style="{background: user['icon_color']}" class="user-logo"></div>
    <div class="user-name">{{ user['name'] }} <span v-if="user['user_id'] === this.$store.state.my_hash">(you)</span></div>
  </div>
</template>

<script>
export default {
  name: "User",
  props: {
    user: {
      require: true
    }
  },
  methods: {
    openChat(user){
      let user_id = user['user_id']
      let user_name = user['name']
      if (this.$store.state.current_chat_id !== user_id) {
        this.$store.commit('set_current_chat_id', user_id)
        this.$store.commit('set_current_chat_name', user_name)
        this.$store.commit('update_message_list', [])
        let msg = {
          message_type: "open_chat",
          from_user_id: this.$store.state.my_hash,
          to_user_id: user_id
        }
        this.$store.state.connection.send(JSON.stringify(msg))
      }
    }
  }
}
</script>

<style scoped>
.user-info-container{
  display: flex;
  padding: 5px 15px 5px 40px;
  height: 65px;
}
.user-logo{
  margin-right: 20px;
  width: 55px;
  height: 55px;
  border-radius: 28px;
}
.user-name{
  line-height: 65px;
  /* todo vertical middle */
  vertical-align: middle;
}
</style>
