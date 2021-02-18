<template>
    <Narbar />
    <div class="container" :class="{ loading: loading }">
        <router-view />
    </div>
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
.container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}
</style>
<script>
import { mapState } from "vuex";
// @ is an alias to /src
import Narbar from "@/components/Narbar.vue";
import Footer from "./components/Footer.vue";

export default {
    name: "App",
    components: { Narbar, Footer },
    computed: {
        ...mapState(["loading"]),
    },
    mounted: function () {
        this.$store.dispatch("loadBooks");
    },
};
</script>
