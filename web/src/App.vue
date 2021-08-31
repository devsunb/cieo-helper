<template>
    <div id="app" class="container-fluid">
        <top-bar></top-bar>
        <div class="content">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import TopBar from "@/components/TopBar";

export default {
    name: "App",
    components: { TopBar }
};
</script>

<style>
.content {
    margin-top: 56px;
}
</style>
