<template>
  <div class="pa-md-10 pa-10 mx-lg-auto" style="width: 100%">
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="submit">
        <validation-provider
          v-slot="{ errors }"
          name="Subject"
          rules="required|max:50"
        >
          <v-textarea
            v-model="emailForm.subject"
            :counter="50"
            :error-messages="errors"
            auto-grow
            :rows="2"
            label="Subject"
            required
          ></v-textarea>
        </validation-provider>
        <validation-provider
          v-slot="{ errors }"
          name="Message"
          rules="required|max:100"
        >
          <v-textarea
            v-model="emailForm.message"
            :counter="100"
            :error-messages="errors"
            label="Message"
            required
          ></v-textarea>
        </validation-provider>

        <validation-provider
          v-slot="{ errors }"
          name="SenderID"
          rules="required|min_value:1"
        >
          <v-text-field
            v-model="emailForm.senderId"
            :error-messages="errors"
            label="SenderID"
            type="number"
            required
          ></v-text-field>
        </validation-provider>

        <validation-provider
          v-slot="{ errors }"
          name="ReceiverID"
          rules="required|min_value:1"
        >
          <v-text-field
            v-model="emailForm.receiverId"
            :error-messages="errors"
            label="ReceiverID"
            type="number"
            required
          ></v-text-field>
        </validation-provider>
        <div class="text-center">
          <v-btn class="mr-4" type="submit" :disabled="invalid"> send </v-btn>
          <v-btn @click="clear"> clear </v-btn>
        </div>
      </form>
    </validation-observer>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from "vuex";
import { required, max, min_value } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";

setInteractionMode("eager");

extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});

extend("max", {
  ...max,
  message: "{_field_} may not be greater than {length} characters",
});

extend("min_value", {
  ...min_value,
  message: "{_field_} may not be less than {min}",
});

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    emails: [],
  }),
  computed: {
    ...mapGetters(["emailForm"]),
  },
  methods: {
    ...mapActions(["sendEmail"]),
    ...mapMutations(["CLEAR_EMAIL_FORM"]),
    async submit() {
      const isValid = await this.$refs.observer.validate();
      if (isValid) {
        const payload = {
          subject: this.emailForm.subject,
          message: this.emailForm.message,
          receiver: this.emailForm.receiverId,
          sender: this.emailForm.senderId,
        };
        this.sendEmail(payload);
        this.$refs.observer.reset();
      }
    },
    clear() {
      this.CLEAR_EMAIL_FORM();
      this.$refs.observer.reset();
    },
  },
};
</script>
