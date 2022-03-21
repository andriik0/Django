import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';

import auth from './auth';
import sepulkas from './sepulkas';

Vue.use(Vuex);

const vuexlocal = new VuexPersistence({
  // storage: window.localStorage,
  reducer: (state) => ({ auth: state.auth }),
});

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth,
    sepulkas,
  },
  plugins: [vuexlocal.plugin],
});
