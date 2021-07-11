<template>
  <div class="user-info-container">
    <div v-bind:style="{background: user['icon_color']}" class="user-logo"></div>
    <div class="user-name">{{ user['name'] }}</div>
  </div>
</template>

<script>
export default {
  name: "User",
  props: {
    user: {
      require: true
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