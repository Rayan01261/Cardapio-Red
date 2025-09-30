<script setup>
import { defineProps, defineEmits, onMounted,ref } from 'vue'
import api from '@/api'
import { watch } from 'vue'

const props = defineProps({
  mostrar: Boolean,
  mesa: Object,
  comanda: Object
})

const emit = defineEmits(['update:mostrar'])
const opcaoID = ref()
const opcaoQTD = ref({})
const snackbar = ref(false)


const fechar = () => {
  emit('update:mostrar', false)
}

const Abrirsnackbar = () =>{
  snackbar.value = true
}


</script>

<template>
  <v-dialog :model-value="mostrar" @update:model-value="val => emit('update:mostrar', val)" max-width="600px">
    <v-card>
      <v-card-title>Comanda para Mesa {{ mesa.id }}</v-card-title>
      <v-snackbar v-model="snackbar" :timeout="3000">
        
        <template #action="{ attrs }">
          <v-btn color="pink" text v-bind="attrs" @click="snackbar = false">Fechar</v-btn>
        </template>
      </v-snackbar>
      <v-card-text>
            <v-table>
                <tbody>
                    <tr v-for="(pedido, j) in comanda.pedidos" :key="j">
                    <td>{{ pedido.item.nome }}</td>
                    <td>R$ {{ pedido.item.preço }}</td>
                    <td>{{ pedido.quantidade }}</td>
                    </tr>
                </tbody>
            </v-table>
        Total: R${{ comanda.total }}
      </v-card-text>
        
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="fechar">Fechar</v-btn>
        <v-btn v-if="mesa.ocupada">Ver Comanda</v-btn>
        <v-btn v-else>Criar Comanda</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
