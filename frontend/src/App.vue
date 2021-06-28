<template>
  <div>
    <v-app>
      <v-container fluid>
        <div class="text-center">
          <v-snackbar
            centered
            v-bind:color="snackbar.successStyle ? `cyan` : `red`"
            v-model="snackbar.show"
            timeout="1000"
          >
            {{ snackbar.text }}
          </v-snackbar>
        </div>
        <v-card
          max-width="1000"
          min-height="700"
          class="mx-auto overflow-hidden"
        >
          <v-card-title class="cyan white--text">
            <span class="text-h5">
              <span>{{ title }}</span>
            </span>
            <v-spacer></v-spacer>
            <Menu />
          </v-card-title>
          <router-view />
        </v-card>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Menu from "./components/Menu.vue";

export default {
  name: "App",
  data() {
    return {
      title: "",
    };
  },
  components: {
    Menu,
  },
  computed: {
    ...mapGetters(["user", "snackbar"]),
  },
  methods: {
    ...mapActions(["getCurrentUser", "getEmails"]),
  },
  created() {
    this.getCurrentUser();
  },
  watch: {
    $route: {
      immediate: true,
      handler(to) {
        this.title = to.meta.title;
      },
    },
  },
};
</script>
