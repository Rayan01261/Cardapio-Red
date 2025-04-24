<!-- src/pages/HomePage.vue -->
<template>
    <v-container class="fill-screen" fluid>
      <v-card>
        <v-card-title>Bem Vindo</v-card-title>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    name: 'HomePage',
  }
  </script>
  
  <style scoped>
  .fill-screen {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  