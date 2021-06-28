<template>
  <v-dialog v-model="dialog" persistent max-width="290">
    <template v-slot:activator="{ on, attrs }">
      <v-list-item-action>
        <v-icon v-bind="attrs" color="grey lighten-1" v-on="on">
          mdi-trash-can-outline
        </v-icon>
      </v-list-item-action>
    </template>
    <v-card>
      <v-card-title class="text-h5">
        Are you sure you want to delete this email?
      </v-card-title>
      <v-card-text>Please note that this action is irreversible.</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="cyan darken-1" text @click="dialog = false">
          Cancel
        </v-btn>
        <v-btn color="cyan darken-1" text @click="deleteItem"> Delete </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "DeleteButton",
  props: ["id"],
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    deleteItem() {
      this.dialog = false;
      this.$emit("delete-email", this.id);
    },
  },
};
</script>
