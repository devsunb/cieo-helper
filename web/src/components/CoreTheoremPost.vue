<template>
  <div>
    <modal @close="closeNodeModal">
      <h3 slot="header">{{ nodeInfo.name }}</h3>
      <div slot="body">
        <ul class="nav nav-tabs modal-tabs">
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'nodeInfo', params: { id }, query: { type: 'intro' }}" exact-active-class="active">소개</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'nodeInfo', params: { id }, query: { type: 'process' }}" exact-active-class="active"><i class="fas fa-spinner"></i><span class="badge badge-light">{{ nodeInfo.process }}</span></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'nodeInfo', params: { id }, query: { type: 'waiting' }}" exact-active-class="active"><i class="fas fa-hourglass-half"></i><span class="badge badge-light">{{ nodeInfo.waiting }}</span></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'nodeInfo', params: { id }, query: { type: 'clear' }}" exact-active-class="active"><i class="fas fa-check-square"></i><span class="badge badge-light">{{ nodeInfo.clear }}</span></router-link>
          </li>
        </ul>
        <pre class="node-description" v-if="type == 'intro'">{{ nodeInfo.description }}</pre>
        <div class="node-process" v-if="type == 'process'">
          <p class="text-info"><i class="fas fa-spinner mr-2"></i>내부 회의가 진행 중인 항목들</p>
          <div class="list-group">
            <router-link class="list-group-item list-group-item-action list-group-item-info" :to="{name:'main'}">Dapibus ac facilisis in</router-link>
          </div>
        </div>
        <div class="node-waiting" v-if="type == 'waiting'">
          <p class="text-danger"><i class="fas fa-spinner mr-2"></i>다른 곳에 넘겨 처리를 대기 중인 항목들</p>
          <div class="list-group">
            <router-link class="list-group-item list-group-item-action list-group-item-danger" :to="{name:'main'}">Dapibus ac facilisis in</router-link>
          </div>
        </div>
        <div class="node-clear" v-if="type == 'clear'">
          <p class="text-success"><i class="fas fa-spinner mr-2"></i>처리가 완료되어 답변이 끝난 항목들</p>
          <div class="list-group">
            <router-link class="list-group-item list-group-item-action list-group-item-success" :to="{name:'main'}">Dapibus ac facilisis in</router-link>
          </div>
        </div>
      </div>
    </modal>
  </div>
</template>

<script>
import { mapState } from "vuex";

import CONSTANT from "../constant";

import Modal from "./Modal";

export default {
    name: "core-theorem-post",
    components: { Modal }
};
</script>

<style scoped>
.modal-tabs {
    margin-bottom: 20px;
}
.modal-tabs .badge {
    margin-left: 10px;
}

.node-description {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 18px;
    text-align: center;
}

.node-process > p,
.node-waiting > p,
.node-clear > p {
    font-size: 18px;
}
</style>
