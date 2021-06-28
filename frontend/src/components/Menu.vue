<template>
  <v-menu bottom left>
    <template v-slot:activator="{ on, attrs }">
      <v-btn dark icon v-bind="attrs" v-on="on">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </template>
    <v-list>
      <template v-if="user">
        <v-list-item-avatar class="ml-4">
          <img src="https://cdn.vuetifyjs.com/images/lists/1.jpg" />
        </v-list-item-avatar>
        <v-list-item-content class="ml-4">
          <v-list-item-title>{{ user.username }}</v-list-item-title>
        </v-list-item-content>
      </template>
      <v-list-item v-for="(item, index) in items" :key="index">
        <v-list-item-icon class="mr-4">
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-title>
          <a :href="item.to" v-if="item.type === 'href'">{{ item.title }} </a>
          <router-link
            :to="{ name: item.to }"
            v-else-if="item.type === 'route-name'"
            >{{ item.title }}
          </router-link>
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Menu",
  data: () => ({
    items: [
      {
        title: "Compose Email",
        to: "compose-email",
        type: "route-name",
        icon: "mdi-email-edit-outline",
      },
      {
        title: "Manage Emails",
        to: "manage-emails",
        type: "route-name",
        icon: "mdi-email-multiple-outline",
      },
      {
        title: "Logout",
        to: "/accounts/logout/",
        type: "href",
        icon: "mdi-logout",
      },
    ],
  }),
  computed: {
    ...mapGetters(["user"]),
  },
};
</script>

<style>
.v-application .v-menu__content a {
  text-decoration: none;
}
</style>
