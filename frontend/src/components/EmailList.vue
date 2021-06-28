<template>
  <v-list three-line>
    <template v-if="receivedMessages.count === 0">
      <v-card class="pa-md-15 mx-lg-auto mt-15 elevation-0" max-width="350px">
        <v-alert outlined type="info" text color="cyan" max-width="250">
          No emails yet!
        </v-alert>
      </v-card>
    </template>
    <template v-for="item in receivedMessages.results">
      <v-list-item :key="item.id">
        <v-list-item-avatar>
          <v-img src="https://cdn.vuetifyjs.com/images/lists/2.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-subtitle>
            <span class="text--primary">
              {{ item.created_at }} | Sender: {{ item.sender.username }}(ID:{{
                item.sender.id
              }}) | Receiver: {{ item.receiver.username }}(ID:{{
                item.receiver.id
              }})
            </span>
          </v-list-item-subtitle>
          <v-list-item-title v-html="item.subject"></v-list-item-title>
          <v-list-item-subtitle>
            {{ item.message }}
          </v-list-item-subtitle>
        </v-list-item-content>

        <DeleteButton :id="item.id" @delete-email="deleteEmailItem" />
      </v-list-item>
      <v-divider :key="'d' + item.id" :inset="true"></v-divider>
    </template>

    <template>
      <div class="text-center">
        <v-pagination
          v-if="pagesCount > 1"
          color="cyan"
          v-model="pageId"
          :length="pagesCount"
          :total-visible="7"
          @input="next"
        ></v-pagination>
      </div>
    </template>
  </v-list>
</template>

<script>
import DeleteButton from "./DeleteButton.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "EmailList",
  components: {
    DeleteButton,
  },
  data() {
    return {
      dialog: false,
      snackbar: false,
      pageId: 1,
    };
  },
  computed: {
    ...mapGetters(["receivedMessages", "userId"]),
    pagesCount: function () {
      if (this.receivedMessages.count > 0) {
        return Math.ceil(this.receivedMessages.count / 5);
      }
      return 1;
    },
  },
  methods: {
    ...mapActions(["getEmails", "deleteEmail"]),
    next() {
      this.$emit("load-emails", this.userId, this.pageId);
    },
    deleteItem() {
      this.snackbar = true;
    },
    deleteEmailItem(id) {
      this.deleteEmail(id).then(() => {
        this.pageId =
          this.receivedMessages.results.length > 1 ? this.pageId : 1;
        this.$emit("load-emails", this.userId, this.pageId);
      });
    },
  },
  watch: {
    userId: function (val) {
      if (val > 0) {
        this.pageId = 1;
      }
    },
  },
};
</script>

<style>
.v-list-item__action i {
  cursor: pointer;
}
</style>
