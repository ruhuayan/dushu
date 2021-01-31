<template>
    <div class="home">All Books</div>
</template>

<script>
export default {
    name: "Home",
    components: {},
    props: {},
    data() {
        return {
            books: [],
        };
    },
    mounted: function () {
        this.loadAllBooks();
    },
    methods: {
        loadAllBooks: function () {},
    },
};
</script>
