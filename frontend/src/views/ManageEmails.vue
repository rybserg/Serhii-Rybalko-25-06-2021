<template>
  <div>
    <v-card class="mx-lg-auto elevation-0" max-width="250px">
      <validation-observer ref="observer">
        <validation-provider
          v-slot="{ errors }"
          name="User ID"
          rules="required|min_value:1"
        >
          <v-text-field
            class="user-id-input"
            v-model="userId"
            :error-messages="errors"
            label="User ID"
            type="number"
            min="1"
            step="1"
            required
          ></v-text-field>
        </validation-provider>
      </validation-observer>
    </v-card>

    <template>
      <v-tabs v-model="tab" background-color="transparent" color="basil" grow>
        <v-tab><v-icon left> mdi-mailbox </v-icon>Inbox</v-tab>
        <v-tab><v-icon left> mdi-email-send </v-icon>Sent</v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab" v-if="userId">
        <v-tab-item v-for="index in 2" :key="index">
          <v-card flat>
            <EmailList @load-emails="loadEmails" />
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </template>
  </div>
</template>

<script>
import EmailList from "../components/EmailList.vue";
import { min_value } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
import { mapActions, mapMutations } from "vuex";

setInteractionMode("eager");

extend("min_value", {
  ...min_value,
  message: "{_field_} may not be less than {min}",
});

export default {
  name: "Inbox",
  components: {
    EmailList,
    ValidationObserver,
    ValidationProvider,
  },
  data() {
    return {
      tab: null,
    };
  },
  computed: {
    userId: {
      get: function () {
        return this.$store.getters["userId"];
      },
      set: function (value) {
        this.$store.commit("SET_USER_ID", value);
      },
    },
  },
  methods: {
    ...mapActions(["getEmails"]),
    ...mapMutations(["SET_RECEIVED_MESSAGES"]),
    loadEmails(userId, pageId) {
      let payload = { userId: userId };
      payload.params = { page: pageId };
      if (this.tab === 0) {
        payload.params.received = 1;
      } else if (this.tab === 1) {
        payload.params.sent = 1;
      }
      this.getEmails(payload);
    },
  },
  mounted() {
    this.loadEmails(this.userId, 1);
  },
  watch: {
    userId: function (val) {
      this.SET_RECEIVED_MESSAGES([]);
      if (val > 0) {
        this.loadEmails(val, 1);
      }
    },
    tab: function (to, from) {
      if (typeof from === "number" && this.userId > 0) {
        this.loadEmails(this.userId, 1);
      }
    },
  },
};
</script>

<style scoped>
.v-tabs-bar.primary--text {
  color: #00bcd4 !important;
  caret-color: #00bcd4 !important;
}
</style>
