<template>
  <div>
    <div class="user-block-header">
      <div class="title">{{ tab_name }}</div>
    </div>
    <div class="user-list">
      <div v-for="(user, index) in users" v-bind:key="index">
        <User :user="user"/>
      </div>
    </div>
  </div>
</template>

<script>
import User from "./ui-elements/User"

export default {
  name: "UserPanel",
  components:{
    User
  },
  props: {
    tab_name: {
      require: true
    },
    users: {
      require: true
    }
  }
}
</script>

<style scoped>
.user-block-header{
  padding: 10px;

}

.title{
  text-align: left;
  font-size: 24px;
  color: #2c3e50;
  font-weight: bold;
}
</style>
