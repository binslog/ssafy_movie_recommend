<template>
  <div>
    startview...
  </div>
</template>

<script>
// import Vue from 'vue'


export default {
  name: 'StartView',
  methods: {
    logout : function (){
      this.$store.dispatch('logout')
      this.$router.push({name : 'Login' })
      
    },
  },
}
</script>

<style></style>
