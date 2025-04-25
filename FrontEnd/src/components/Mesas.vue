<template>
    <v-container class="fill-screen" fluid>
        <div class="Mesa-icon" v-for="mesa in mesas" :key="mesa.id">
            <v-btn class="btn"><v-col>Mesa {{ mesa.id }}</v-col></v-btn>
        </div>
    </v-container>
</template>
  
<script setup>
    import { ref, onMounted } from 'vue'
    import api from '@/api'

    defineOptions({
    name: 'HomePage',
    })

    const mesas = ref([])

    const fetchMesas = async () => {
        try {
            const res = await api.get('/api/mesas')
            if (Array.isArray(res.data)) {
            mesas.value = res.data
            } else {
            console.warn('Formato de dados inesperado:', res.data)
            }
        } catch (err) {
            console.error(err)
        }
    }

    onMounted(fetchMesas)
</script>

  
<style scoped>
    .fill-screen {
    height: 100vh;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    }
    .btn{
        width: 75px;
        height: 50px;
        margin: 10px;
    } 

</style>
  