<template>
    <v-container class="fill-screen" fluid>
        <v-row>
            <v-col v-for="(mesa,index) in mesas" :key="index" cols="auto">
                <v-card>
                    <v-card-title>Mesa {{ mesa.id }}</v-card-title>
                    <v-card-text>
                        PLACEHOLDER
                        
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
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
            const res = await api.get('/api/mesa')
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
  