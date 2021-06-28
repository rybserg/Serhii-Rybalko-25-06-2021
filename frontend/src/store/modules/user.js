import { requestConfig } from "../../common/api.config";

export default {
  state: {
    user: null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
  },
  actions: {
    getCurrentUser(ctx) {
      fetch("/api/user/", requestConfig())
        .then(async (response) => {
          const data = await response.json();
          ctx.commit("SET_USER", data);
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
        })
        .catch((error) => {
          console.error("There was an error!", error);
        });
    },
  },
  getters: {
    user: (state) => state.user,
  },
};
