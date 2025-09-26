<script setup>
import { defineProps, defineEmits, onMounted,ref } from 'vue'
import api from '@/api'

const props = defineProps({
  mostrar: Boolean,
  mesa: Object
})

const emit = defineEmits(['update:mostrar'])
const cardapio = ref()
const fetchCardapio = async () => {
        try {
            const res = await api.get('/api/cardapio')
            if (Array.isArray(res.data)) {
            cardapio.value = res.data[0]
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

onMounted(fetchCardapio)
</script>

<template>
  <v-dialog :model-value="mostrar" @update:model-value="val => emit('update:mostrar', val)" max-width="400px">
    <v-card>
      <v-card-title>Cardapio</v-card-title>
      <v-expansion-panels multiple>
        <v-expansion-panel v-for="(categoria,j) in cardapio.Categoria">
            <v-expansion-panel-title>{{categoria.nome_categoria}}</v-expansion-panel-title>
                <v-expansion-panel-text>
                    <v-table>
                        <thead>
                            <tr>
                            <th class="text-left">Nome</th>
                            <th class="text-left">Preço</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(opcao, j) in categoria.itens" :key="j">
                            <td>{{ opcao.nome }}</td>
                            <td>R$ {{ opcao.preço }}</td>
                            </tr>
                        </tbody>
                    </v-table>

                </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
        
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="fechar">Fechar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
