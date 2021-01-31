<template>
    <div class="book">
        <h1>Book {{ id }}</h1>
    </div>
</template>
<script>
export default {
    name: "Book",
    components: {},
    props: {},
    data() {
        return {
            id: null,
            book: {},
        };
    },
    mounted: function () {
        if (this.$route.params.id) {
            this.id = this.$route.params.id;
            this.loadBook(this.id);
        }
    },
    methods: {
        loadBook: function (id) {
            console.log(id);
        },
    },
};
</script>