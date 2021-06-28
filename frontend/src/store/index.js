import Vue from "vue";
import Vuex from "vuex";
import user from "./modules/user";
import emails from "./modules/emails";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    emails,
  },
});
