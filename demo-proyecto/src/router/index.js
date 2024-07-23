import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../components/HelloWorld.vue';
import ListaEstudiantes from '../components/ListaEstudiantes.vue';
import ListaTelefonos from '../components/ListaTelefonos.vue';
import ListaTelefonosDos from '../components/ListaTelefonosDos.vue';
import ListaEdificios from '../components/ListaEdificios.vue';

const routes = [
  { path: '/estudiantes',
  name: 'ListaEstudiantes',
  component: ListaEstudiantes },

  { path: '/telefonos',
  name: 'ListaTelefonos',
  component: ListaTelefonos },

  { path: '/telefonos-dos',
  name: 'ListaTelefonosDos',
  component: ListaTelefonosDos },

  { path: '/edificios',
  name: 'ListaEdificios',
  component: ListaEdificios }


];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
