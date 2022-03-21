import Vue from 'vue';

export default {
  namespaced: true,
  state: {
    token: null,
  },
  actions: {
    async LOGIN({ commit }, { username, password }) {
      const response = await Vue.$axios.post('/api/v1/token/', { username, password });
      const { access } = response.data;
      commit('SET_TOKEN', access);
    },
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token;
    },
  },
};
