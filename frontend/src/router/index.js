import Vue from "vue";
import VueRouter from "vue-router";
import ManageEmails from "../views/ManageEmails.vue";
import ComposeEmail from "../views/ComposeEmail.vue";
import NotFound from "../views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/manage-emails",
    name: "manage-emails",
    component: ManageEmails,
    meta: { title: "Manage Emails" },
  },
  {
    path: "/",
    name: "compose-email",
    component: ComposeEmail,
    meta: { title: "Compose Email" },
  },
  {
    path: "*",
    name: "page-not-found",
    component: NotFound,
    meta: { title: "404" },
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
