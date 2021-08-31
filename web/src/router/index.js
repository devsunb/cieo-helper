import Vue from "vue";
import Router from "vue-router";

import MainPage from "@/components/MainPage";
import CoreTheorem from "@/components/CoreTheorem";
import CrammingCommand from "@/components/CrammingCommand";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "MainPage",
      component: MainPage
    },
    {
      path: "/core",
      name: "CoreTheorem",
      component: CoreTheorem
    },
    {
      path: "/cc",
      name: "CrammingCommand",
      component: CrammingCommand
    }
  ]
});
