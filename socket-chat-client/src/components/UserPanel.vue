<template>
  <div>
    <div class="user-block-header">
      <div class="title">Users</div>
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
    users: {
      require: true
    }
  }
}
</script>

<style scoped>
.user-block-header{
  padding: 40px 20px 20px 40px;

}

.title{
  text-align: left;
  font-size: 24px;
  color: #2c3e50;
  font-weight: bold;


}
</style>