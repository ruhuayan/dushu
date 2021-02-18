<template>
    <div class="book" v-if="book">
        <h1>{{ book.title }}</h1>
        <div class="desc">{{ book.description }}</div>
    </div>
</template>
<script>
export default {
    name: "Book",
    components: {},
    props: {},
    data() {
        return {};
    },
    computed: {
        book() {
            return this.$store.getters["getBookById"](this.$route.params.id);
        },
    },
    mounted: function () {},
    methods: {},
};
</script>