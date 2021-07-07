<template>
  <div class="hello">
    <b-container class="bv-example-row">
      <b-row>
        <b-col>HOME</b-col>
        <b-col>
          <div class="message-list-block">
            sdf
          </div>
          <div class="create-message-block">
            <b-input-group>
              <b-form-input v-model="message"></b-form-input>
              <b-input-group-append>
                <b-button variant="success">Send</b-button>
              </b-input-group-append>
            </b-input-group>
          </div>
        </b-col>
        <b-col>3 of 3</b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  name: 'Home'

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.message-list-block{
  height: 500px;
}

</style>