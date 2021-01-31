<template>
    <div class="about">
        <h1>about {{ $route.params.category }} page</h1>
    </div>
</template>
<script>
export default {
    name: "About",
    components: {},
    props: {},
    data() {
        return {
            category: "",
            books: [],
        };
    },
    watch: {
        $route(route) {
            if (
                route.params.category &&
                route.params.category !== this.category
            ) {
                this.category = route.params.category;
                this.loadBooks(this.category);
            }
        },
    },
    mounted: function () {
        if (this.$route.params.category) {
            this.category = this.$route.params.category;
            this.loadBooks(this.category);
        }
    },
    methods: {
        loadBooks: function (category) {
            console.log(category);
        },
    },
};
</script>