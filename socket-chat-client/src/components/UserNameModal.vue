<template>
  <div>
    <b-modal ref="usernameModal" v-model="showModal" hide-footer hide-header-close no-close-on-backdrop no-close-on-esc>
      <template #modal-title>
        Input your name
      </template>
      <b-form-input ref="inputUserName" v-model="name" autofocus></b-form-input>
      <div class="error-message">{{ error_message }}</div>
      <b-button class="mt-3" block @click="saveName">Save name</b-button>
    </b-modal>

  </div>
</template>

<script>
export default {
  name: "UserNameModel",
  data: function () {
    return {
      showModal: true,
      name: '',
      error_message: ''
    }
  },
  watch:{
    showModal: function(){
      // set the focus when the modal opened/closed
      this.$refs.inputUserName.focus();
    }
  },
  methods: {
    saveName(){
      this.error_message = ''
      let trimmed_name = this.name.trim()
      if (trimmed_name.length > 0){
        let msg = {
          message_type: "new_user",
          user_id: "12345",
          user_name: trimmed_name
        }
        this.$store.state.connection.send(JSON.stringify(msg))
        this.$refs['usernameModal'].hide()
      }
      else{
        this.error_message = "The name can't be empty"
        this.name = ''
      }
    }
  }
}
</script>

<style scoped>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
  }

  .modal-fade-enter,
  .modal-fade-leave-to {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .5s ease;
  }
  .error-message{
    color: darkred;
    margin-top: 5px;
    margin-bottom: 5px;
  }
</style>
