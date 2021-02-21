<template>
    <div class="about">
        <h1>{{ categoryCn }}</h1>
        <div class="books">
            <div class="book" v-for="book in books" :key="book.id">
                <div class="bookTitle">
                    <router-link :to="'/book/' + book.id">{{
                        book.title
                    }}</router-link>
                </div>
                <div class="bookDesc">{{ book.description }}</div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "About",
    components: {},
    props: {},
    computed: {
        books() {
            return this.$store.getters["getBookByCategory"](
                this.$route.params.category
            );
        },
        letters() {
            return Array.from({ length: 26 }).map((_, i) =>
                String.fromCharCode(i + 97)
            );
        },
    },
    data() {
        return {};
    },
    mounted: function () {},
    methods: {},
};
</script>