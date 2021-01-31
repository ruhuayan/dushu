<template>
    <Narbar />
    <router-view />
    <Footer />
</template>

<style lang="scss">
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    // text-align: center;
    color: #2c3e50;
}
</style>
<script>
// @ is an alias to /src
import Narbar from "@/components/Narbar.vue";
import Footer from "./components/Footer.vue";

export default {
    name: "App",
    components: { Narbar, Footer },
    data() {
        return {};
    },
};
</script>
