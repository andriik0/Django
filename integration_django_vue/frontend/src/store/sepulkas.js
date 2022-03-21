import Vue from 'vue';

export default {
  namespaced: true,
  state: {
    sepulkas: [],
  },
  actions: {
    async GET_SEPULKAS({ commit }) {
      const response = await Vue.$axios.get('/api/v1/sepulkas/');
      commit('SET_LIST', response.data);
    },
  },
  mutations: {
    SET_LIST: (state, list) => {
      state.sepulkas = list;
    },
  },
};
