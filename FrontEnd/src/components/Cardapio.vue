<script setup>
import { defineProps, defineEmits, onMounted,ref } from 'vue'
import api from '@/api'
import { watch } from 'vue'

const props = defineProps({
  mostrar: Boolean,
  mesa: Object
})

const emit = defineEmits(['update:mostrar'])
const cardapio = ref()
const opcaoID = ref()
const opcaoQTD = ref({})
const snackbar = ref(false)
const comanda = ref()
const fetchComanda = async () => {
    const res1 = await api.get(`/api/comanda/?mesa=${props.mesa.id}`)
    if (Array.isArray(res1.data)) {
    comanda.value = res1.data[res1.data.length-1]
    } else {
    console.warn('Formato de dados inesperado:', res1.data)
    }
}
const fetchCardapio = async () => {
        try {
            const res = await api.get('/api/cardapio')
            if (Array.isArray(res.data)) {
            cardapio.value = res.data[0]

            cardapio.value.Categoria.forEach(categoria => {
            categoria.itens.forEach(opcao => {
              opcaoQTD.value[opcao.id] = 0
            })
          })
            } else {
            console.warn('Formato de dados inesperado:', res.data)
            }
          
        } catch (err) {
            console.error(err)
        }
    }


const fechar = () => {
  emit('update:mostrar', false)
}

const Abrirsnackbar = () =>{
  snackbar.value = true
}

const FazerPedido = async (opcao) => {
    opcaoID.value = opcao.id
    try {
            const res = await api.post('/api/pedido/', {
                item_id: opcaoID.value,
                quantidade: opcaoQTD.value[opcao.id],
                comanda: comanda.value.id
            }) 
          Abrirsnackbar()
        } catch (err) {
            console.error(err)
        }
    
}

const acrescentar = (opcao) => {
  opcaoQTD.value[opcao.id] ++
}
const decrementar = (opcao) => {
  if(opcaoQTD.value[opcao.id] > 1){
    opcaoQTD.value[opcao.id] --
  }else{
    opcaoQTD.value[opcao.id] = 0
  }
  
}

watch(() => props.mostrar, (valor) => {
  fetchComanda()
  fetchCardapio()
})

onMounted(fetchCardapio)
</script>

<template>
  <v-dialog :model-value="mostrar" @update:model-value="val => emit('update:mostrar', val)" max-width="600px">
    <v-card>
      <v-card-title>Cardapio para Mesa {{ mesa.id }}</v-card-title>
      <v-snackbar v-model="snackbar" :timeout="3000">
        Pedido Adicionado a Comanda com Sucesso
        <template #action="{ attrs }">
          <v-btn color="pink" text v-bind="attrs" @click="snackbar = false">Fechar</v-btn>
        </template>
      </v-snackbar>
      <v-expansion-panels multiple>
        <v-expansion-panel v-for="(categoria,j) in cardapio.Categoria">
            <v-expansion-panel-title>{{categoria.nome_categoria}}</v-expansion-panel-title>
                <v-expansion-panel-text>
                    <v-table>
                        <tbody>
                            <tr v-for="(opcao, j) in categoria.itens" :key="j">
                            <td>{{ opcao.nome }}</td>
                            <td>R$ {{ opcao.preço }}</td>
                            <td> <v-btn icon="mdi-minus" size="small" density="compact" @click="decrementar(opcao)"></v-btn> {{  opcaoQTD[opcao.id] }} <v-btn icon="mdi-plus" size="small" density="compact" @click="acrescentar(opcao)"></v-btn></td>
                            <td><v-icon @click="FazerPedido(opcao)">mdi-plus</v-icon></td>
                            </tr>
                        </tbody>
                    </v-table>

                </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
        
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="fechar">Fechar</v-btn>
        <v-btn v-if="mesa.ocupada">Ver Comanda</v-btn>
        <v-btn v-else>Criar Comanda</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
