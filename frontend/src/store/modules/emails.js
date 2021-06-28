import { requestConfig } from "../../common/api.config";
import helpers from "../../common/helpers";

export default {
  state: {
    snackbar: {
      show: false,
      text: false,
      successStyle: true,
    },
    emailForm: {
      subject: "",
      message: "",
      senderId: null,
      receiverId: null,
    },
    userId: 1,
    sentMessages: [],
    receivedMessages: [],
  },
  mutations: {
    SET_SNACKBAR(state, snackbar) {
      state.snackbar = snackbar;
    },
    SET_EMAIL_FORM(state, emailForm) {
      state.emailForm = emailForm;
    },
    CLEAR_EMAIL_FORM(state) {
      state.emailForm = {
        subject: "",
        message: "",
        senderId: "",
        receiverId: "",
      };
    },
    SET_SENT_MESSAGES(state, sentMessages) {
      state.sentMessages = sentMessages;
    },
    SET_RECEIVED_MESSAGES(state, receivedMessages) {
      state.receivedMessages = receivedMessages;
    },
    SET_USER_ID(state, userId) {
      state.userId = userId;
    },
  },
  actions: {
    sendEmail(ctx, payload) {
      fetch("/api/emails/", requestConfig(payload, "POST"))
        .then(async (response) => {
          const data = await response.json();

          if (!response.ok) {
            let error = (data && data.message) || response.statusText;
            if (data.sender && data.sender[0]) {
              error += " Sender: " + data.sender[0];
            }
            if (data.receiver && data.receiver[0]) {
              error += " Receiver: " + data.receiver[0];
            }
            throw Error(error);
          }

          ctx.commit("SET_SNACKBAR", {
            show: true,
            text: "Email successfully sent!",
            successStyle: true,
          });
          ctx.commit("CLEAR_EMAIL_FORM");
        })
        .catch((error) => {
          ctx.commit("SET_SNACKBAR", {
            show: true,
            text: "Email sanding is failed. " + error,
            successStyle: false,
          });
        });
    },
    getEmails(ctx, payload) {
      ctx.commit("SET_RECEIVED_MESSAGES", []);
      const queryString = helpers.objectToQueryString(payload.params);
      fetch(
        `/api/users/${payload.userId}/emails/?${queryString}`,
        requestConfig()
      )
        .then(async (response) => {
          const data = await response.json();

          if (!response.ok) {
            let error = (data && data.message) || response.statusText;
            if (response.status === 404) {
              error += " - No such user or page";
            }
            throw Error(error);
          }

          ctx.commit("SET_RECEIVED_MESSAGES", data);
        })
        .catch((error) => {
          ctx.commit("SET_SNACKBAR", {
            show: true,
            text: "Emails fetching is failed. " + error,
            successStyle: false,
          });
        });
    },

    deleteEmail(ctx, id) {
      return new Promise((resolve, reject) => {
        fetch(`/api/emails/${id}/`, requestConfig(null, "DELETE"))
          .then(async (response) => {
            await response;

            if (!response.ok) {
              let error = response.statusText;
              throw Error(error);
            }

            ctx.commit("SET_SNACKBAR", {
              show: true,
              text: "Email successfully deleted!",
              successStyle: true,
            });
            resolve(response);
          })
          .catch((error) => {
            ctx.commit("SET_SNACKBAR", {
              show: true,
              text: "Email deleting is failed. " + error,
              successStyle: false,
            });
            reject({ error });
          });
      });
    },
  },
  getters: {
    snackbar: (state) => state.snackbar,
    emailForm: (state) => state.emailForm,
    sentMessages: (state) => state.sentMessages,
    receivedMessages: (state) => state.receivedMessages,
    userId: (state) => state.userId,
  },
};
