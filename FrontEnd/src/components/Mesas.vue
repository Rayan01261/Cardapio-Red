<template>
    <v-container class="fill-screen" fluid>
        <v-card>
        <v-card-title>Mesas</v-card-title>
        </v-card>
    </v-container>
</template>
  
<script setup>
    import { ref } from 'vue'
    import { defineOptions } from 'vue'
    import axios from 'axios'

    defineOptions({
    name: 'HomePage',
    })

    const mesas = ref([])
    axios.get('localhost/mesas')
        .then(response => {
            mesas.value = console.log(response.data)
        })
        .catch(error => {
            console.error(error)
        })
</script>
  
<style scoped>
    .fill-screen {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    }
</style>
  