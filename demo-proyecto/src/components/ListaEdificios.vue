<template>
  <div>
    <h1>Lista de Edificios</h1>
    <center>
    <table class="mi-tabla">
      <tr>
        <th>Nombre</th>
        <th>Direccion</th>
        <th>Ciudad</th>
        <th>Tipo</th>
      </tr>
      <tr v-for="edificio in edificios" :key="edificio.id">
        <td>{{ edificio.nombre }}</td>
        <td>{{ edificio.direccion }}</td>
        <td>{{ edificio.ciudad }}</td>
        <td>{{ edificio.tipo }}</td>
      </tr>
    </table>
    </center>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      edificios: []
    };
  },
  created() {
    this.fetchEdificios();
  },
  methods: {
    async fetchEdificios() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/edificios/');
        this.edificios = response.data;
      } catch (error) {
        console.error('Error obteniendo edificios:', error);
      }
    }
  }
};
</script>

<style scoped>
/* agregar ---- */
</style>
