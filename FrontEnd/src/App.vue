<!-- src/App.vue -->
<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-app-bar-title>Cardapio Red</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn text href="/mesas">Mesas</v-btn>
      <v-btn text>Gerencia</v-btn>
    </v-app-bar>  
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: hsl(0, 0%, 100%); /* azul do Vuetify */
}
</style>
