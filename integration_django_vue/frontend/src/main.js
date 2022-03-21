import Vue from 'vue';

import axios from 'axios';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.$axios = axios.create();

Vue.$axios.interceptors.request.use((config) => {
  const { token } = store.state.auth;
  /* eslint-disable-next-line no-param-reassign */
  config.headers.Authorization = `Bearer ${token}`;
  return config;
});

router.beforeEach((to, from, next) => {
  const { token } = store.state.auth;

  if (to.meta && 'anon' in to.meta && to.meta.anon) {
    return next();
  }

  if (!token) {
    return next('/login');
  }

  return next();
  /*
  console.log(store.state);
  console.log('navigating to', to);
  console.log({ token });
  */
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
