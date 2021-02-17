<template>
    <div class="home">Most downloaded Books</div>
    <div class="book" v-for="book in books" :key="book.id">
        <div>{{ book.id }}</div>
    </div>
</template>

<script>
import { mapState } from "vuex";
export default {
    name: "Home",
    components: {},
    props: {},
    computed: mapState(["books"]),
    // computed: {
    //     books() {
    //         return this.$store.state.books;
    //     },
    // },
    mounted: function () {
        this.$store.dispatch("loadBooks");
    },
    methods: {},
};
</script>
