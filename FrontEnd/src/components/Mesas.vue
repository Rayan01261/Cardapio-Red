<template>
    <v-container class="fill-screen" fluid>
        <v-row>
            <v-col v-for="(mesa,index) in mesas" :key="index" cols="auto">
                <v-card elevation="12" v-if="mesa.ocupada" color="error">
                    <v-card-title>Mesa {{ mesa.id }}</v-card-title>
                        <v-card-text>MESA OCUPADA</v-card-text>
                    <v-card-actions>
                        <v-btn @click="abrirCardapio(mesa)">Abrir Cardapio</v-btn>
                        <v-btn @click="abrirComanda(mesa)">Ver Comanda</v-btn>
                    </v-card-actions>
                </v-card>
                <v-card elevation="12" v-else color="green">
                    <v-card-title>Mesa {{ mesa.id }}</v-card-title>
                       <v-card-text>MESA LIVRE</v-card-text>
                       <v-card-actions>
                            <v-btn @click="criarComanda(mesa)">Criar Comanda</v-btn>
                        </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>

    <Cardapio
    :mesa="mesaSelecionada" 
    :mostrar="modalAberto" 
    @update:mostrar="modalAberto = $event" 
    />
    <Comanda
    :mesa="mesaSelecionada"
    :comanda="comandaSelecionada"
    :mostrar="modalComandaAberto" 
    @update:mostrar="modalComandaAberto = $event" 
    />
</template>
  
<script setup>
    import { ref, onMounted } from 'vue'
    import api from '@/api'
    import Cardapio from './Cardapio.vue'
    import Comanda from './Comanda.vue'


    defineOptions({
    name: 'HomePage',
    })

    const mesas = ref([])
    const modalAberto = ref(false)
    const modalComandaAberto = ref(false)
    const mesaSelecionada = ref(null)
    const comandaSelecionada = ref({ pedidos: [] })

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

    const abrirCardapio = mesa => {
        mesaSelecionada.value = mesa
        modalAberto.value = true
    }

    const fetchComanda = async (mesa) => {
            try {
                const res = await api.get(`/api/comanda/?mesa=${mesa.id}`)
                if (Array.isArray(res.data)) {
                comandaSelecionada.value = res.data[res.data.length-1]
                } else {
                console.warn('Formato de dados inesperado:', res.data)
                }
            } catch (err) {
                console.error(err)
            }
        }
    const abrirComanda = mesa => {
        fetchComanda(mesa)
        mesaSelecionada.value = mesa
        modalComandaAberto.value = true
    }

    const criarComanda = async (mesa) => {
        try {
            const res = await api.patch(`/api/mesa/${mesa.id}/`, {
                ocupada: true
            })
            const res1 = await api.post('/api/comanda/', {
                total: 0,
                sub_total: 0,
                mesa: mesa.id
            }) 
        } catch (err) {
            console.error(err)
        }
        await fetchMesas()

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
  