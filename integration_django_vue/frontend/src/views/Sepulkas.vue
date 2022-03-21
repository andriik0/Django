<template>
  <div class="about">
    <h1>This is a sepulkas page</h1>
    <table>
    <thead>
      <tr>
        <th>
          Коеффициент
        </th>
      <th>
        Название
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="sepulka in sepulkas" :key="sepulka.id">
        <td>{{ sepulka.coefficient }}</td>
        <td>{{ sepulka.slug }}</td>
      </tr>
    </tbody>
  </table>
  </div>
</template>
<script>
import { mapActions, mapState } from 'vuex';

export default {
  computed: mapState('sepulkas', [
    'sepulkas',
  ]),
  methods: mapActions('sepulkas', [
    'GET_SEPULKAS',
  ]),
  mounted() {
    this.GET_SEPULKAS();
  },
};
</script>
